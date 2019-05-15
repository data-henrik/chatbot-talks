ibmcloud fn action create slackdemo/fetchSystemInfo systemInfo.js  --kind nodejs:8
ibmcloud fn service bind dashDB slackdemo/fetchSystemInfo --instance eventDB

#ibmcloud fn action create slackdemo/queryTable queryTable.py  --kind python-jessie:3
#ibmcloud fn service bind dashDB slackdemo/queryTable --instance eventDB
