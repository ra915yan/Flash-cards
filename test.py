import json
import re


def info(data):

    if isinstance(data,list):
        print("List")
        print(f"Length: {len(data)}\n")
        print(json.dumps(data,indent=3))

    elif isinstance(data,dict):
        print("keys")
        print(data.keys())
        print(json.dumps(data,indent=3))

    else:
        print(data)


def getText(data , l:list = []):

    pattern = r'\{.*?\}|\[.*?\]'

    if isinstance(data,dict):
        for key,value in data.items():

            if key in ("t","text"):
                value = re.sub(pattern, '', value).strip()
                yield value

            else: yield from getText(value)

    elif isinstance(data,list):
        for item in data:
            yield from getText(item)




    


file = open('test.txt','r')
json_data =file.read()

data = json.loads(json_data)
# print(data[0].keys())
for dic in data[0]:
    if dic == 'def':
        continue
    
    # print(json.dumps(data[0][dic],indent=3))

 

# values = [d.get('if').replace('*','') for d in data[0]['ins'] if isinstance(d,dict)]
# print(values)




# data[0]['def'][0]['sseq']
# data[0]['def'][0]['sseq'][0][0][1]['dt']
# info(data[0]['def'][0]['sseq'][0][0][1]['dt'][0][1])


# for elem in data[0]['def'][0]['sseq']:

#     for elem2 in elem[0]:
#         info(elem2)

l = list(getText(data))

for sentence in l:
    print(f"{sentence}\n")






file.close()