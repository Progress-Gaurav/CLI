import logging
import os
import re
import pytest
from junitparser import JUnitXml, TestSuite, TestCase
from _pytest.junitxml import LogXML
import xml.etree.ElementTree as ET
from qmetryupload import upload_test_results
import json

REPORT_PATH = 'report.xml'
REPORTING_MARKERS = ['testcasekey', 'storykey']

# add command-line (or ENV var) parameters in this method (pytest_addoption), and 
# create as fixtures (like in def qmetrykey right below)
# then refer to as input variables to methods as in integration-tests\configuration\config_options_test.py
def pytest_addoption(parser):
    parser.addoption(
        "--qmetrykey", action="store", help="qmetrykey: supply the API key for Qmetry"
    )
    parser.addoption(
        "--test-suite", action="store", default="chef360", help="test-suite: which set of tests to run, folder name under /integration-tests"
    )
    parser.addoption(
        "--test-runner", action="store", default="macos", help="test-runner: which CLIs to use, can be linux, windows, or macos"
    )
    parser.addoption(
        "--cafile", action="store", default="foo.pem", help="cafile: name of the CA file in integration-tests\chef360\nodes for chef360 tests"
    )
    parser.addoption(
        "--device-name", action="store", default="localhost", help="device-name: hostname where tests are running"
    )
    parser.addoption(
        "--profile-name", action="store", default="default", help="profile-name: for chef360 register-device"
    )
    parser.addoption(
        "--tenant-domain", action="store", help="tenant-domain: something like in qa1.demos.chef.co"
    )
    parser.addoption(
        "--tenant-url", action="store", help="tenant-url: usually http:// + tenant-domain + :31000"
    )
    # parser.addoption(
    #     "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    # )

@pytest.fixture
def qmetrykey(request):
    logging.info('qmetrykey read as: ' + request.config.getoption("--qmetrykey"))
    return request.config.getoption("--qmetrykey")

@pytest.fixture
def testsuite(request):
    logging.info('test-suite read as: ' + request.config.getoption("--test-suite"))
    # TODO: convert this from just a folder to tagged tests
    return request.config.getoption("--test-suite")

@pytest.fixture
def testrunnerOS(request):
    logging.info('test-runner read as: ' + request.config.getoption("--test-runner"))
    # TODO: validate that it is macos, linux, windows
    return request.config.getoption("--test-runner")

@pytest.fixture
def chef360CAFilename(request):
    logging.info('cafile read as: ' + request.config.getoption("--cafile"))
    # TODO: validate that file exists
    return request.config.getoption("--cafile")

@pytest.fixture
def chef360devicename(request):
    logging.info('device-name read as: ' + request.config.getoption("--device-name"))
    # TODO: call hostname if blank
    return request.config.getoption("--device-name")

@pytest.fixture
def chef360profile(request):
    logging.info('profile-name read as: ' + request.config.getoption("--profile-name"))
    return request.config.getoption("--profile-name")

@pytest.fixture
def chef360tenantDomain(request):
    logging.info('tenant-domain read as: ' + request.config.getoption("--tenant-domain"))
    return request.config.getoption("--tenant-domain")

@pytest.fixture
def chef360tenantServiceURL(request):
    strURL = request.config.getoption("--tenant-url")
    if request.config.getoption("--tenant-url") == "":
        strURL = "http://" + request.config.getoption("--tenant-domain") + ":31000"
    logging.info('tenant-url read as: ' + strURL)
    return strURL

#OLD SAMPLE @pytest.fixture
# def cmdopt(request):
#     logging.info('cmdopt read as: ' + request.config.getoption("--cmdopt"))
#     return request.config.getoption("--cmdopt")

def parse_report_xml(junitxml, item_classnames):
    tree = ET.parse(junitxml)
    root = tree.getroot()

    for testsuite in root.iter('testsuite'):
        suite_name = testsuite.get('name')
        
        # Check if the suite name matches any key in item_classnames
        if suite_name in item_classnames:
            value = item_classnames[suite_name]
            if all(marker in value for marker in REPORTING_MARKERS):
                # Filter out empty strings and combine keys with their values
                pattern = '|'.join(REPORTING_MARKERS)
                markers = re.split(f'({pattern})', value)
                markers = [f'{markers[i]}={markers[i+1].strip()}' for i in range(1, len(markers)-1, 2)]
                for marker in markers:
                    key, val = marker.split('==')
                    testsuite.set(key, val.strip('"'))
            else:
                key, val = value.split('=')
                testsuite.set(key, val.strip('"'))

    # Save the modified XML back to the file
    tree.write(junitxml, encoding='utf-8', xml_declaration=True)
        
def pytest_configure(config):
    # Register the custom XML reporter with the static path
    junitxml = getattr(config.option, 'xmlpath', None)
    config._xml = CustomJUnitXML(junitxml)
    config.pluginmanager.register(config._xml)
    # logging.info('qmetrykey read as: ' + config.getoption("--qmetrykey"))

## The CustomJUnitXML class extends the LogXML class and overrides the pytest_sessionfinish method to split the consolidated XML report into individual test suites.
## The default Junit report generated by pytest is a consolidated report that contains all the test cases. The split_junit_report method 
## reads the consolidated report and splits it into individual test suites based on the test case class name. 
class CustomJUnitXML(LogXML):
    def __init__(self, logfile):
        if logfile is None:
            logfile = REPORT_PATH
        super().__init__(logfile, prefix='')
        self.logfile = logfile
        self.session = None

    def pytest_sessionstart(self, session):
        # Store the session object
        self.session = session

    def pytest_sessionfinish(self, session, exitstatus):
        # Perform post-processing directly after the test session
        self.split_junit_report(self.logfile, session)

    def split_junit_report(self, input_file, session):

        if input_file is None:
            return
        xml = JUnitXml.fromfile(input_file)
        suites = {}
    
        for suite in xml:
            for case in suite:
                if case.classname not in suites:
                    suites[case.classname] = TestSuite(name=case.classname)
                    
                # Create a TestCase for each test and add it to the suite
                new_case = TestCase(name=case.name, classname=case.classname, time=case.time)
                new_case.result = case.result
                suites[case.classname].add_testcase(new_case)
                suites[case.classname].time += case.time
    
        # Write all suites to a single file
        consolidated_xml = JUnitXml()
        for suite in suites.values():
            consolidated_xml.add_testsuite(suite)

        consolidated_xml.write(input_file)
    
@pytest.hookimpl(tryfirst=True)
def get_key(functionname):
    with open("CLI/integration-tests/chef360/Test-Cases.json", "r") as f:
        data = json.load(f)
    for key, value in data.items():
        if functionname in key:
            return value
    return None
        

@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(items, session):
    item_classnames = {}
    # Extract marker information from each test item
    
    for item in items:
        findkeybyclass= str(item.parent.name)
        key = get_key(findkeybyclass)
        marker_strings = []
        for marker in item.iter_markers():
            ## verify that the marker only has testcasekey
            if marker.name in REPORTING_MARKERS:
                if marker.args:
                    marker_string = f'{marker.name}="{marker.args[0]}"'
                else:
                    marker_string = f'{marker.name}="{key}"'
                marker_strings.append(marker_string)

        markers_str = " ".join(marker_strings)
        
        ## split the information required to store the testsuite name and the markers
        node_parts = item.nodeid.split("::")
        file_path = os.path.splitext(node_parts[0])[0]  # Get the file path without the test case
        class_name = node_parts[1]  # Get the class name
        suite_name = f"{file_path}.{class_name}".replace(os.sep, '.')  # Combine and replace slashes with dots
        
        if (markers_str != '' or None):
            item_classnames[suite_name] = markers_str

    session.item_classnames = item_classnames

def pytest_sessionfinish(session,exitstatus):
    junitxml = getattr(session.config.option, 'xmlpath', None)
    if junitxml is None:
        junitxml = REPORT_PATH
   
    logging.info(f'Uploading test results to QMetry')
    if session.item_classnames:
        parse_report_xml(junitxml,session.item_classnames)
        apiKey = getattr(session.config.option, 'qmetrykey', None)
        logging.info('USING API KEY ' + apiKey)
        upload_test_results(junitxml, apiKey)
