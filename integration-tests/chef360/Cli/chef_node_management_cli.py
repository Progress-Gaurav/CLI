import subprocess,json
import time


def test_bulk_enroll():
    enroll_bulk=subprocess.run(f"chef-node-management-cli enrollment bulk-enroll",shell=True,capture_output=True)
    print( enroll_bulk.stdout)
    assert  enroll_bulk.returncode==0

def test_node_enroll():
    enroll_node=subprocess.run(f"chef-node-management-cli enrollment enroll-node",shell=True,capture_output=True)
    print(enroll_node.stdout)
    assert  enroll_node.returncode==0

def test_default_profile():
    def_device=subprocess.run(f"chef-node-management-cli get-default-profile",shell=True,capture_output=True)
    print(def_device.stdout)
    assert def_device.returncode==0

def test_profiles():
    profile_names=subprocess.run(f"chef-node-management-cli list-profile-names",shell=True,capture_output=True)
    print(profile_names.stdout)
    assert profile_names.returncode==0




# Assembly 
def test_assembly():
    asssembly=subprocess.run(f"chef-node-management-cli management assembly",shell=True,capture_output=True)
    print(asssembly.stdout)
    assert asssembly.returncode==0

def test_create_assembly():
    asssembly_creation=subprocess.run(f"chef-node-management-cli management assembly create-assembly [flag]",shell=True,capture_output=True)
    print(asssembly_creation.stdout)
    assert asssembly_creation.returncode==0

def test_delete_assembly():
    asssembly_deletion=subprocess.run(f"chef-node-management-cli management assembly delete-assembly [flags]",shell=True,capture_output=True)
    print(asssembly_deletion.stdout)
    assert asssembly_deletion.returncode==0

def test_find_all_assembly():
    asssembly_find_all=subprocess.run(f"chef-node-management-cli management assembly find-all-assemblies [flags]",shell=True,capture_output=True)
    print(asssembly_find_all.stdout)
    assert asssembly_find_all.returncode==0

def test_find_one_assembly():
    asssembly_find_one=subprocess.run(f"chef-node-management-cli management assembly find-one-assemblies [flags]",shell=True,capture_output=True)
    print(asssembly_find_one.stdout)
    assert asssembly_find_one.returncode==0

def test_update_assembly():
    asssembly_update=subprocess.run(f"chef-node-management-cli management assembly update-assembly [flags]",shell=True,capture_output=True)
    print(asssembly_update.stdout)
    assert asssembly_update.returncode==0

def test_update_assembly():
    asssembly_update=subprocess.run(f"chef-node-management-cli management assembly update-assembly [flags]",shell=True,capture_output=True)
    print(asssembly_update.stdout)
    assert asssembly_update.returncode==0




# Cohort
def test_cohort():
    cohort=subprocess.run(f"chef-node-management-cli management cohort",shell=True,capture_output=True)
    print(cohort.stdout)
    assert cohort.returncode==0

def test_cohort_assign_setting():
    assign_setting=subprocess.run(f"chef-node-management-cli management cohort assign-setting [flags]",shell=True,capture_output=True)
    print(assign_setting.stdout)
    assert assign_setting.returncode==0

def test_assign_skillassembly():
    skillassembly_assign=subprocess.run(f"chef-node-management-cli management cohort assign-skillAssembly [flags]",shell=True,capture_output=True)
    print(skillassembly_assign.stdout)
    assert skillassembly_assign.returncode==0

def test_create_cohort():
    cohort_creation=subprocess.run(f"chef-node-management-cli management cohort create-cohort [flags]",shell=True,capture_output=True)
    print(cohort_creation.stdout)
    assert cohort_creation.returncode==0

def test_delete_cohort():
    cohort_deletion=subprocess.run(f"chef-node-management-cli management cohort delete-cohort [flags]",shell=True,capture_output=True)
    print(cohort_deletion.stdout)
    assert cohort_deletion.returncode==0

def test_find_all_cohort():
    cohort_find_all=subprocess.run(f"chef-node-management-cli management cohort find-all-cohort [flags]",shell=True,capture_output=True)
    print(cohort_find_all.stdout)
    assert cohort_find_all.returncode==0


def test_find_one_cohort():
    cohort_find_one=subprocess.run(f"chef-node-management-cli management cohort find-one-cohort [flags]",shell=True,capture_output=True)
    print(cohort_find_one.stdout)
    assert cohort_find_one.returncode==0




#filter
def test_filter():
    filter=subprocess.run(f"chef-node-management-cli management filter",shell=True,capture_output=True)
    print(filter.stdout)
    assert filter.returncode==0

def test_create_filter():
    filter_create=subprocess.run(f"chef-node-management-cli management filter create-filter [flags]",shell=True,capture_output=True)
    print(filter_create.stdout)
    assert filter_create.returncode==0

def test_delete_filter():
    filter_delete=subprocess.run(f"chef-node-management-cli management filter delete-filter [flags]",shell=True,capture_output=True)
    print(filter_delete.stdout)
    assert filter_delete.returncode==0

def test_find_all_filter():
    filter_find_all=subprocess.run(f"chef-node-management-cli management filter find-all-filter [flags]",shell=True,capture_output=True)
    print(filter_find_all.stdout)
    assert filter_find_all.returncode==0

def test_find_one_filter():
    filter_find_one=subprocess.run(f"chef-node-management-cli management filter find-one-filter [flags]",shell=True,capture_output=True)
    print(filter_find_one.stdout)
    assert filter_find_one.returncode==0

def test_run_adhocfilter():
    filter_run_adhoc=subprocess.run(f"chef-node-management-cli management filter run-adhocFilter [flags]",shell=True,capture_output=True)
    print(filter_run_adhoc.stdout)
    assert filter_run_adhoc.returncode==0

def test_run_savedFilter():
    filter_run_saved=subprocess.run(f"chef-node-management-cli management filter run-savedFilter [flags]",shell=True,capture_output=True)
    print(filter_run_saved.stdout)
    assert filter_run_saved.returncode==0

def test_update_Filter():
    filter_update=subprocess.run(f"chef-node-management-cli management filter update-filter [flags]",shell=True,capture_output=True)
    print(filter_update.stdout)
    assert filter_update.returncode==0




#list
def test_list():
    lists=subprocess.run(f"chef-node-management-cli management list",shell=True,capture_output=True)
    print(lists.stdout)
    assert lists.returncode==0

def test_add_nodes_list():
    lists_add_nodes=subprocess.run(f"chef-node-management-cli management list add-nodes [flags]",shell=True,capture_output=True)
    print(lists_add_nodes.stdout)
    assert lists_add_nodes.returncode==0

def test_create_list():
    lists_creation=subprocess.run(f"chef-node-management-cli management list create-list [flags]",shell=True,capture_output=True)
    print(lists_creation.stdout)
    assert lists_creation.returncode==0

def test_delete_list():
    lists_deletion=subprocess.run(f"chef-node-management-cli management list delete-list [flags]",shell=True,capture_output=True)
    print(lists_deletion.stdout)
    assert lists_deletion.returncode==0