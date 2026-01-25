from dataclasses import dataclass
from typing import List

@dataclass
class flashCard:
    word:       str
    Phonetic:   str
    definition: str
    sentences:  List
    
    