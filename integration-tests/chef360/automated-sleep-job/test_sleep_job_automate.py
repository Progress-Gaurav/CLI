import subprocess,json
import time
import logging
import os
import platform
import emoji
 
path=""
 
def test_load_license(get_env_variables):
    license_id=get_env_variables["LICENSE_ID"]
    cmd_to_load_license="chef-platform-auth-cli license-management license load-license --body '{\"licenseId\": \""+license_id+"\"}' --profile tenant-admin"
    load_license = subprocess.run(cmd_to_load_license, shell=True,capture_output=True)
    assert load_license.returncode == 0,"error \U0001F61E"
    load_license_result= json.loads(load_license.stdout)
    print(load_license_result)
 
def test_check_system_path():
     global path
     path=os.path.expanduser("~/")
     print(path)
     path+="CLI/integration-tests/chef360/automated-sleep-job/"
 
 
 
 
def test_register_skill_agent():
    # 15-register node management agent
    #               >create a json file(A)
    #               >create the skill agent(A)
    
    skill_agent_registration = subprocess.run(f"chef-node-management-cli management skill update-agent --body-file {path}register-agent-skill.json --profile node-manager", shell=True,capture_output=True)
    assert skill_agent_registration.returncode == 0
    skill_agent_result= json.loads(skill_agent_registration.stdout)
    # print(res)
    assert skill_agent_result["code"]== 200, "error \U0000274C"
 
 
# 16-defining all the skills(A) and verifying skills(A)
def test_install_skills():
    #courier-runner-skill
    skill1 = subprocess.run(f"chef-node-management-cli management skill create-skill --body-file {path}courier-runner-skill.json --profile node-manager",shell=True, capture_output=True)
    assert skill1.returncode == 0
    #gohai-skill
    skill2 = subprocess.run(f"chef-node-management-cli management skill create-skill --body-file {path}gohai-skill.json --profile node-manager",shell=True, capture_output=True)
    assert skill2.returncode == 0
    #shell-interpreter-skill
    skill3 = subprocess.run(f"chef-node-management-cli management skill create-skill --body-file {path}shell-interpreter-skill.json --profile node-manager",shell=True, capture_output=True)
    assert skill3.returncode == 0
    #restart-interpreter-skill
    skill4 = subprocess.run(f"chef-node-management-cli management skill create-skill --body-file {path}restart-interpreter-skill.json --profile node-manager",shell=True, capture_output=True)
    assert skill4.returncode == 0
    #chef-client-interpreter-skill
    skill5 = subprocess.run(f"chef-node-management-cli management skill create-skill --body-file {path}chef-client-interpreter-skill.json --profile node-manager",shell=True, capture_output=True)
    assert skill5.returncode == 0
    #inspec-interpreter-skill
    skill6 = subprocess.run(f"chef-node-management-cli management skill create-skill --body-file {path}inspec-interpreter-skill.json --profile node-manager",shell=True, capture_output=True)
    assert skill6.returncode == 0
 
def test_find_all_skills():
    skill_agent = subprocess.run(f"chef-node-management-cli management skill find-all-skills --profile node-manager",shell=True, capture_output=True)
    print("\n\n_________________\U0001F431 All the skills are successfully installed \U0001F431_________________________")
    assert skill_agent.returncode == 0, "error \U0000274C"
 
 
skillAssemblyID=""
def test_skill_assembly():
    # 17-defining the skill assembly(A) but changing the version (M/A){if the version are stable then its A otherwise M}. storing skillasssembly id(A)
    skill_assembly = subprocess.run(f"chef-node-management-cli management assembly create-assembly --body-file {path}skill-assembly.json --profile node-manager",shell=True, capture_output=True)
    assert skill_assembly.returncode == 0
    skill_assembly_result= json.loads(skill_assembly.stdout)
    print(skill_assembly_result)
    skillAssemblyID = skill_assembly_result["item"]["skillAssemblyId"]
    path_to_append_skillAssemblyID=path+"node-cohort.json"
    with open(path_to_append_skillAssemblyID, 'r') as file:
        config = json.load(file)
        config["skillAssemblyId"]=skillAssemblyID
    with open(path_to_append_skillAssemblyID, 'w') as file:
            json.dump(config, file, indent=4)
    print("\n\n_________________\U0001F604 The skillAssemblyID:"+skillAssemblyID+" \U0001F604_________________________")        
            
 
SETTING_ID=""
def test_node_override_settings():
    #18- create override settings(A)and storing the settingId(A)
    override_settings=subprocess.run(f"chef-node-management-cli management setting create-setting --body-file {path}node-override-setting.json --profile node-manager",shell=True, capture_output=True)
    assert override_settings.returncode == 0
    override_settings_result= json.loads(override_settings.stdout)
    print(override_settings_result)
    SETTING_ID= override_settings_result["item"]["settingId"]
    path_to_append_Setting_Id=path+"node-cohort.json"
    with open(path_to_append_Setting_Id, 'r') as file:
        config = json.load(file)
        config["settingId"] = SETTING_ID
    with open(path_to_append_Setting_Id, 'w') as file:
            json.dump(config, file, indent=4)
    print("\n\n_________________\U0001F604 The SETTING_ID="+SETTING_ID+" \U0001F604_________________________")        
 
 
COHORT_ID=""
def test_cohort(get_env_variables):
    #19-creating cohort(A) and storing the cohort id(A)
    pem_key=get_env_variables["PEM_KEY"]
    node_fqdn=get_env_variables["NODE_FQDN"]
    node_username=get_env_variables["NODE_USERNAME"]
    node_port=int(get_env_variables["NODE_PORT"])
    pem_key=pem_key.replace("\\n", "\n")
    cohort=subprocess.run(f"chef-node-management-cli management cohort create-cohort --body-file {path}node-cohort.json --profile node-manager",shell=True, capture_output=True)
    assert cohort.returncode==0
    cohort_result=json.loads(cohort.stdout)
    print(cohort_result)
    COHORT_ID=cohort_result["item"]["cohortId"]
    path_to_append_COHORT_ID=path+"enroll-linux.json"
    with open(path_to_append_COHORT_ID, 'r') as file:
        change = json.load(file)
        change["cohortId"]=COHORT_ID
        change["url"]=node_fqdn
        change["sshCredentials"]["username"]=node_username
        change["sshCredentials"]["key"]=pem_key
        change["sshCredentials"]["port"]=node_port
    with open(path_to_append_COHORT_ID, 'w') as file:
        json.dump(change, file, indent=4)
    print("\n\n________________\U0001F604 COHORT_ID="+COHORT_ID+" \U0001F604_________________________")    
    
 
            
NODE_ID=""
def test_Node_enroll():
    #20-node enrollment(M)
    enroll_node=subprocess.run(f"chef-node-management-cli enrollment enroll-node --body-file {path}enroll-linux.json --profile node-manager",shell=True,capture_output=True)
    assert enroll_node.returncode==0
    node_enrollment_result=json.loads(enroll_node.stdout)
    print(node_enrollment_result)
    NODE_ID=node_enrollment_result["item"]["nodeId"]
    path_to_append_node_id=path+"create-job-simple.json"
    with open(path_to_append_node_id, 'r') as file:
        job_config = json.load(file)
        job_config["target"]["groups"][0]["nodeIdentifiers"] = [NODE_ID]
    with open(path_to_append_node_id, 'w') as file:
        json.dump(job_config, file, indent=4)
    print("\n\n_________________\U0001F604NODE_ID="+NODE_ID+"\U0001F604_________________________")    
 
 
 
 
JOB_ID=""
def test_job():
    #21-creating a job(A)and getting jobId(A)
    job_run=subprocess.run(f"chef-courier-cli scheduler jobs add-job --body-file {path}create-job-simple.json --profile courier-operator",shell=True,capture_output=True)
    assert job_run.returncode==0
    job_run_result=json.loads(job_run.stdout)
    print(job_run_result)
    global JOB_ID
    JOB_ID=job_run_result["item"]["id"]
    print("\n\n_________________\U0001F604"+JOB_ID+"\U0001F604_________________")
    time.sleep(10)
 
  
 
def test_get_instance():
    job_instance=subprocess.run(f"chef-courier-cli state instance list-all --job-id {JOB_ID} --profile courier-operator",shell=True,capture_output=True)
    job_instance_result=json.loads(job_instance.stdout)
    print(job_instance_result)
    instance=job_instance_result["items"][0]['id']
    print(instance)
 
    list_instance_runs=subprocess.run(f"chef-courier-cli state instance list-instance-runs --instanceId {instance} --profile courier-operator ",shell=True,capture_output=True)
    runs_list=json.loads(list_instance_runs.stdout)
    runid=runs_list["items"][0]["runId"]
    print(runs_list)
    print(runid)
 
    lists_run_steps=subprocess.run(f"chef-courier-cli state run list-steps --runId {runid}  --profile courier-operator",shell=True,capture_output=True)
    print(lists_run_steps.stdout)
    run_steps=json.loads(lists_run_steps.stdout)
 
    print(run_steps)
    print("\U0000270C \U0001F389 \U0000270CYou have sucessfully ran the job Congratulations \U0000270C \U0001F389 \U0000270C ")
 
