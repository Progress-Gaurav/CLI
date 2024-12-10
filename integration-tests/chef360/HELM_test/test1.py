import subprocess,json
import time
import os
from configparser import ConfigParser
 
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
def test_ubuntu():
        print("\n",5," Updates the package list using the apt package manager.")
        list_jobs=subprocess.run(f"sudo apt update -y",shell=True,capture_output=True)
        time.sleep(15)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
        
 

# sudo snap install docker
def test_instll_docker():
        print("\n",6, " Installs Docker via the Snap package manager")
        list_jobs=subprocess.run(f"sudo snap install docker",shell=True,capture_output=True)
        time.sleep(10)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
 

# sudo snap start docker
def test_start_docker():
        print("\n",7," Starts the Docker service.")
        list_jobs=subprocess.run(f"sudo snap start docker",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
 


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

def test_get_access_keys(get_env_variables, monkeypatch):
    print("\n",20, " Configuring AWS credentials")

    # Fetch environment variables
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")

   
    list_jobs=subprocess.run(f"mkdir -p ~/.aws",shell=True,capture_output=True)
    print( list_jobs.stdout)
    assert  list_jobs.returncode==0
    
    list_jobs=subprocess.run(f"echo \"[default]\" > ~/.aws/credentials",shell=True,capture_output=True)
    print( list_jobs.stdout)
    assert  list_jobs.returncode==0

    cmd1="echo \"aws_access_key_id=\" "+AWS_ACCESS_KEY_ID+" >> ~/.aws/credentials"
    list_jobs=subprocess.run(cmd1,shell=True,capture_output=True)
    print( list_jobs.stdout)
    assert  list_jobs.returncode==0

    cmd2="echo \"aws_secret_access_key=\" "+AWS_SECRET_ACCESS_KEY+" >> ~/.aws/credentials"
    list_jobs=subprocess.run(cmd2,shell=True,capture_output=True)
    print( list_jobs.stdout)
    assert  list_jobs.returncode==0

    aws_access_key_id = AWS_ACCESS_KEY_ID
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    aws_session_token = AWS_SESSION_TOKEN

    # AWS credentials file path
    credentials_file = os.path.expanduser("~/.aws/credentials")
    config_file = os.path.expanduser("~/.aws/config")

    #  Create config parser for credentials file
    credentials = ConfigParser()
    credentials.read(credentials_file)

    # Set credentials under the default profile
    if not credentials.has_section('default'):
        credentials.add_section('default')
    credentials.set('default', 'aws_access_key_id', aws_access_key_id)
    credentials.set('default', 'aws_secret_access_key', aws_secret_access_key)
    credentials.set('default', 'aws_session_token', aws_session_token)

    # Write the updated credentials file
    with open(credentials_file, 'w') as f:
        credentials.write(f)

    # Create config file for region
    config = ConfigParser()
    config.read(config_file)

    # Set the region under the default profile
    if not config.has_section('default'):
        config.add_section('default')
    config.set('default', 'session_token', aws_session_token)

    # Write the updated config file
    with open(config_file, 'w') as f:
        config.write(f)

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
def test_helm_deploy(get_env_variables, monkeypatch):
    print("\n",25, " changing FQDN in the file")
    monkeypatch.setenv("FQDN", get_env_variables["FQDN"])
    FQDN = os.getenv("FQDN")
    
    print(FQDN)
    cmd="sed -i 's/tenant-1.dev-360.chef.co/"+FQDN+"/g' helm/chef-platform/values.yaml"
    list_jobs=subprocess.run(cmd,shell=True,capture_output=True)
    print( list_jobs.stdout)
    assert  list_jobs.returncode==0
    
 
# #sudo helm install chef-platform .
def test_install_chef_platform():
    print("\n",26, " Installing chef platform")
    list_jobs=subprocess.run(f"sudo helm install chef-platform .",shell=True,capture_output=True, cwd="helm/chef-platform")
    print( list_jobs.stdout)
    assert  list_jobs.returncode==0


def test_mailpit():
    print("\n",27, " This command exposes the nginx-reverse-proxy service running in Kubernetes on port 8080 to be accessible on your machine (and possibly other devices) via port 31000.")
    command = "sudo nohup kubectl port-forward --namespace default service/mailpit --address 0.0.0.0 31100:8025 &"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Wait for a moment to ensure the process starts
    time.sleep(2)


def test_reverse_proxy():
    print("\n",28," This command exposes the RabbitMQ service (chef-platform-rabbitmq) running in the Kubernetes cluster on port 5672 to your local machine’s port 31050, allowing external applications or users to connect to RabbitMQ via 31050.")
    command = "sudo nohup kubectl port-forward --namespace default service/nginx-reverse-proxy --address 0.0.0.0 31000:8080 &"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Wait for a moment to ensure the process starts
    time.sleep(2)


def test_rabbit_mq():
    print("\n",29," It forwards local port 31050 to port 5672 of the chef-platform-rabbitmq service in the Kubernetes default namespace, making RabbitMQ accessible externally")
    command = "sudo nohup kubectl port-forward --namespace default service/chef-platform-rabbitmq --address 0.0.0.0 31050:5672 &"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Wait for a moment to ensure the process starts
    time.sleep(2)




# cmd1="curl -sk http://"+FQDN+":31000/platform/bundledtools/v1/static/install.sh | TOOL=\"chef-node-management-cli\" SERVER=\""+FQDN+":31000\" VERSION=\"latest\" bash -"
# print(cmd1)


