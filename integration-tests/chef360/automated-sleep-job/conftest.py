import pytest
 
 
def pytest_addoption(parser):
    parser.addoption("--PEM_KEY", action="store", default="default4", help="Value for PEM_KEY")
    parser.addoption("--NODE_URL", action="store", default="default4", help="Value for NODE_URL")
    parser.addoption("--LICENSE_ID", action="store", default="default4", help="Value for LICENSE_ID")
 
 
 
@pytest.fixture
def get_env_variables(request):
    env1 = request.config.getoption("--PEM_KEY")
    env2 = request.config.getoption("--NODE_URL")
    env3 = request.config.getoption("--LICENSE_ID")
    return {"PEM_KEY": env1, "NODE_FQDN": env2, "LICENSE_ID": env3}
