import subprocess,json
import time
import os
from configparser import ConfigParser
import platform
 
# #### Helm Setup
# curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
def test_Helm_setup():
        print("\n",1," Downloading Helm Setup")
        list_jobs=subprocess.run(f"curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
 

# chmod 700 get_helm.sh
def test_Helm_file():
        print("\n",2," Changing the permissions of get_helm.sh to make it executable by the owner only")
        list_jobs=subprocess.run(f"chmod 700 get_helm.sh",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
 
#./get_helm.sh
def test_get_Helm_file():
        print("\n",3," Executes the get_helm.sh script, which installs Helm")
        list_jobs=subprocess.run(f"./get_helm.sh",shell=True,capture_output=True)
        time.sleep(5)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
        
 
#helm version
def test_get_Helm_version():
        print("\n",4," Verifies the installation and displays the Helm version.")
        list_jobs=subprocess.run(f"helm version",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0



#If on Ubuntu:
#sudo apt update -y
def update_ubuntu():
        print("\n",5," Updates the package list using the apt package manager.")
        list_jobs=subprocess.run(f"sudo apt update -y",shell=True,capture_output=True)
        time.sleep(15)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
        
 

# sudo snap install docker
def install_docker_ubuntu():
        print("\n",6, " Installs Docker via the Snap package manager")
        list_jobs=subprocess.run(f"sudo snap install docker",shell=True,capture_output=True)
        time.sleep(10)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
 

# sudo snap start docker
def start_docker_ubuntu():
        print("\n",7," Starts the Docker service.")
        list_jobs=subprocess.run(f"sudo snap start docker",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0


#If on RHEL, Centos or Amazon Linux:
def update_linux():
        print("\n",7," Updates the package list using the apt package manager.")
        list_jobs=subprocess.run(f"sudo yum update -y",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0


def install_docker_linux():
        print("\n",7," Starts the Docker service.")
        list_jobs=subprocess.run(f"sudo yum install docker -y",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0


def start_docker_linux():
        print("\n",7," Starts the Docker service.")
        list_jobs=subprocess.run(f"sudo systemctl start docker",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0


def add_user_linux():
        print("\n",7," Adds the current user to the docker group.")
        list_jobs=subprocess.run(f"sudo usermod -aG docker $USER && newgrp docker",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0


def test_install_docker():
#   current_os=input("Enter the os\n1.Linux\n2.Mac OS\n3.Linux")
    current_os = platform.system()
    print(current_os)
    
    if current_os == "Linux":
        with open("/etc/os-release") as f:
                os_info = f.read()

                if "Ubuntu" in os_info:
                      update_ubuntu()
                      install_docker_ubuntu()
                      start_docker_ubuntu()
                else:
                      update_linux()
                      install_docker_linux()
                      start_docker_linux()
                      add_user_linux()     
    elif current_os == "Windows":
        print("Not supported")
    else:
        print(f"Unsupported OS: {current_os}")
 

 


#curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
def test_download_binary():
        print("\n",8," Downloads the latest stable version of the kubectl binary for Linux (amd64 architecture)")
        list_jobs=subprocess.run(f"curl -LO \"https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl\"",shell=True,capture_output=True)
        time.sleep(10)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
 

 # chmod +x kubectl
def test_set_kubectl():
        print("\n",9, " Ensures kubectl is executable")
        list_jobs=subprocess.run(f"chmod +x kubectl",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0


# sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
def test_install_kubectl():
        print("\n",10, " Installs the kubectl binary to /usr/local/bin with proper ownership and permissions.")
        list_jobs=subprocess.run(f"sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
 


 

# mkdir -p ~/.local/bin
def test_create_directory():
        print("\n",11, " Creates a directory (~/.local/bin) if it doesn't already exist.")
        list_jobs=subprocess.run(f"sudo mkdir -p /root/.local/bin",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0


# mv ./kubectl ~/.local/bin/kubectl
def test_move_kubernetes():
        print("\n",12, " Moves the kubectl binary to the ~/.local/bin directory.")
        list_jobs=subprocess.run(f"sudo mv ./kubectl /root/.local/bin/kubectl",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0  
 

# # kubectl version
def test_version_check_kubernetes():
        print("\n",13, " Verifies the installation and displays the kubectl version")
        list_jobs=subprocess.run(f"sudo kubectl version",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert b'Version:' in list_jobs.stdout


# # curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
def test_download_minikube():
        print("\n",14," Downloads the latest Minikube binary for Linux (amd64 architecture).")
        list_jobs=subprocess.run(f"curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 ",shell=True,capture_output=True)
        time.sleep(20)
        print(list_jobs.stdout)
        assert  list_jobs.returncode==0
 

# # sudo install minikube-linux-amd64 /usr/local/bin/minikube
def test_install_minikube():
        print("\n",15," installs the Minikube binary to /usr/local/bin.")
        list_jobs=subprocess.run(f"sudo install minikube-linux-amd64 /usr/local/bin/minikube ",shell=True,capture_output=True)
        time.sleep(3)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0     
 

# minikube version
def test_minikube_version():
        print("\n",16," Verifies the installation and displays the Minikube version")
        list_jobs=subprocess.run(f"sudo minikube version",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  b'version' in list_jobs.stdout.lower(), "no version found" 


# minikube start --force
def test_minikube_start():
        print("\n",17," Starts a Minikube cluster.")
        list_jobs=subprocess.run(f"sudo minikube start --force",shell=True,capture_output=True)
        time.sleep(20)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
        
 

# # minikube status
def test_minikube_status():
        print("\n",18, " Displays the status of the Minikube cluster (e.g., whether it's running).")
        list_jobs=subprocess.run(f"sudo minikube status",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0



# yes \"y\" | sudo apt install awscli
def test_install_awscli():
        print("\n",19, " Install AWSCLIs")
        list_jobs=subprocess.run(f"yes \"y\" | sudo apt install awscli",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0

def test_get_access_keys(get_env_variables):
    print("\n",20, " Configuring AWS credentials")

    # Fetch environment variables
    AWS_ACCESS_KEY_ID = get_env_variables["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY = get_env_variables["AWS_SECRET_ACCESS_KEY"]
    AWS_SESSION_TOKEN = get_env_variables["AWS_SESSION_TOKEN"]

    path1=os.path.expanduser("~/.aws")
    cmd="mkdir -p "+path1
    list_jobs=subprocess.run(cmd,shell=True,capture_output=True)
    print( list_jobs.stdout)
    assert  list_jobs.returncode==0
    

    # AWS credentials file path
    credentials_file = os.path.expanduser("~/.aws/credentials")
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
    with open(credentials_file, 'w') as f:
        credentials.write(f)
    print("AWS credentials and config files have been updated.")



def test_awscli():
        print("\n",21, "Checking AWS installation")
        list_jobs=subprocess.run(f"aws --version",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0

    
# kubectl create secret docker-registry regcred  --docker-server=448877188565.dkr.ecr.us-east-2.amazonaws.com   --docker-username=AWS   --docker-password=$(aws ecr get-login-password --region us-east-2)
def test_create_image_secret():
    print("\n",22, " The command creates a Kubernetes secret (regcred) to store credentials for authenticating with an Amazon Elastic Container Registry (ECR). This allows Kubernetes to securely pull private container images from the specified ECR repository.")
    list_jobs=subprocess.run(f"sudo kubectl create secret docker-registry regcred  --docker-server=448877188565.dkr.ecr.us-east-2.amazonaws.com   --docker-username=AWS   --docker-password=$(aws ecr get-login-password --region us-east-2)",shell=True,capture_output=True)
    print( list_jobs.stdout)
    assert  list_jobs.returncode==0
 
 
#sudo apt install git -y
def test_install_git():
    print("\n",23, " Installing Git")
    list_jobs=subprocess.run(f"sudo apt install git -y",shell=True,capture_output=True)
    print( list_jobs.stdout)
    assert  list_jobs.returncode==0
 
#git clone git@github.com:progress-platform-services/helm.git
def test_clone_git():
    print("\n",24, " Cloning git repository")
    list_jobs=subprocess.run(f"GIT_SSH_COMMAND=\"ssh -o StrictHostKeyChecking=no\" git clone git@github.com:progress-platform-services/helm.git",shell=True,capture_output=True)
    print( list_jobs.stdout)
    assert  list_jobs.returncode==0


#sed -i 's/tenant-1.dev-360.chef.co/ec2-3-94-190-118.compute-1.amazonaws.com/g' values.yaml
def test_helm_deploy(get_env_variables):
    print("\n",25, " changing FQDN in the file")
    #monkeypatch.setenv("FQDN", get_env_variables["FQDN"])
    FQDN = get_env_variables["FQDN"]
    
    print(FQDN)
    path1=os.path.expanduser("helm/chef-platform/values.yaml")
    cmd="sed -i 's/tenant-1.dev-360.chef.co/"+FQDN+"/g' "+path1
    list_jobs=subprocess.run(cmd,shell=True,capture_output=True)
    print( list_jobs.stdout)
    assert  list_jobs.returncode==0
    
 
# #sudo helm install chef-platform .
def test_install_chef_platform():
    print("\n",26, " Installing chef platform")
    path1= os.path.expanduser("helm/chef-platform")
    list_jobs=subprocess.run(f"sudo helm install chef-platform .",shell=True,capture_output=True, cwd=path1)
    print( list_jobs.stdout)
    assert  list_jobs.returncode==0


def test_mailpit_port_exposure(get_env_variables):
    port=get_env_variables["PORT_FOR_MAILPIT"]
    print("\n",27, " This command runs kubectl port-forward in the background (using nohup) to expose the mailpit service in the default namespace on localhost and all network interfaces (0.0.0.0), mapping port 31100 to 8025")
    command = "sudo nohup kubectl port-forward --namespace default service/mailpit --address 0.0.0.0 "+port+":8025 &"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Wait for a moment to ensure the process starts
    time.sleep(2)


def test_reverse_proxy(get_env_variables):
    port=get_env_variables["PORT_FOR_NGINX_REVERSE_PROXY"]
    print("\n",28," This command runs kubectl port-forward in the background (using nohup) to expose the nginx-reverse-proxy service in the default namespace on all network interfaces (0.0.0.0), mapping port 31000 on the host to port 8080 on the service..")
    command = "sudo nohup kubectl port-forward --namespace default service/nginx-reverse-proxy --address 0.0.0.0 "+port+":8080 &"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Wait for a moment to ensure the process starts
    time.sleep(2)


def test_rabbit_mq(get_env_variables):
    port=get_env_variables["PORT_FOR_RABBITMQ"]
    print("\n",29," It forwards local port 31050 to port 5672 of the chef-platform-rabbitmq service in the Kubernetes default namespace, making RabbitMQ accessible externally")
    command = "sudo nohup kubectl port-forward --namespace default service/chef-platform-rabbitmq --address 0.0.0.0 "+port+":5672 &"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Wait for a moment to ensure the process starts
    time.sleep(2)



def for_MAC(FQDN):
    cmd1= "curl -sk http://"+FQDN+":31000/platform/bundledtools/v1/static/install.sh | TOOL=\"chef-platform-auth-cli\" SERVER=\""+FQDN+":31000\" VERSION=\"latest\" bash -"
    command1=subprocess.run(cmd1,shell=True)
    cmd2= "curl -sk http://"+FQDN+":31000/platform/bundledtools/v1/static/install.sh | TOOL=\"chef-node-management-cli\" SERVER=\""+FQDN+":31000\" VERSION=\"latest\" bash -"
    command2=subprocess.run(cmd2,shell=True)
    cmd3= "curl -sk http://"+FQDN+":31000/platform/bundledtools/v1/static/install.sh | TOOL=\"chef-courier-cli\" SERVER=\""+FQDN+":31000\" VERSION=\"latest\" bash -"
    command3=subprocess.run(cmd3,shell=True)

def for_linux(FQDN):
    cmd1= "curl -sk http://"+FQDN+":31000/platform/bundledtools/v1/static/install.sh | TOOL=\"chef-platform-auth-cli\" SERVER=\""+FQDN+":31000\" VERSION=\"latest\" bash -"
    command1=subprocess.run(cmd1,shell=True)
    cmd2= "curl -sk http://"+FQDN+":31000/platform/bundledtools/v1/static/install.sh | TOOL=\"chef-node-management-cli\" SERVER=\""+FQDN+":31000\" VERSION=\"latest\" bash -"
    command2=subprocess.run(cmd2,shell=True)
    cmd3= "curl -sk http://"+FQDN+":31000/platform/bundledtools/v1/static/install.sh | TOOL=\"chef-courier-cli\" SERVER=\""+FQDN+":31000\" VERSION=\"latest\" bash -"
    command3=subprocess.run(cmd3,shell=True)
def for_Windows(FQDN):
    cmd1="$env:TOOL=\"chef-platform-auth-cli\"; $env:SERVER=\""+FQDN+":31000\"; Invoke-WebRequest -Uri \""+FQDN+":31000/platform/bundledtools/v1/static/install.ps1\" -UseBasicParsing | Invoke-Expression"
    command1=subprocess.run(cmd1,shell=True)
    cmd2="$env:TOOL=\"chef-node-management-cli\"; $env:SERVER=\""+FQDN+":31000\"; Invoke-WebRequest -Uri \""+FQDN+":31000/platform/bundledtools/v1/static/install.ps1\" -UseBasicParsing | Invoke-Expression"
    command2=subprocess.run(cmd2,shell=True)
    cmd3="$env:TOOL=\"chef-courier-cli\"; $env:SERVER=\""+FQDN+":31000\"; Invoke-WebRequest -Uri \""+FQDN+":31000/platform/bundledtools/v1/static/install.ps1\" -UseBasicParsing | Invoke-Expression"
    command3=subprocess.run(cmd3,shell=True)



def test_install_cli(get_env_variables):
    current_os = platform.system()
    FQDN = get_env_variables["FQDN"]
    print(current_os)
    
    if current_os == "Linux":
        for_linux(FQDN)
    elif current_os == "Darwin":
        for_MAC(FQDN)
    elif current_os == "Windows":
        for_Windows(FQDN)
        pass
    else:
        print(f"Unsupported OS: {current_os}")







