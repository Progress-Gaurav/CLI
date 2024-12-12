import subprocess,json
import time
import logging
import os
import platform


def test_skill_agent():
    # 15-register node management agent
    #               >create a json file(A)
    #               >create the skill agent(A)
 
    skill_agent = subprocess.run(f"chef-node-management-cli management skill update-agent --body-file /home/ubuntu/CLI/integration-tests/chef360/automated-sleep-job/register-agent-skill.json --profile node-manager", shell=True,capture_output=True)
    assert skill_agent.returncode == 0
    res= json.loads(skill_agent.stdout)
    # print(res)
    assert res["code"]== 200, "error"
 
 
    # 16-defining all the skills(A) and verifying skills(A)
def test_install_skills():
    #courier-runner-skill
    skill1 = subprocess.run(f"chef-node-management-cli management skill create-skill --body-file /home/ubuntu/CLI/integration-tests/chef360/automated-sleep-job/courier-runner-skill.json --profile node-manager",shell=True, capture_output=True)
    assert skill1.returncode == 0
    #gohai-skill
    skill2 = subprocess.run(f"chef-node-management-cli management skill create-skill --body-file /home/ubuntu/CLI/integration-tests/chef360/automated-sleep-job/gohai-skill.json --profile node-manager",shell=True, capture_output=True)
    assert skill2.returncode == 0
    #shell-interpreter-skill
    skill3 = subprocess.run(f"chef-node-management-cli management skill create-skill --body-file /home/ubuntu/CLI/integration-tests/chef360/automated-sleep-job/shell-interpreter-skill.json --profile node-manager",shell=True, capture_output=True)
    assert skill3.returncode == 0
    #restart-interpreter-skill
    skill4 = subprocess.run(f"chef-node-management-cli management skill create-skill --body-file /home/ubuntu/CLI/integration-tests/chef360/automated-sleep-job/restart-interpreter-skill.json --profile node-manager",shell=True, capture_output=True)
    assert skill4.returncode == 0
    #chef-client-interpreter-skill
    skill5 = subprocess.run(f"chef-node-management-cli management skill create-skill --body-file /home/ubuntu/CLI/integration-tests/chef360/automated-sleep-job/chef-client-interpreter-skill.json --profile node-manager",shell=True, capture_output=True)
    assert skill5.returncode == 0
    #inspec-interpreter-skill
    skill6 = subprocess.run(f"chef-node-management-cli management skill create-skill --body-file /home/ubuntu/CLI/integration-tests/chef360/automated-sleep-job/inspec-interpreter-skill.json --profile node-manager",shell=True, capture_output=True)
    assert skill6.returncode == 0
 
def test_find_all_skills():
    skill_agent = subprocess.run(f"chef-node-management-cli management skill find-all-skills --profile node-manager",shell=True, capture_output=True)
    print("\n\n_________________All the skills are successfully installed_________________________")
    assert skill_agent.returncode == 0
 
skillAssemblyID=""
 
def test_skill_assembly():
    # 17-defining the skill assembly(A) but changing the version (M/A){if the version are stable then its A otherwise M}. storing skillasssembly id(A)
    assembly = subprocess.run(f"chef-node-management-cli management assembly create-assembly --body-file /home/ubuntu/CLI/integration-tests/chef360/automated-sleep-job/skill-assembly.json --profile node-manager",shell=True, capture_output=True)
    assert assembly.returncode == 0
    res1= json.loads(assembly.stdout)
    print(res1)
    skillAssemblyID = res1["item"]["skillAssemblyId"]
    with open('/home/ubuntu/CLI/integration-tests/chef360/automated-sleep-job/node-cohort.json', 'r') as file:
        config = json.load(file)
        config["skillAssemblyId"]=skillAssemblyID
    with open('/home/ubuntu/CLI/integration-tests/chef360/automated-sleep-job/node-cohort.json', 'w') as file:
            json.dump(config, file, indent=4)
    print("\n\n_________________The skillAssemblyID:"+skillAssemblyID+"_________________________")        
            
 
SETTING_ID=""
def test_node_override_settings():
    #18- create override settings(A)and storing the settingId(A)
    override=subprocess.run(f"chef-node-management-cli management setting create-setting --body-file /home/ubuntu/CLI/integration-tests/chef360/automated-sleep-job/node-override-setting.json --profile node-manager",shell=True, capture_output=True)
    assert override.returncode == 0
    res2= json.loads(override.stdout)
    print(res2)
    SETTING_ID= res2["item"]["settingId"]
    with open('/home/ubuntu/CLI/integration-tests/chef360/automated-sleep-job/node-cohort.json', 'r') as file:
        config = json.load(file)
        config["settingId"] = SETTING_ID
    with open('/home/ubuntu/CLI/integration-tests/chef360/automated-sleep-job/node-cohort.json', 'w') as file:
            json.dump(config, file, indent=4)
    print("\n\n_________________The SETTING_ID="+SETTING_ID+"_________________________")        
 
 
COHORT_ID=""
def test_cohort():
    #19-creating cohort(A) and storing the cohort id(A)
    cohort=subprocess.run(f"chef-node-management-cli management cohort create-cohort --body-file /home/ubuntu/CLI/integration-tests/chef360/automated-sleep-job/node-cohort.json --profile node-manager",shell=True, capture_output=True)
    assert cohort.returncode==0
    res3=json.loads(cohort.stdout)
    print(res3)
    COHORT_ID=res3["item"]["cohortId"]
    with open('/home/ubuntu/CLI/integration-tests/chef360/automated-sleep-job/enroll-linux.json', 'r') as file:
        change = json.load(file)
        change["cohortId"]=COHORT_ID
    with open('/home/ubuntu/CLI/integration-tests/chef360/automated-sleep-job/enroll-linux.json', 'w') as file:
        json.dump(change, file, indent=4)
    
 
 
def test_get_key():
    path="/home/ubuntu/ImportantFiles"
    keyname="chef-360-demo.pem"
    command="awk \'NF {sub(/\r/, \"\"); printf \"%s\\n\",$0;}\' "+keyname
 
    keyextract=subprocess.run(command,shell=True,cwd=path,capture_output=True)
    key=keyextract.stdout
    regular_string = key.decode('utf-8')
    print(key)
    key1=key[0]
    print(keyextract.stdout)
    print(key1)
 
    with open('/Users/hbiju/Desktop/sample-enrollfile.json', 'r') as file:
            config = json.load(file)
            config["sshCredentials"]["key"]=regular_string
    with open('/Users/hbiju/Desktop/sample-enrollfile.json', 'w') as file:
            json.dump(config, file, indent=4)
            
NODE_ID=""
def test_Node_enroll():
    #20-node enrollment(M)
    enroll=subprocess.run(f"chef-node-management-cli enrollment enroll-node --body-file /home/ubuntu/CLI/integration-tests/chef360/automated-sleep-job/enroll-linux.json --profile node-manager",shell=True,capture_output=True)
    assert enroll.returncode==0
    res4=json.loads(enroll.stdout)
    print(res4)
    NODE_ID=res4["item"]["nodeId"]
    with open('/home/ubuntu/CLI/integration-tests/chef360/automated-sleep-job/create-job-simple.json', 'r') as file:
        job_config = json.load(file)
        job_config["target"]["groups"][0]["nodeIdentifiers"] = [NODE_ID]
    with open('/home/ubuntu/CLI/integration-tests/chef360/automated-sleep-job/create-job-simple.json', 'w') as file:
        json.dump(job_config, file, indent=4)
 
 
 
JOB_ID=""
def test_job():
    #21-creating a job(A)and getting jobId(A)
    job_run=subprocess.run(f"chef-courier-cli scheduler jobs add-job --body-file /home/ubuntu/CLI/integration-tests/chef360/automated-sleep-job/create-job-simple.json --profile courier-operator",shell=True,capture_output=True)
    assert job_run.returncode==0
    res5=json.loads(job_run.stdout)
    print(res5)
    global JOB_ID
    JOB_ID=res5["item"]["id"]
    print(JOB_ID)
    time.sleep(30)
 
  
 
# def test_get_instance():
#     result1=subprocess.run(['chef-courier-cli','state','instance','list-all','--job-id',JOB_ID],capture_output=True,text=True)
#     res6=json.loads(result1.stdout)
#     print(res6)
#     instance=res6["items"][0]['id']
#     print(instance)

#     result2=subprocess.run(['chef-courier-cli','state','instance','list-instance-runs','--instanceId',instance],capture_output=True,text=True)
#     res7=json.loads(result2.stdout)
#     runid=res7["items"][0]["runId"]
#     print(res7)
#     print(runid)
 
#     result3=subprocess.run(['chef-courier-cli','state','run','list-steps','--runId',runid],capture_output=True,text=True)
#     print(result3.stdout)
#     res8=json.loads(result3.stdout)
 
#     print(res8)
#     # final=any(item["status"]=="success" for item in res8["items"])
#     # assert final,"Job instance run failed!"
