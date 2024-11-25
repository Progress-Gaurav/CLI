# intro text
import subprocess

# data
# JOHN_DATA = {
#     'name': 'John Q. Public',
#     'address': '123 Main St. \nAnytown, FL 99999'
#     'siblings': ['Michael R. Public', 'Suzy Q. Public'],
#     'parents': ['John Q. Public Sr.', 'Mary S. Public'],
# }

# fixtures are initializers

# class CliVersionClass:

def test_getversion():
    # check chef-courier-cli is installed
    # TODO: need to add architecture folder as well... macos/arm macos/amd...
    proc = subprocess.run(['./bin/chef360/macos/chef-courier-cli', 'version'], capture_output=True)
    assert proc.returncode == 0
    assert b'supports' in proc.stdout # check if the text 'supports' is in the output... not sure if this works

    # check chef-node-management-cli is installed
    proc = subprocess.run(['./bin/chef360/macos/chef-node-management-cli', 'version'], capture_output=True)
    assert proc.returncode == 0
    assert b'supports' in proc.stdout # check if the text 'supports' is in the output... not sure if this works

    # check chef-platform-auth-cli is installed
    proc = subprocess.run(['./bin/chef360/macos/chef-platform-auth-cli', 'version'], capture_output=True)
    assert proc.returncode == 0
    assert b'supports' in proc.stdout # check if the text 'supports' is in the output... not sure if this works
    