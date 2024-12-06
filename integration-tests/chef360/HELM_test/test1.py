import subprocess,json
import time
import os
from configparser import ConfigParser
 
# # #### Helm Setup
# # curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
# def test_Helm_setup():
#         print(1)
#         list_jobs=subprocess.run(f"curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
 

# # chmod 700 get_helm.sh
# def test_Helm_file():
#         print(2)
#         list_jobs=subprocess.run(f"chmod 700 get_helm.sh",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
 
# #./get_helm.sh
# def test_get_Helm_file():
#         print(3)
#         list_jobs=subprocess.run(f"./get_helm.sh",shell=True,capture_output=True)
#         time.sleep(5)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
        
 
# #helm version
# def test_get_Helm_version():
#         print(4)
#         list_jobs=subprocess.run(f"helm version",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
 
# #If on Ubuntu:
# #sudo apt update -y
# def test_ubuntu():
#         print(5)
#         list_jobs=subprocess.run(f"sudo apt update -y",shell=True,capture_output=True)
#         time.sleep(15)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
        
 

# # sudo snap install docker
# def test_instll_docker():
#         print(6)
#         list_jobs=subprocess.run(f"sudo snap install docker",shell=True,capture_output=True)
#         time.sleep(10)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
 

# # sudo snap start docker
# def test_start_docker():
#         print(7)
#         list_jobs=subprocess.run(f"sudo snap start docker",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
 

# #curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
# #curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
# def test_download_binary():
#         print(8)
#         list_jobs=subprocess.run(f"curl -LO \"https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl\"",shell=True,capture_output=True)
#         time.sleep(10)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
 

#  # chmod +x kubectl
# def test_install_kubectl():
#         print(10)
#         list_jobs=subprocess.run(f"chmod +x kubectl",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0


# # sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
# def test_install_kubectl():
#         print(9)
#         list_jobs=subprocess.run(f"sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
 


 

# # mkdir -p ~/.local/bin
# def test_create_directory():
#         print(11)
#         list_jobs=subprocess.run(f"sudo mkdir -p /root/.local/bin",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0


# # mv ./kubectl ~/.local/bin/kubectl
# def test_move_kubernetes():
#         print(12)
#         list_jobs=subprocess.run(f"sudo mv ./kubectl /root/.local/bin/kubectl",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0  
 

# # # kubectl version
# def test_version_check_kubernetes():
#         print(13)
#         list_jobs=subprocess.run(f"sudo kubectl version",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert b'Version:' in list_jobs.stdout


# # # curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
# def test_download_minikube():
#         print(14)
#         list_jobs=subprocess.run(f"curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 ",shell=True,capture_output=True)
#         time.sleep(20)
#         print(list_jobs.stdout)
#         assert  list_jobs.returncode==0
 

# # # sudo install minikube-linux-amd64 /usr/local/bin/minikube
# def test_install_minikube():
#         print(15)
#         list_jobs=subprocess.run(f"sudo install minikube-linux-amd64 /usr/local/bin/minikube ",shell=True,capture_output=True)
#         time.sleep(3)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0     
 

# # minikube version
# def test_minikube_version():
#         print(16)
#         list_jobs=subprocess.run(f"sudo minikube version",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert  b'version' in list_jobs.stdout.lower(), "no version found" 


# # minikube start --force
# def test_minikube_start():
#         print(17)
#         list_jobs=subprocess.run(f"sudo minikube start --force",shell=True,capture_output=True)
#         time.sleep(20)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
        
 

# # # minikube status
# def test_minikube_status():
#         print(18)
#         list_jobs=subprocess.run(f"sudo minikube status",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0


# # # kubectl version
# def test_version_check_kubernetes123():
#         print(13)
#         list_jobs=subprocess.run(f"sudo kubectl version",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert b'Version:' in list_jobs.stdout

# # yes \"y\" | sudo apt install awscli
# def test_install_awscli():
#         print(19)
#         list_jobs=subprocess.run(f"yes \"y\" | sudo apt install awscli",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0

# def test_get_access_keys(get_env_variables, monkeypatch):
#     # Set environment variables using monkeypatch
#     monkeypatch.setenv("AWS_ACCESS_KEY_ID", get_env_variables["AWS_ACCESS_KEY_ID"])
#     monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", get_env_variables["AWS_SECRET_ACCESS_KEY"])
#     monkeypatch.setenv("AWS_SESSION_TOKEN", get_env_variables["AWS_SESSION_TOKEN"])

#     # Fetch environment variables
#     AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
#     AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
#     AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")

#     # Print for debugging
#     print("AWS_ACCESS_KEY_ID:", AWS_ACCESS_KEY_ID)
#     print("AWS_SECRET_ACCESS_KEY:", AWS_SECRET_ACCESS_KEY)
#     print("AWS_SESSION_TOKEN:", AWS_SESSION_TOKEN)


#     list_jobs=subprocess.run(f"mkdir -p ~/.aws",shell=True,capture_output=True)
#     print( list_jobs.stdout)
#     assert  list_jobs.returncode==0
    
#     list_jobs=subprocess.run(f"echo \"[default]\" > ~/.aws/credentials",shell=True,capture_output=True)
#     print( list_jobs.stdout)
#     assert  list_jobs.returncode==0

#     cmd1="echo \"aws_access_key_id=\" "+AWS_ACCESS_KEY_ID+" >> ~/.aws/credentials"
#     list_jobs=subprocess.run(cmd1,shell=True,capture_output=True)
#     print( list_jobs.stdout)
#     assert  list_jobs.returncode==0

#     cmd2="echo \"aws_secret_access_key=\" "+AWS_SECRET_ACCESS_KEY+" >> ~/.aws/credentials"
#     list_jobs=subprocess.run(cmd2,shell=True,capture_output=True)
#     print( list_jobs.stdout)
#     assert  list_jobs.returncode==0

#     aws_access_key_id = AWS_ACCESS_KEY_ID
#     aws_secret_access_key = AWS_SECRET_ACCESS_KEY
#     aws_session_token = AWS_SESSION_TOKEN

#     # AWS credentials file path
#     credentials_file = os.path.expanduser("~/.aws/credentials")
#     config_file = os.path.expanduser("~/.aws/config")

#     #  Create config parser for credentials file
#     credentials = ConfigParser()
#     credentials.read(credentials_file)

#     # Set credentials under the default profile
#     if not credentials.has_section('default'):
#         credentials.add_section('default')
#     credentials.set('default', 'aws_access_key_id', aws_access_key_id)
#     credentials.set('default', 'aws_secret_access_key', aws_secret_access_key)
#     credentials.set('default', 'aws_session_token', aws_session_token)

#     # Write the updated credentials file
#     with open(credentials_file, 'w') as f:
#         credentials.write(f)

#     # Create config file for region
#     config = ConfigParser()
#     config.read(config_file)

#     # Set the region under the default profile
#     if not config.has_section('default'):
#         config.add_section('default')
#     config.set('default', 'session_token', aws_session_token)

#     # Write the updated config file
#     with open(config_file, 'w') as f:
#         config.write(f)

#     print("AWS credentials and config files have been updated.")


# def test_awscli():
#         print(19)
#         list_jobs=subprocess.run(f"aws --version",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0

    
# # kubectl create secret docker-registry regcred  --docker-server=448877188565.dkr.ecr.us-east-2.amazonaws.com   --docker-username=AWS   --docker-password=$(aws ecr get-login-password --region us-east-2)
# def test_create_image_secret():
#     print(19)
#     list_jobs=subprocess.run(f"sudo kubectl create secret docker-registry regcred  --docker-server=448877188565.dkr.ecr.us-east-2.amazonaws.com   --docker-username=AWS   --docker-password=$(aws ecr get-login-password --region us-east-2)",shell=True,capture_output=True)
#     print( list_jobs.stdout)
#     assert  list_jobs.returncode==0
 
 
# #sudo apt install git -y
# def test_install_git():
#     print(19)
#     list_jobs=subprocess.run(f"sudo apt install git -y",shell=True,capture_output=True)
#     print( list_jobs.stdout)
#     assert  list_jobs.returncode==0
 
# #git clone git@github.com:progress-platform-services/helm.git
# def test_clone_git():
#     print(19)
#     list_jobs=subprocess.run(f"yes \"y\" | git clone git@github.com:progress-platform-services/helm.git",shell=True,capture_output=True)
#     print( list_jobs.stdout)
#     assert  list_jobs.returncode==0


# #sed -i 's/tenant-1.dev-360.chef.co/ec2-3-94-190-118.compute-1.amazonaws.com/g' values.yaml
# def test_helm_deploy(get_env_variables, monkeypatch):
#     print(19)
#     monkeypatch.setenv("FQDN", get_env_variables["FQDN"])
#     FQDN = os.getenv("FQDN")
#     print(FQDN)
#     cmd="sed -i 's/tenant-1.dev-360.chef.co/"+FQDN+"/g' helm/chef-platform/values.yaml"
#     list_jobs=subprocess.run(cmd,shell=True,capture_output=True)
#     print( list_jobs.stdout)
#     assert  list_jobs.returncode==0
    
 
# # #sudo helm install chef-platform .
# def test_install_chef_platform():
#     print(19)
#     list_jobs=subprocess.run(f"sudo helm install chef-platform .",shell=True,capture_output=True, cwd="helm/chef-platform")
#     print( list_jobs.stdout)
#     assert  list_jobs.returncode==0


# def test_mailpit():
#     print(19)
#     command = "sudo nohup kubectl port-forward --namespace default service/mailpit --address 0.0.0.0 31100:8025 &"
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

#     # Wait for a moment to ensure the process starts
#     time.sleep(2)


# def test_reverse_proxy():
#     print(19)
#     command = "sudo nohup kubectl port-forward --namespace default service/nginx-reverse-proxy --address 0.0.0.0 31000:8080 &"
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

#     # Wait for a moment to ensure the process starts
#     time.sleep(2)


# def test_rabbit_mq():
#     print(19)
#     command = "sudo nohup kubectl port-forward --namespace default service/chef-platform-rabbitmq --address 0.0.0.0 31050:5672 &"
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

#     # Wait for a moment to ensure the process starts
#     time.sleep(2)