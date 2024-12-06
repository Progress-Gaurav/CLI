import pytest

def pytest_addoption(parser):
    parser.addoption("--AWS_ACCESS_KEY_ID", action="store", default="default1", help="Value for AWS_ACCESS_KEY_ID")
    parser.addoption("--AWS_SECRET_ACCESS_KEY", action="store", default="default2", help="Value for AWS_SECRET_ACCESS_KEY")
    parser.addoption("--AWS_SESSION_TOKEN", action="store", default="default3", help="Value for AWS_SESSION_TOKEN")
    parser.addoption("--FQDN", action="store", default="default4", help="Value for FQDN")


@pytest.fixture
def get_env_variables(request):
    env1 = request.config.getoption("--AWS_ACCESS_KEY_ID")
    env2 = request.config.getoption("--AWS_SECRET_ACCESS_KEY")
    env3 = request.config.getoption("--AWS_SESSION_TOKEN")
    env4 = request.config.getoption("--FQDN")
    return {"AWS_ACCESS_KEY_ID": env1, "AWS_SECRET_ACCESS_KEY": env2, "AWS_SESSION_TOKEN": env3, "FQDN": env4}