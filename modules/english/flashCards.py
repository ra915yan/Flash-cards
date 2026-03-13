from dataclasses import dataclass , field
from typing import List, Any



@dataclass
class FlashCards:
    id:str = ""
    word:str = ""
    part_Of_speech:str = ""
    definition:List = field(default_factory=list)
    Phonetic:str = ""
    stems:List = field(default_factory=list)
    sentences:List = field(default_factory=list)
    


def parseJson(data, card: FlashCards = None) -> FlashCards:
    
    if card is None:
        card = FlashCards()
        
    if isinstance(data,list):
        for item in data:
            parseJson(item,card)
    
    if isinstance(data,dict):
        for key ,value in data.items():
        
            match key:
                case "hw":
                    card.word = value
                    
                case 'ipa':
                    card.Phonetic = value
                
                case "stems":
                    _add_items(card.stems, value)
                    
                case "shortdef":
                    _add_items(card.definition,value)
                    
                case "t" | "text":
                    card.sentences.append(value)
                    
            if isinstance(value , (list,dict)):
                parseJson(value,card)
            
    return card
        
        
def _add_items(target_list: list , value: Any):
    
    if isinstance(value,list):
        target_list.extend([str(i) for i in value])
    else:
        target_list.append(str(value))
    
            



# word print(data[0]['hwi']['hw'])
# Phonetic print(data[0]['hwi']['prs'][0]['ipa'])
# stems data[0]["meta"]["stems"]
# meaning print(data[0]['shortdef'][0])