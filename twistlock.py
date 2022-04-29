import json

import requests


def call_twistlock_defenders():
    url = "https://twistlock-console.apps.openshift.aws.zenigma.com/api/v1"
    token= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoidHdpc3Rsb2NrLmFkbWluIiwicm9sZSI6ImFkbWluIiwiZ3JvdXBzIjpudWxsLCJyb2xlUGVybXMiOltbMjU1LDI1NSwyNTUsMjU1LDI1NSwxMjcsMV0sWzI1NSwyNTUsMjU1LDI1NSwyNTUsMTI3LDFdXSwic2Vzc2lvblRpbWVvdXRTZWMiOjM2MDAwLCJleHAiOjE2NTEyNjU5NTQsImlzcyI6InR3aXN0bG9jayJ9.dkaOSyGBnE1QyPsVZLoXWg8Dd4pCdqOiR-L82nOmDwo"

    url = url + "/defenders"
    response = requests.get(url=url, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}, verify=False)
    defenders = json.loads(response.text)

    hostnames =""
    for defender in defenders:
        hostnames = hostnames + defender["hostname"] + "/" + defender["cluster"] + ", "

    return {
        "message": "I'm happy to get Twistlock Defenders! Number of defenders are: "+ str(len(defenders)) + ". Here is hostname/cluster details: " +hostnames +" . I'm the security geek <3 "
    }