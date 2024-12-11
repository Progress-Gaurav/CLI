import subprocess,json
import time
import os
from configparser import ConfigParser
import platform
 
# #### Helm Setup
# curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
def test_download_helm_binary():
        print("\n",1," Downloading Helm Setup")
        download_helm=subprocess.run(f"curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3",shell=True,capture_output=True)
        print(download_helm.stdout)
        assert download_helm.returncode==0
 

# chmod 700 get_helm.sh
def test_Helm_permission():
        print("\n",2," Changing the permissions of get_helm.sh to make it executable by the owner only")
        change_helm_permission=subprocess.run(f"chmod 700 get_helm.sh",shell=True,capture_output=True)
        print(change_helm_permission.stdout)
        assert change_helm_permission.returncode==0
 
#./get_helm.sh
def test_install_Helm():
        print("\n",3," Executes the get_helm.sh script, which installs Helm")
        helm_install=subprocess.run(f"./get_helm.sh",shell=True,capture_output=True)
        time.sleep(5)
        print(helm_install.stdout)
        assert helm_install.returncode==0
        
 
#helm version
def test_get_Helm_version():
        print("\n",4," Verifies the installation and displays the Helm version.")
        helm_version=subprocess.run(f"helm version",shell=True,capture_output=True)
        print(helm_version.stdout)
        assert helm_version.returncode==0



#If on Ubuntu:
#sudo apt update -y
def update_ubuntu():
        print("\n",5," Updates the package list using the apt package manager.")
        ubuntu_update=subprocess.run(f"sudo apt update -y",shell=True,capture_output=True)
        time.sleep(15)
        print(ubuntu_update.stdout)
        assert ubuntu_update.returncode==0
        
 

# sudo snap install docker
def install_docker_on_ubuntu():
        print("\n",6, " Installs Docker via the Snap package manager")
        install_docker=subprocess.run(f"sudo snap install docker",shell=True,capture_output=True)
        time.sleep(10)
        print(install_docker.stdout)
        assert  install_docker.returncode==0
 

# sudo snap start docker
def starting_docker_on_ubuntu():
        print("\n",7," Starts the Docker service.")
        start_docker=subprocess.run(f"sudo snap start docker",shell=True,capture_output=True)
        print(start_docker.stdout)
        assert start_docker.returncode==0


#If on RHEL, Centos or Amazon Linux:
def update_linux():
        print("\n",7," Updates the package list using the apt package manager.")
        linux_update=subprocess.run(f"sudo yum update -y",shell=True,capture_output=True)
        print(linux_update.stdout)
        assert linux_update.returncode==0


def install_docker_on_linux():
        print("\n",7," Starts the Docker service.")
        install_docker=subprocess.run(f"sudo yum install docker -y",shell=True,capture_output=True)
        print(install_docker.stdout)
        assert install_docker.returncode==0


def start_docker_on_linux():
        print("\n",7," Starts the Docker service.")
        start_docker=subprocess.run(f"sudo systemctl start docker",shell=True,capture_output=True)
        print(start_docker.stdout)
        assert start_docker.returncode==0


def add_user_linux():
        print("\n",7," Adds the current user to the docker group.")
        add_user=subprocess.run(f"sudo usermod -aG docker $USER && newgrp docker",shell=True,capture_output=True)
        print(add_user.stdout)
        assert add_user.returncode==0


def test_install_docker():
    current_os = platform.system()
    print(current_os)
    
    if current_os == "Linux":
        with open("/etc/os-release") as file_data:
                os_info = file_data.read()

                if "Ubuntu" in os_info:
                      update_ubuntu()
                      install_docker_on_ubuntu()
                      starting_docker_on_ubuntu()
                else:
                      update_linux()
                      install_docker_on_linux()
                      start_docker_on_linux()
                      add_user_linux()     
    elif current_os == "Windows":
        print("Not supported")
    else:
        print(f"Unsupported OS: {current_os}")
 

 
#curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
def test_download_binary_kubectl():
        print("\n",8," Downloads the latest stable version of the kubectl binary for Linux (amd64 architecture)")
        download_kubectl=subprocess.run(f"curl -LO \"https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl\"",shell=True,capture_output=True)
        time.sleep(10)
        print(download_kubectl.stdout)
        assert download_kubectl.returncode==0
 

 # chmod +x kubectl
def test_set_kubectl():
        print("\n",9, " Ensures kubectl is executable")
        make_kubectl_executable=subprocess.run(f"chmod +x kubectl",shell=True,capture_output=True)
        print(make_kubectl_executable.stdout)
        assert make_kubectl_executable.returncode==0


# sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
def test_install_kubectl():
        print("\n",10, " Installs the kubectl binary to /usr/local/bin with proper ownership and permissions.")
        kubectl_install=subprocess.run(f"sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl",shell=True,capture_output=True)
        print(kubectl_install.stdout)
        assert  kubectl_install.returncode==0
 


 

# mkdir -p ~/.local/bin
def test_create_directory():
        print("\n",11, " Creates a directory (~/.local/bin) if it doesn't already exist.")
        create_directory=subprocess.run(f"sudo mkdir -p /root/.local/bin",shell=True,capture_output=True)
        print(create_directory.stdout)
        assert create_directory.returncode==0


# mv ./kubectl ~/.local/bin/kubectl
def test_move_kubernetes():
        print("\n",12, " Moves the kubectl binary to the ~/.local/bin directory.")
        moving_kubernetes=subprocess.run(f"sudo mv ./kubectl /root/.local/bin/kubectl",shell=True,capture_output=True)
        print(moving_kubernetes.stdout)
        assert moving_kubernetes.returncode==0  
 

# # kubectl version
def test_kubernetes_version_check():
        print("\n",13, " Verifies the installation and displays the kubectl version")
        kubernetes_version=subprocess.run(f"sudo kubectl version",shell=True,capture_output=True)
        print(kubernetes_version.stdout)
        assert b'Version:' in kubernetes_version.stdout


# # curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
def test_download_minikube():
        print("\n",14," Downloads the latest Minikube binary for Linux (amd64 architecture).")
        download_minikube=subprocess.run(f"curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 ",shell=True,capture_output=True)
        time.sleep(20)
        print(download_minikube.stdout)
        assert download_minikube.returncode==0
 

# # sudo install minikube-linux-amd64 /usr/local/bin/minikube
def test_install_minikube():
        print("\n",15," installs the Minikube binary to /usr/local/bin.")
        install_minikube=subprocess.run(f"sudo install minikube-linux-amd64 /usr/local/bin/minikube ",shell=True,capture_output=True)
        time.sleep(3)
        print(install_minikube.stdout)
        assert install_minikube.returncode==0     
 

# minikube version
def test_minikube_version():
        print("\n",16," Verifies the installation and displays the Minikube version")
        minikube_version=subprocess.run(f"sudo minikube version",shell=True,capture_output=True)
        print(minikube_version.stdout)
        assert  b'version' in minikube_version.stdout.lower(), "no version found" 


# minikube start --force
def test_minikube_start():
        print("\n",17," Starts a Minikube cluster.")
        start_minikube=subprocess.run(f"sudo minikube start --force",shell=True,capture_output=True)
        time.sleep(20)
        print(start_minikube.stdout)
        assert start_minikube.returncode==0
        
 

# # minikube status
def test_minikube_status():
        print("\n",18, " Displays the status of the Minikube cluster (e.g., whether it's running).")
        minikube_status=subprocess.run(f"sudo minikube status",shell=True,capture_output=True)
        print(minikube_status.stdout)
        assert minikube_status.returncode==0



# yes \"y\" | sudo apt install awscli
def test_install_awscli():
        print("\n",19, " Install AWSCLIs")
        awscli=subprocess.run(f"yes \"y\" | sudo apt install awscli",shell=True,capture_output=True)
        print( awscli.stdout)
        assert  awscli.returncode==0

def test_set_access_keys(get_env_variables):
    print("\n",20, " Configuring AWS credentials")

    # Fetch environment variables
    AWS_ACCESS_KEY_ID = get_env_variables["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY = get_env_variables["AWS_SECRET_ACCESS_KEY"]
    AWS_SESSION_TOKEN = get_env_variables["AWS_SESSION_TOKEN"]

    complete_path=os.path.expanduser("~/")
    print(complete_path)
    create_aws_directory="mkdir -p "+complete_path+".aws"
    create_directory=subprocess.run(create_aws_directory,shell=True,capture_output=True)
    print(create_directory.stdout)
    assert create_directory.returncode==0 ,"fail to create a directory .aws"
    

    # AWS credentials file path
    credentials_file = complete_path+".aws/credentials"
    print(credentials_file)

    #  Create config parser for credentials file
    credentials = ConfigParser()
    credentials.read(credentials_file)

    # Set credentials under the default profile
    if not credentials.has_section('default'):
        credentials.add_section('default')

    credentials.set('default', 'aws_access_key_id', AWS_ACCESS_KEY_ID)
    credentials.set('default', 'aws_secret_access_key', AWS_SECRET_ACCESS_KEY)
    credentials.set('default', 'aws_session_token', AWS_SESSION_TOKEN)
    
    # Write the updated credentials file
    with open(credentials_file, 'w') as filedata:
        credentials.write(filedata)
    print("AWS credentials and config files have been updated.")

    assert (
        credentials.get('default', 'aws_access_key_id') == AWS_ACCESS_KEY_ID and
        credentials.get('default', 'aws_secret_access_key') == AWS_SECRET_ACCESS_KEY and
        credentials.get('default', 'aws_session_token') == AWS_SESSION_TOKEN
    ), "AWS credentials are not set correctly in the file."


def test_awscli_version_check():
        print("\n",21, "Checking AWS installation")
        awscli_version=subprocess.run(f"aws --version",shell=True,capture_output=True)
        print( awscli_version.stdout)
        assert  awscli_version.returncode==0

    
# kubectl create secret docker-registry regcred  --docker-server=448877188565.dkr.ecr.us-east-2.amazonaws.com   --docker-username=AWS   --docker-password=$(aws ecr get-login-password --region us-east-2)
def test_create_image_secret():
    print("\n",22, " The command creates a Kubernetes secret (regcred) to store credentials for authenticating with an Amazon Elastic Container Registry (ECR). This allows Kubernetes to securely pull private container images from the specified ECR repository.")
    create_image=subprocess.run(f"sudo kubectl create secret docker-registry regcred  --docker-server=448877188565.dkr.ecr.us-east-2.amazonaws.com   --docker-username=AWS   --docker-password=$(aws ecr get-login-password --region us-east-2)",shell=True,capture_output=True)
    print(create_image.stdout)
    assert create_image.returncode==0
 
 
#sudo apt install git -y
def test_install_git():
    print("\n",23, " Installing Git")
    git_installation=subprocess.run(f"sudo apt install git -y",shell=True,capture_output=True)
    print(git_installation.stdout)
    assert git_installation.returncode==0
 
#git clone git@github.com:progress-platform-services/helm.git
def test_clone_git():
    print("\n",24, " Cloning git repository")
    clone_repo=subprocess.run(f"GIT_SSH_COMMAND=\"ssh -o StrictHostKeyChecking=no\" git clone git@github.com:progress-platform-services/helm.git",shell=True,capture_output=True)
    print( clone_repo.stdout)
    assert clone_repo.returncode==0


#sed -i 's/tenant-1.dev-360.chef.co/ec2-3-94-190-118.compute-1.amazonaws.com/g' values.yaml
def test_change_tenant_fqdn(get_env_variables):
    print("\n",25, " changing FQDN in the file")
    #monkeypatch.setenv("FQDN", get_env_variables["FQDN"])
    FQDN = get_env_variables["FQDN"]
    
    print(FQDN)
    values_file_path=os.path.expanduser("helm/chef-platform/values.yaml")
    change_fqdn="sed -i 's/tenant-1.dev-360.chef.co/"+FQDN+"/g' "+values_file_path
    running_change_fqdn=subprocess.run(change_fqdn,shell=True,capture_output=True)
    print(running_change_fqdn.stdout)
    assert running_change_fqdn.returncode==0
    
 
# #sudo helm install chef-platform .
def test_install_chef_platform():
    print("\n",26, " Installing chef platform")
    path_to_install_chef= os.path.expanduser("helm/chef-platform")
    chef_installation=subprocess.run(f"sudo helm install chef-platform .",shell=True,capture_output=True, cwd=path_to_install_chef)
    print( chef_installation.stdout)
    assert  chef_installation.returncode==0


def test_mailpit_port_exposure(get_env_variables):
    port_for_mailpit=get_env_variables["PORT_FOR_MAILPIT"]
    print("\n",27, " This command runs kubectl port-forward in the background (using nohup) to expose the mailpit service in the default namespace on localhost and all network interfaces (0.0.0.0), mapping port 31100 to 8025")
    command_for_port_forwarding = "sudo nohup kubectl port-forward --namespace default service/mailpit --address 0.0.0.0 "+port_for_mailpit+":8025 &"
    process = subprocess.Popen(command_for_port_forwarding, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Wait for a moment to ensure the process starts
    time.sleep(2)


def test_reverse_proxy(get_env_variables):
    port_for_nginx_reverse_proxy=get_env_variables["PORT_FOR_NGINX_REVERSE_PROXY"]
    print("\n",28," This command runs kubectl port-forward in the background (using nohup) to expose the nginx-reverse-proxy service in the default namespace on all network interfaces (0.0.0.0), mapping port 31000 on the host to port 8080 on the service..")
    command_for_port_forwarding = "sudo nohup kubectl port-forward --namespace default service/nginx-reverse-proxy --address 0.0.0.0 "+port_for_nginx_reverse_proxy+":8080 &"
    process = subprocess.Popen(command_for_port_forwarding, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Wait for a moment to ensure the process starts
    time.sleep(2)


def test_rabbit_mq(get_env_variables):
    port_for_rabbitmq=get_env_variables["PORT_FOR_RABBITMQ"]
    print("\n",29," It forwards local port 31050 to port 5672 of the chef-platform-rabbitmq service in the Kubernetes default namespace, making RabbitMQ accessible externally")
    command_for_port_forwarding = "sudo nohup kubectl port-forward --namespace default service/chef-platform-rabbitmq --address 0.0.0.0 "+port_for_rabbitmq+":5672 &"
    process = subprocess.Popen(command_for_port_forwarding, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Wait for a moment to ensure the process starts
    time.sleep(2)


def test_install_cli(get_env_variables):
    current_os = platform.system()
    print("\n", current_os)
    FQDN = get_env_variables["FQDN"]
    
    if current_os == "Linux":
        for_linux(FQDN)
    elif current_os == "Darwin":
        for_MAC(FQDN)
#     elif current_os == "Windows":
        # for_Windows(FQDN)
    else:
        print(f"Unsupported OS: {current_os}")


def for_MAC(FQDN):
    download_chef_platform_auth_cli= "curl -sk http://"+FQDN+":31000/platform/bundledtools/v1/static/install.sh | TOOL=\"chef-platform-auth-cli\" SERVER=\"http://"+FQDN+":31000\" VERSION=\"latest\" bash -"
    command1=subprocess.run(download_chef_platform_auth_cli,shell=True)
    download_node_management_cli= "curl -sk http://"+FQDN+":31000/platform/bundledtools/v1/static/install.sh | TOOL=\"chef-node-management-cli\" SERVER=\"http://"+FQDN+":31000\" VERSION=\"latest\" bash -"
    command2=subprocess.run(download_node_management_cli,shell=True)
    download_chef_courier_cli= "curl -sk http://"+FQDN+":31000/platform/bundledtools/v1/static/install.sh | TOOL=\"chef-courier-cli\" SERVER=\"http://"+FQDN+":31000\" VERSION=\"latest\" bash -"
    command3=subprocess.run(download_chef_courier_cli,shell=True)


def for_linux(FQDN):
    download_chef_platform_auth_cli= "curl -sk http://"+FQDN+":31000/platform/bundledtools/v1/static/install.sh | TOOL=\"chef-platform-auth-cli\" SERVER=\"http://"+FQDN+":31000\" VERSION=\"latest\" bash -"
    command1=subprocess.run(download_chef_platform_auth_cli,shell=True)
    download_node_management_cli= "curl -sk http://"+FQDN+":31000/platform/bundledtools/v1/static/install.sh | TOOL=\"chef-node-management-cli\" SERVER=\"http://"+FQDN+":31000\" VERSION=\"latest\" bash -"
    command2=subprocess.run(download_node_management_cli,shell=True)
    download_chef_courier_cli= "curl -sk http://"+FQDN+":31000/platform/bundledtools/v1/static/install.sh | TOOL=\"chef-courier-cli\" SERVER=\"http://"+FQDN+":31000\" VERSION=\"latest\" bash -"
    command3=subprocess.run(download_chef_courier_cli,shell=True)


# def for_Windows(FQDN):
#     download_chef_platform_auth_cli="$env:TOOL=\"chef-platform-auth-cli\"; $env:SERVER=\"http://"+FQDN+":31000\"; Invoke-WebRequest -Uri \"http://"+FQDN+":31000/platform/bundledtools/v1/static/install.ps1\" -UseBasicParsing | Invoke-Expression"
#     command1=subprocess.run(download_chef_platform_auth_cli,shell=True)
#     download_node_management_cli="$env:TOOL=\"chef-node-management-cli\"; $env:SERVER=\"http://"+FQDN+":31000\"; Invoke-WebRequest -Uri \"http://"+FQDN+":31000/platform/bundledtools/v1/static/install.ps1\" -UseBasicParsing | Invoke-Expression"
#     command2=subprocess.run(download_node_management_cli,shell=True)
#     download_chef_courier_cli="$env:TOOL=\"chef-courier-cli\"; $env:SERVER=\"http://"+FQDN+":31000\"; Invoke-WebRequest -Uri \"http://"+FQDN+":31000/platform/bundledtools/v1/static/install.ps1\" -UseBasicParsing | Invoke-Expression"
#     command3=subprocess.run(download_chef_courier_cli,shell=True)



def test_cli_installed():
    checkstatus_platform_auth_cli=subprocess.run('chef-platform-auth-cli --help',capture_output=True,shell=True,text=True)
    print(checkstatus_platform_auth_cli.stdout)
    assert checkstatus_platform_auth_cli.returncode==0

    checkstatus_chef_courier_cli=subprocess.run('chef-courier-cli --help',capture_output=True,shell=True, text=True)
    print(checkstatus_chef_courier_cli.stdout)
    assert checkstatus_chef_courier_cli.returncode==0

    checkstatus_node_management_cli=subprocess.run('chef-node-management-cli --help',capture_output=True,shell=True,text=True)
    print(checkstatus_node_management_cli.stdout)
    assert checkstatus_node_management_cli.returncode==0







