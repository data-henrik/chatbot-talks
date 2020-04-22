# (C) 2020 IBM Corporation / Henrik Loeser
#
# IBM Cloud Functions / OpenWhisk action to obtain extract from
# Wikipedia page. See this link for details on parameters:
# https://www.mediawiki.org/w/api.php?action=help&modules=query%2Bextracts

import json,sys,os
import requests
import urllib.parse

def getWikipedia(searchterm, lang):
    # encode the searchterm
    st=urllib.parse.quote(searchterm)
    url     = "https://{}.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&titles={}&explaintext&exintro&redirects=1&indexpageids".format(lang,st)
    headers = { "Content-Type" : "application/json" }
    response  = requests.get( url, headers=headers)
    if(response.status_code >= 400):
        print("status_code: {} Message: {}".format(response.status_code, response.text))
        raise RuntimeError(response.text)

    jsonResponse = response.json()
    # we need the page ID to get to the actual extract
    pageID=jsonResponse["query"]["pageids"][0]
    return jsonResponse["query"]["pages"][pageID]["extract"]

def main(args):
    # call the function and return its result
    res=getWikipedia(args.get("searchterm"),args.get("lang"))
    return {"info":res}

if __name__ == "__main__":
    val=main(json.loads(sys.argv[1]))
    print(val)
