from dataclasses import dataclass
import json
from modules.japanese.srtFile import srtFile
import re
import fugashi
from patterns.JP import JP_PATTERN
import os
# A. Decouple File I/O
# Don't hardcode file reading inside the class. Pass the content in, or use a context manager.

# Update: Move the SRT parsing logic into a dedicated parser.py or keep it as a robust @classmethod that handles encoding errors.



    




file = open(r'data\[Crunchyroll Retime] Kimetsu no Yaiba - S01E01.ja.srt','r',encoding='utf-8')


obj = srtFile.from_file(file)

# for name in set(obj.extract_names()):
#     print(name)
text = obj.get_words()
print(len(text))
# import time
from api.japanese.jisho import get_word
from modules.japanese.Japanese_card import JishoWord
# for word in text[30:36]:
#     get_word(word.surface)
#     time.sleep(5)
    
path = 'data\words'

# l = []
for file in os.listdir(path)[-1:]:
    fPath = os.path.join(path,file)
    f = open(fPath,'r',encoding='utf-8')
    j =  json.loads(f.read())
    f.close()
    j = j['data']
    
    obj = JishoWord.from_json(j[0])
    print(obj.slug)
    print(obj.full_data)






   







