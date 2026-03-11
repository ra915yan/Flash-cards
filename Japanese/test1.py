import fugashi
import re
from dataclasses import dataclass
import json

@dataclass
class timeStamp:
    id:             int
    start_time:     str
    end_time:       str
    text_content:   list[str]
    
    @classmethod
    def str_to_ts(cls, raw_ts:str) -> 'timeStamp':
        l = raw_ts.split('\n')
        try:
            time = l[1].split('-->')
            return cls(
                id=l[0],
                start_time=time[0],
                end_time=time[1],
                text_content=l[2:]
            )
        except Exception as e:
            return cls(id = -1, start_time = '',end_time='',text_content=[])
        
    def __str__(self):
        return f"""
id:             {self.id}
start_time:     {self.start_time}
end_time:       {self.end_time}
text_content:   {self.text_content}
"""
    
    
@dataclass
class translation_file:
    original_text:   str
    time_stamps:    list[timeStamp]
    
    
    
    @classmethod
    def from_file(cls,f):
        txt = file.read()
        tss= [timeStamp.str_to_ts(raw_ts) for raw_ts in txt.split('\n\n')]
        return cls(
            original_text  = txt,
            time_stamps = tss
        )


kanji_pattern = re.compile(r'[\u4e00-\u9faf]+')

file = open('Japanese\[Crunchyroll Retime] Kimetsu no Yaiba - S01E01.ja.srt','r',encoding='utf-8')
tagger = fugashi.Tagger()


obj = translation_file.from_file(file)

[print(ts) for ts in obj.time_stamps]

