import requests as req
import json
URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"
response = req.get(URL + "Hello")

file = open("test.txt",'w')
if response.status_code == 200:
    data = response.json()
    file.write(json.dumps(data,indent=4))