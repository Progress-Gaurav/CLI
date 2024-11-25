# George's upload to Qmetry script - replaced by Irfan's code

API_KEY=

URL=https://qtmcloud.qmetry.com/rest/api/automation/importresult

payload="{ \"format\":\"junit\", \"testCycleToReuse\":\"CHEF-TR-27\", \"matchTestSteps\": false }"
resp=$(curl -s -H "apiKey: $API_KEY" -H "Content-Type: application/json" --data "$payload" $URL)
upload=$(echo $resp | jq -r .url)
trackingId=$(echo $resp | jq -r .trackingId)
results=$(curl -X PUT -H "Content-Type: multipart/form-data" --upload-file /home/ec2-user/regression/junit.xml "$upload")