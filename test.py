import json

def print_json_tree(data,level = 0):
    indent  ="  " * level
    if isinstance(data,dict):
        for key , value in data.items():
            print(f"{indent} Key: {key}")
            print_json_tree(value, level + 1)
            
    elif isinstance(data,list):
        for index, item in enumerate(data):
            print(f"{indent}[item{index}]")
            print_json_tree(item , level + 1)
            
    else:
        print(f"{indent}Value:{data}")     
    


file = open('test.txt','r')
json_data =file.read()

data = json.loads(json_data)
print_json_tree(data)

file.close()