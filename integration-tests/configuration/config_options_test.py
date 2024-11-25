import pytest
import logging

# simple tests to make sure command line flags are read in correctly

# --qmetrykey
@pytest.mark.testcasekey('CHEF-TC-1000')    
def test_qmetrykey_flag(qmetrykey):
    logging.info('qmetrykey read as: ' + qmetrykey)
    assert 1 # 0 to see what was printed
    
# --test-suite
@pytest.mark.testcasekey('CHEF-TC-1001')    
def test_testsuite_flag(testsuite):
    logging.info('test-suite read as: ' + testsuite)
    assert 1 
    
# --test-runner
@pytest.mark.testcasekey('CHEF-TC-1002')    
def test_testrunner_flag(testrunnerOS):
    logging.info('test-runner read as: ' + testrunnerOS)
    assert 1 
    
# --cafile
@pytest.mark.testcasekey('CHEF-TC-1003')    
def test_cafile_flag(chef360CAFilename):
    logging.info('cafile read as: ' + chef360CAFilename)
    assert 1     

# --device-name
@pytest.mark.testcasekey('CHEF-TC-1004')    
def test_devicename_flag(chef360devicename):
    logging.info('device-name read as: ' + chef360devicename)
    assert 1     
  
# --profile-name
@pytest.mark.testcasekey('CHEF-TC-1004')    
def test_profilename_flag(chef360profile):
    logging.info('profile-name read as: ' + chef360profile)
    assert 1     
 
# --tenant-domain
@pytest.mark.testcasekey('CHEF-TC-1005')    
def test_tenantdomain_flag(chef360tenantDomain):
    logging.info('tenant-domain read as: ' + chef360tenantDomain)
    assert 1     

@pytest.mark.testcasekey('CHEF-TC-1006')    
def test_tenanturl_flag(chef360tenantServiceURL):
    logging.info('tenant-url read as: ' + chef360tenantServiceURL)
    assert 1     

# @pytest.mark.testcasekey('CHEF-TC-1000')
# def test_answer(cmdopt):
#     if cmdopt == "type1":
#         print("first")
#     elif cmdopt == "type2":
#         print("second")
#     assert 1 # 0 to see what was printed