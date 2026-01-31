import json 


def info(data):
    
    if isinstance(data, list):
        print(f"List: {len(data)}")
    
    elif isinstance(data,dict):
        print(f"Dict: keys({[key for key in data]})")
    
    else:
        print(type(data))


file = open("test.txt",'r')

data = file.read()

data = json.loads(data)

word = 'led'
words = [word in word for data if word['meta']['id'].split(":")[0] == word]
    
    
