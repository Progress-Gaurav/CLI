import subprocess,json
import time
 
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
 
# If on Ubuntu:
#sudo apt update -y
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
# def test_download_binary():
#         print(8)
#         list_jobs=subprocess.run(f"curl -LO \"https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl\"",shell=True,capture_output=True)
#         time.sleep(10)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
 

# # sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
# def test_install_kubectl():
#         print(9)
#         list_jobs=subprocess.run(f"sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl",shell=True,capture_output=True)
#         print( list_jobs.stdout)
#         assert  list_jobs.returncode==0
 

# # chmod +x kubectl
# def test_install_kubectl():
#         print(10)
#         list_jobs=subprocess.run(f"chmod +x kubectl",shell=True,capture_output=True)
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
def test_minikube_status():
        print(18)
        list_jobs=subprocess.run(f"sudo minikube status",shell=True,capture_output=True)
        print( list_jobs.stdout)
        assert  list_jobs.returncode==0
        
       
 