import requests as req
import json
# "https://api.dictionaryapi.dev/api/v2/entries/en/"
# URL = "https://www.dictionaryapi.com/api/v3/references/learners/json/apple?key=your-api-key"
API_KEY = "77352c50-c1e4-4e51-b137-f37ae0a39891"
word = "led"
    
    
def fetch_word_data(word:str):
    
    file = open("test.txt",'w')
    URL = f"https://www.dictionaryapi.com/api/v3/references/learners/json/{word}?key={API_KEY}"
    
    
    response = req.get(URL)
    
    # DEBUGGING STEPS:
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: '{response.text}'") # This will show you exactly what failed
    
    if response.status_code == 200:
        try:
            data = response.json()
            file.write(json.dumps(data,indent=4))
            # ... rest of your code
        except Exception as e:
            print(f"JSON Parsing failed! The server sent: {response.text}")
        
    
fetch_word_data(word)