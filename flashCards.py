from dataclasses import dataclass , field
from typing import List



@dataclass
class FlashCards:
    word:str
    definition:str
    Phonetic:str
    sentences:List






    # word print(data[0]['hwi']['hw'])
# Phonetic print(data[0]['hwi']['prs'][0]['ipa'])
# stems data[0]["meta"]["stems"]
# meaning print(data[0]['shortdef'][0])