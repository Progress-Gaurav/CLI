import pytest

def pytest_addoption(parser):
    parser.addoption("--AWS_ACCESS_KEY_ID", action="store", default="default1", help="Value for AWS_ACCESS_KEY_ID")
    parser.addoption("--AWS_SECRET_ACCESS_KEY", action="store", default="default2", help="Value for AWS_SECRET_ACCESS_KEY")
    parser.addoption("--AWS_SESSION_TOKEN", action="store", default="default3", help="Value for AWS_SESSION_TOKEN")
    parser.addoption("--FQDN", action="store", default="default4", help="Value for FQDN")
    parser.addoption("--PORT_FOR_MAILPIT", action="store", default="31100", help="Value for PORT_FOR_MAILPIT")
    parser.addoption("--PORT_FOR_NGINX_REVERSE_PROXY", action="store", default="31000", help="Value for PORT_FOR_NGINX_REVERSE_PROXY")
    parser.addoption("--PORT_FOR_RABBITMQ", action="store", default="31050", help="Value for PORT_FOR_RABBITMQ")


@pytest.fixture
def get_env_variables(request):
    env1 = request.config.getoption("--AWS_ACCESS_KEY_ID")
    env2 = request.config.getoption("--AWS_SECRET_ACCESS_KEY")
    env3 = request.config.getoption("--AWS_SESSION_TOKEN")
    env4 = request.config.getoption("--FQDN")
    env5 = request.config.getoption("--PORT_FOR_MAILPIT")
    env6 = request.config.getoption("--PORT_FOR_NGINX_REVERSE_PROXY")
    env7 = request.config.getoption("--PORT_FOR_RABBITMQ")
    return {"AWS_ACCESS_KEY_ID": env1, "AWS_SECRET_ACCESS_KEY": env2, "AWS_SESSION_TOKEN": env3, "FQDN": env4, "PORT_FOR_MAILPIT": env5, "PORT_FOR_NGINX_REVERSE_PROXY": env6, "PORT_FOR_RABBITMQ": env7}