# Developing tests

## install poetry
### one-time steps
poetry new <name> creates a new test folder/project for Python - only do this at start of project
poetry init (adds poetry to an existing project, creates pyproject.toml) - already done for this repo
poetry install - installs deps first time
poetry install --no-ansi --no-root (updates deps)
poetry lock - creates poetry.lock file
poetry remove - removes a dep

### after git clone locally, to set up petry config to run
poetry show - lists deps in pyproject.toml
poetry update - gets latest deps, re-writes poetry.lock
poetry run <pytest> - runs a command inside poetry

typically run this command
`poetry run pytest integration-tests\sample-test --junitxml=reports\report.xml`

Poetry useful commands - https://pytest-with-eric.com/getting-started/poetry-run-pytest/#Useful-Poetry-Commands

## test folder layout
matches Qmetry folder layout

folder name indicating the tag to upload results to (for example, folder CHEF-TC-213 will upload to https://progresssoftware.atlassian.net/plugins/servlet/ac/com.infostretch.QmetryTestManager/qtm4j-test-management?project.key=CHEF&project.id=11060#!/TestCaseDetail/2mjHqQpf7qoRY/1?projectId=11060 with @pytest.mark.testcasekey('CHEF-TC-213')  )

can have test-case specific inputs, like `job-53.json`, in the folder
(sample data inputs go in /integration-tests/chef360/generic-test-inputs like job specs, etc. - if these are test case specific, they go in the TC folder)

setup & teardown methods are in a file called <test>_setup_teardown.py per https://pytest-with-eric.com/pytest-best-practices/pytest-setup-teardown/
will use `yield` and finalizers to clean up

(shared fixtures like registering a CLI, will go in shared-fixtures directory)

More on fixtures at https://docs.pytest.org/en/latest/how-to/fixtures.html#teardown-cleanup-aka-fixture-finalization & https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest 

Good description of testing at https://realpython.com/pytest-python-testing/ 

## common utilities
go in /integration-tests/src

# Running tests locally from Terminal in VS Code
(then run tests)

With poetry, `poetry run pytest integration-tests\sample-test --junitxml=reports\report.xml`
To run the configuration tests, which test command-line flags, `poetry run pytest integration-tests\configuration --junitxml=reports\report.xml`

With only pytest, 
`pytest integration-tests --junitxml=reports\report.xml`
`pytest integration-tests\sample-test --junitxml=reports\report.xml`

## format the results in reports/report.xml
Install XML Formatter in VSCode (Fabian Lauer)
Right click --> Format Document

## marking tests for Qmetry
Use the syntax `@pytest.mark.testcasekey('CHEF-TC-1000')` to align a test with reporting into Qmetry

## running tests in EC2
Team to document how this can work
