import json


    


file = open('test.txt','r')
json_data =file.read()

data = json.loads(json_data)
print(data[0].keys())
for dic in data[0]:
    if dic == 'def':
        continue
    
    # print(json.dumps(data[0][dic],indent=3))

# word print(data[0]['hwi']['hw'])
# Phonetic print(data[0]['hwi']['prs'][0]['ipa'])
# stems data[0]["meta"]["stems"]
# meaning print(data[0]['shortdef'][0])


values = [d.get('if').replace('*','') for d in data[0]['ins'] if isinstance(d,dict)]
print(values)



file.close()