import subprocess,json
import time
import logging
import os
import platform

# def test_chef360_installation():

#     download_chef=subprocess.run(['curl','-f','https://appservice.chef360.chef.io/embedded/chef-360/stable','-H','"Authorization: 2eogd7vN1WG9aK79NRqKTfTWDUL"','-o','chef-360-stable.tgz'],capture_output=True)
#     assert download_chef.returncode==0

#     extract_chef=subprocess.run(['tar','-xvzf','chef-360-stable.tgz'],capture_output=True)
#     assert extract_chef.returncode==0
    
#     install_chef=subprocess.run(['sudo','./chef-360','install','--license license.yaml'],capture_output=True)
#     assert install_chef.returncode==0

#     #type the password
#     #Configure the Tenant Setup,Deploy


# NEW VARIABLES
# testrunnerOS: macos, linux, windows
# chef360CAFilename
# chef360devicename
# chef360profile
# chef360tenantDomain
# chef360tenantServiceURL
# def test_get_OS():
#     current_os = platform.system()
    
#     if current_os == "Linux":
#         return "linux"
    
#     elif current_os == "Darwin":
#         return "macos"
    
#     elif current_os == "Windows":
#         return "windows"
#     else:
#         return f"{current_os}"
def test_install_cli():
#   current_os=input("Enter the os\n1.Linux\n2.Mac OS\n3.Linux")
    current_os = platform.system()
    print(current_os)
    
    if current_os == "Linux":
         for_linux()
    elif current_os == "Darwin":
          for_MAC()
    elif current_os == "Windows":
        for_Windows()
    else:
        print(f"Unsupported OS: {current_os}")

def for_MAC():
    command1=subprocess.run("curl -sk http://ec2-54-242-50-112.compute-1.amazonaws.com:31000/platform/bundledtools/v1/static/install.sh | TOOL=\"chef-platform-auth-cli\" SERVER=\"http://ec2-54-242-50-112.compute-1.amazonaws.com:31000\" VERSION=\"latest\" bash -",shell=True)
    command2=subprocess.run("curl -sk http://ec2-54-242-50-112.compute-1.amazonaws.com:31000/platform/bundledtools/v1/static/install.sh | TOOL=\"chef-node-management-cli\" SERVER=\"http://ec2-54-242-50-112.compute-1.amazonaws.com:31000\" VERSION=\"latest\" bash -",shell=True)
    command3=subprocess.run("curl -sk http://ec2-54-242-50-112.compute-1.amazonaws.com:31000/platform/bundledtools/v1/static/install.sh | TOOL=\"chef-courier-cli\" SERVER=\"http://ec2-54-242-50-112.compute-1.amazonaws.com:31000\" VERSION=\"latest\" bash -",shell=True)

def for_linux():
    command1=subprocess.run("curl -sk http://ec2-54-242-50-112.compute-1.amazonaws.com:31000/platform/bundledtools/v1/static/install.sh | TOOL=\"chef-platform-auth-cli\" SERVER=\"http://ec2-54-242-50-112.compute-1.amazonaws.com:31000\" VERSION=\"latest\" bash -",shell=True)
    command2=subprocess.run("curl -sk http://ec2-54-242-50-112.compute-1.amazonaws.com:31000/platform/bundledtools/v1/static/install.sh | TOOL=\"chef-node-management-cli\" SERVER=\"http://ec2-54-242-50-112.compute-1.amazonaws.com:31000\" VERSION=\"latest\" bash -",shell=True)
    command3=subprocess.run("curl -sk http://ec2-54-242-50-112.compute-1.amazonaws.com:31000/platform/bundledtools/v1/static/install.sh | TOOL=\"chef-courier-cli\" SERVER=\"http://ec2-54-242-50-112.compute-1.amazonaws.com:31000\" VERSION=\"latest\" bash -",shell=True)

def for_Windows():
    command1=subprocess.run("$env:TOOL=\"chef-platform-auth-cli\"; $env:SERVER=\"http://ec2-54-242-50-112.compute-1.amazonaws.com:31000\"; Invoke-WebRequest -Uri \"http://ec2-54-242-50-112.compute-1.amazonaws.com:31000/platform/bundledtools/v1/static/install.ps1\" -UseBasicParsing | Invoke-Expression",shell=True)
    command2=subprocess.run("$env:TOOL=\"chef-node-management-cli\"; $env:SERVER=\"http://ec2-54-242-50-112.compute-1.amazonaws.com:31000\"; Invoke-WebRequest -Uri \"http://ec2-54-242-50-112.compute-1.amazonaws.com:31000/platform/bundledtools/v1/static/install.ps1\" -UseBasicParsing | Invoke-Expression",shell=True)
    command3=subprocess.run("$env:TOOL=\"chef-courier-cli\"; $env:SERVER=\"http://ec2-54-242-50-112.compute-1.amazonaws.com:31000\"; Invoke-WebRequest -Uri \"http://ec2-54-242-50-112.compute-1.amazonaws.com:31000/platform/bundledtools/v1/static/install.ps1\" -UseBasicParsing | Invoke-Expression",shell=True)

# testrunnerOS=
def test_install_cli():
    # dowmload_platform_auth_cli=subprocess.run([''],capture_output=True)
    # assert dowmload_platform_auth_cli.returncode==0

    # use the runner OS variable to get the right CLI
    # bin/chef360/linux/chef-courier-cli
    # strCommand = "bin/chef360/" + testrunnerOS + '/chef-platform-auth-cli'+"--help"
    # logging.info("Command line path is " + strCommand)
    
    checkstatus_platform_auth_cli=subprocess.run('chef-platform-auth-cli --help',capture_output=True,shell=True)
    assert checkstatus_platform_auth_cli.returncode==0


    # dowmload_chef_courier_cli=subprocess.run([''],capture_output=True)
    # # assert dowmload_chef_courier_cli.returncode==0

    checkstatus_chef_courier_cli=subprocess.run(['chef-courier-cli','--help'],capture_output=True)
    assert checkstatus_chef_courier_cli.returncode==0

    # dowmload_node_management_cli=subprocess.run([''],capture_output=True)
    # assert dowmload_node_management_cli.returncode==0

    checkstatus_node_management_cli=subprocess.run(['chef-node-management-cli','--help'],capture_output=True)
    assert checkstatus_node_management_cli.returncode==0

# def test_device_registration():
    
#     WORKSTATION_NAME=input("Enter the workstation Name")
#     PROFILE_NAME=input("Enter the Profile Name")
#     TENANT_URL=input("Enter the Tenant_URL")

#     device_reg=subprocess.run(['chef-platform-auth-cli','register-device','--device-name',WORKSTATION_NAME,'--profile-name',PROFILE_NAME,'--url',TENANT_URL,'--insecure'],capture_output=True)
#     assert device_reg.returncode==0

#     #Device registration returns a link,got to the link to authorise the device then press y in terminal after the deive is authenticated 
    
#     device_default_profile_reg=subprocess.run(['chef-platform-auth-cli','set-default-profile',PROFILE_NAME],capture_output=True)
#     assert device_default_profile_reg.returncode==0

def test_skill_agent():
    # 15-register node management agent
    #               >create a json file(A)
    #               >create the skill agent(A)

    skill_agent = subprocess.run(['chef-node-management-cli', 'management', 'skill', 'update-agent', '--body-file', 'integration-tests/chef360/automated-sleep-job/register-agent-skill.json'], capture_output=True)
    assert skill_agent.returncode == 0
    res= json.loads(skill_agent.stdout)
    # print(res)
    assert res["code"]== 200, "error"


    # 16-defining all the skills(A) and verifying skills(A)
def test_install_skills():
    #courier-runner-skill
    skill1 = subprocess.run(['chef-node-management-cli', 'management', 'skill', 'create-skill', '--body-file', 'integration-tests/chef360/automated-sleep-job/courier-runner-skill.json'], capture_output=True)
    assert skill1.returncode == 0
    #gohai-skill
    skill2 = subprocess.run(['chef-node-management-cli', 'management', 'skill', 'create-skill', '--body-file', 'integration-tests/chef360/automated-sleep-job/gohai-skill.json'], capture_output=True)
    assert skill2.returncode == 0
    #shell-interpreter-skill
    skill3 = subprocess.run(['chef-node-management-cli', 'management', 'skill', 'create-skill', '--body-file', 'integration-tests/chef360/automated-sleep-job/shell-interpreter-skill.json'], capture_output=True)
    assert skill3.returncode == 0
    #restart-interpreter-skill
    skill4 = subprocess.run(['chef-node-management-cli', 'management', 'skill', 'create-skill', '--body-file', 'integration-tests/chef360/automated-sleep-job/restart-interpreter-skill.json'], capture_output=True)
    assert skill4.returncode == 0
    #chef-client-interpreter-skill
    skill5 = subprocess.run(['chef-node-management-cli', 'management', 'skill', 'create-skill', '--body-file', 'integration-tests/chef360/automated-sleep-job/hef-client-interpreter-skill.json'], capture_output=True)
    assert skill5.returncode == 0
    #inspec-interpreter-skill
    
    skill6 = subprocess.run(['chef-node-management-cli', 'management', 'skill', 'create-skill', '--body-file', 'integration-tests/chef360/automated-sleep-job/inspec-interpreter-skill.json'], capture_output=True)
    assert skill6.returncode == 0

# def test_find_all_skills():
#     skill_agent = subprocess.run(['chef-node-management-cli', 'management', 'skill', 'find-all-skills'], capture_output=True,text=True)
#     assert skill_agent.returncode == 0
#     res= json.loads(skill_agent.stdout)
#     print(res)
#     assert res["code"]== 200, "error"

skillAssemblyID=""

def test_skill_assembly():
    # 17-defining the skill assembly(A) but changing the version (M/A){if the version are stable then its A otherwise M}. storing skillasssembly id(A)
    assembly = subprocess.run(['chef-node-management-cli', 'management', 'assembly', 'create-assembly', '--body-file','integration-tests/chef360/automated-sleep-job/skill-assembly.json'], capture_output=True)
    assert assembly.returncode == 0
    res1= json.loads(assembly.stdout)
    print(res1)
    skillAssemblyID = res1["item"]["skillAssemblyId"]
    with open('integration-tests/chef360/automated-sleep-job/node-cohort.json', 'r') as file:
        config = json.load(file)
        config["skillAssemblyId"]=skillAssemblyID
    with open('integration-tests/chef360/automated-sleep-job/node-cohort.json', 'w') as file:
            json.dump(config, file, indent=4)

SETTING_ID=""
def test_node_override_settings():
    #18- create override settings(A)and storing the settingId(A)
    override=subprocess.run(['chef-node-management-cli','management','setting','create-setting','--body-file','integration-tests/chef360/automated-sleep-job/node-override-setting.json'],capture_output=True)
    assert override.returncode == 0
    res2= json.loads(override.stdout)
    print(res2)
    SETTING_ID= res2["item"]["settingId"]
    with open('integration-tests/chef360/automated-sleep-job/node-cohort.json', 'r') as file:
        config = json.load(file)
        config["settingId"] = SETTING_ID
    with open('integration-tests/chef360/automated-sleep-job/node-cohort.json', 'w') as file:
            json.dump(config, file, indent=4)


COHORT_ID=""
def test_cohort():
    #19-creating cohort(A) and storing the cohort id(A)
    cohort=subprocess.run(['chef-node-management-cli','management','cohort','create-cohort','--body-file','integration-tests/chef360/automated-sleep-job/node-cohort.json'],capture_output=True)
    assert cohort.returncode==0
    res3=json.loads(cohort.stdout)
    print(res3)
    COHORT_ID=res3["item"]["cohortId"]
    with open('integration-tests/chef360/automated-sleep-job/enroll-linux.json', 'r') as file:
        change = json.load(file)
        change["cohortId"]=COHORT_ID
    with open('integration-tests/chef360/automated-sleep-job/enroll-linux.json', 'w') as file:
        json.dump(change, file, indent=4)
    


def test_get_key():
    path="/home/ubuntu/ImportantFiles"
    keyname="chef-360-demo.pem"
    command="awk \'NF {sub(/\r/, \"\"); printf \"%s\\n\",$0;}\' "+keyname

    keyextract=subprocess.run(command,shell=True,cwd=path,capture_output=True)
    key=keyextract.stdout
    regular_string = key.decode('utf-8')
    print(key)
    # key1=key[0]
    # print(keyextract.stdout)
    # print(key1)

    # with open('/Users/hbiju/Desktop/sample-enrollfile.json', 'r') as file:
    #         config = json.load(file)
    #         config["sshCredentials"]["key"]=regular_string
    # with open('/Users/hbiju/Desktop/sample-enrollfile.json', 'w') as file:
    #         json.dump(config, file, indent=4)
            
NODE_ID=""
def test_Node_enroll():
    #20-node enrollment(M)
    enroll=subprocess.run(['chef-node-management-cli','enrollment','enroll-node','--body-file','integration-tests/chef360/automated-sleep-job/enroll-linux.json'],capture_output=True)
    assert enroll.returncode==0
    res4=json.loads(enroll.stdout)
    print(res4)
    NODE_ID=res4["item"]["nodeId"]
    with open('integration-tests/chef360/automated-sleep-job/create-job-simple.json', 'r') as file:
        job_config = json.load(file)
        job_config["target"]["groups"][0]["nodeIdentifiers"] = [NODE_ID]
    with open('integration-tests/chef360/automated-sleep-job/create-job-simple.json', 'w') as file:
        json.dump(job_config, file, indent=4)



JOB_ID=""
def test_job():
    #21-creating a job(A)and getting jobId(A)
    job_run=subprocess.run(['chef-courier-cli','scheduler','jobs','add-job','--body-file','integration-tests/chef360/automated-sleep-job/create-job-simple.json'],capture_output=True)
    assert job_run.returncode==0
    res5=json.loads(job_run.stdout)
    print(res5)
    global JOB_ID
    JOB_ID=res5["item"]["id"]
    print(JOB_ID)
    time.sleep(30)

  

def test_get_instance():
    result1=subprocess.run(['chef-courier-cli','state','instance','list-all','--job-id',JOB_ID],capture_output=True,text=True)
    res6=json.loads(result1.stdout)
    print(res6)
    instance=res6["items"][0]['id']
    print(instance)

    result2=subprocess.run(['chef-courier-cli','state','instance','list-instance-runs','--instanceId',instance],capture_output=True,text=True)
    res7=json.loads(result2.stdout)
    runid=res7["items"][0]["runId"]
    print(res7)
    print(runid)

    result3=subprocess.run(['chef-courier-cli','state','run','list-steps','--runId',runid],capture_output=True,text=True)
    print(result3.stdout)
    res8=json.loads(result3.stdout)

    print(res8)
    # final=any(item["status"]=="success" for item in res8["items"])
    # assert final,"Job instance run failed!"
