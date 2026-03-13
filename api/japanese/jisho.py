import requests
import json
import os
from pathlib import Path
from modules.japanese.Japanese_card import JishoWord
from database.DBM import AnkiDatabase
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("dictionary_access.log"),
        logging.StreamHandler()
    ]
)

URL     = r"https://jisho.org/api/v1/search/words?keyword="
path    = r"data\words"


def _fetch_word_from_jisho(word:str):
    URL_word = URL + word
    response = requests.get(url=URL_word)
    response.raise_for_status()
    return response.json()
    
    
    
def get_word(word:str):
    logging.info(f"Retrieving the word: {word}")
    full_path = os.path.join(path,word,".json")
    
    if AnkiDatabase.exists(full_path):
        logging.info(f"the word: {word} exits in the database")

    else:
        logging.info(f"request for the word: {word}")
        data_json = _fetch_word_from_jisho(word)
        obj_Jisho = JishoWord.from_json(data_json)
        AnkiDatabase.add_word(obj_Jisho)
        logging.info("Added to database")



get_word("真っ黒")
    





