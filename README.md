# chef-integration-tests
This repository contains pyTest and manual tests against all products for use in the Integration and Staging/QA environments

Home page for integration testing - https://chefio.atlassian.net/wiki/spaces/AR/pages/3014066189/Running+tests+and+filing+bug+reports

## Setting up your workstation
The easy way is to install pytest, then poetry then follow the dev_docs to install all deps using poetry.

The components which get installed are 
- install python - https://www.python.org/downloads/
- install pytest - https://docs.pytest.org/en/stable/getting-started.html
- install junitparser - `pip install junitparser`
- install pipx - https://pipx.pypa.io/stable/installation/#on-windows
- install poetry - https://python-poetry.org/docs/

## Running the repo locally
See documentation\running-tests.md

## Running the Github Actions
See documentation\running-github-action.md

## repository folder structure
- `/bin` contains copies of test command lines bu --test-runner flag (windows/linux/macos)
- the --test-suite flag controls which tests are run

## To-do
1. Get linux & MacOS versions of CLIs (make switchable, and preconditions/fixtures/yield) - add to GHA matrix
1. Merge George's code
    - https://joaodlf.com/using-poetry-in-github-actions-the-easy-way

1. Sudharshan to talk about test expectations
1. Team to identify cluster pre-setup tasks, and logical test environment -- documentation\assets\logical test environment.png
1. Team to identify inputs required for CLI operations

chef-courier-cli register-device --cafile <file> --device-name <GHrunner or your machine name/`hostname`> --profile-name <default, which will be supplied on later cmds> --url <tenant>

1. Team to start identifying/estimating stories (subtasks for setup, default docs, new inputs from ENV, test steps - define CLI's, extpected output - generated manually, coded as assert using jq)

1. Pull the latest command lines in GHA from 
    - https://github.com/progress-platform-services/chef-node-management-cli/releases 
    - https://github.com/progress-platform-services/chef-courier-cli/releases
    - https://github.com/progress-platform-services/chef-platform-auth-cli/releases
    can wget/curl
    - create a test ixture to make sure CLIs are loaded locally (do not actually download in the TF - use a /script for local install or add a step in GHA - since it will have access to private repos)
1. Where did Windows version of CLI go? needs to be readded --> file chef360 bug
1. Verify chef360 CLIs rebuild & are on releases?
