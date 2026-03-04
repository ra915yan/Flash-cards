import requests as req
import json
import logging
# "https://api.dictionaryapi.dev/api/v2/entries/en/"
# URL = "https://www.dictionaryapi.com/api/v3/references/learners/json/apple?key=your-api-key"
API_KEY = "77352c50-c1e4-4e51-b137-f37ae0a39891"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("dictionary_access.log"),
        logging.StreamHandler()
    ]
)
    
class DictionaryAPI:
    def __init__(self, word:str, key = API_KEY):
        self.key = key
        self.word = word
        self.URL = f"https://www.dictionaryapi.com/api/v3/references/learners/json/{self.word}?key={self.key}"
        
        
    def fetch_data(self):
        
        logging.info(f"Fetching Data for word: '{self.word}'......")
        
        
        try:
            response = req.get(self.URL)
            data = response.json()
            logging.info("Successfully done")
            return data
        except req.exceptions.RequestException as e:
            logging.info(f"Failed to fetch for '{self.word}'")
            return None
        except json.JSONDecodeError:
            logging.error(f"JSON Parsing falied fro '{self.word}'")
            
            
    def run(self):
        
        data_word = self.fetch_data()
        with open("buffer.txt",'w',encoding="utf-8") as file:
            json.dump(data_word, file, indent=4, ensure_ascii=False)

obj = DictionaryAPI("yawn")
obj.run()
            
        
#compartmentalization contemporary
        
    
