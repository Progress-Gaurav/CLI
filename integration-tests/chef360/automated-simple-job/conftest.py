import pytest


def pytest_addoption(parser):
    parser.addoption("--PEM_KEY", action="store", default="default4", help="Value for PEM_KEY")
    parser.addoption("--NODE_FQDN", action="store", default="default4", help="Value for NODE_FQDN")
    parser.addoption("--LICENSE_ID", action="store", default="default4", help="Value for LICENSE_ID")
    parser.addoption("--NODE_USERNAME", action="store", default="ubuntu", help="Value for NODE_USERNAME")
    parser.addoption("--NODE_PORT", action="store", default="22", help="Value for NODE_PORT")



@pytest.fixture
def get_env_variables(request):
    env1 = request.config.getoption("--PEM_KEY")
    env2 = request.config.getoption("--NODE_FQDN")
    env3 = request.config.getoption("--LICENSE_ID")
    env4 = request.config.getoption("--NODE_USERNAME")
    env5 = request.config.getoption("--NODE_PORT")
    return {"PEM_KEY": env1, "NODE_FQDN": env2, "LICENSE_ID": env3, "NODE_USERNAME": env4, "NODE_PORT": env5}
