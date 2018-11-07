#bx wsk action create slackdemo/fetchSystemInfo systemInfo.js  --kind nodejs:8
#bx wsk service bind dashDB slackdemo/fetchSystemInfo --instance eventDB

bx wsk action create slackdemo/queryTable queryTable.py  --kind python-jessie:3
bx wsk service bind dashDB slackdemo/queryTable --instance eventDB
