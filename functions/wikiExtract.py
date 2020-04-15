# (C) 2020 IBM Corporation / Henrik Loeser
#
# IBM Cloud Functions / OpenWhisk action to obtain extract from
# Wikipedia page

import json,sys,os
import requests

def getWikipedia(searchterm, lang):
    url     = "https://{}.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles={}&explaintext&redirects=1&indexpageids".format(lang,searchterm)
    headers = { "Content-Type" : "application/json" }
    response  = requests.get( url, headers=headers)
    if(response.status_code >= 400):
        print("status_code: {} Message: {}".format(response.status_code, response.text))
        raise RuntimeError(response.text)

    jsonResponse = response.json()
    pageID=jsonResponse["query"]["pageids"][0]
    return jsonResponse["query"]["pages"][pageID]["extract"]

def main(args):

    res=getWikipedia(args.get("searchterm"),args.get("lang"))
    return { **args, "info":res}

if __name__ == "__main__":
    val=main(json.loads(sys.argv[1]))
    print(val)
