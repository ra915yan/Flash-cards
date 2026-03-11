import requests
import json
import os
from Japanese_card import JishoWord
current_path = r'.\Japanese'
os.chdir(current_path)
URL = r"https://jisho.org/api/v1/search/words?keyword="

def getData(word:str):
    URL_word = URL + word
    response = requests.get(url=URL_word)
    response.raise_for_status()
    data = response.json()
    with open('buffer.txt', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=3, ensure_ascii=False)

getData('れ')

file = open('buffer.txt','r',encoding='utf-8')
data_json = json.load(file)
# print(data_json['data'][0])
for word in data_json['data']:
    obj = JishoWord.from_json(word)
    print("==============")
    print(obj.full_data)
    input("press Enter to go next")
    
    





