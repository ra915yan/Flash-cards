from dataclasses import dataclass
import re
import fugashi

        
@dataclass
class Timestamp:
    id:             int
    start_time:     str
    end_time:       str
    text_content:   list[str]
    
    
    
    @staticmethod
    def _srt_parser(raw_str:str):
        #it is expected to have only the one time stamp
        
        
        lines = [line.strip() for line in raw_str.strip().split('\n') if line.strip()]
        
        if len(lines) < 2:
            return None
        
        try:
            start , end = re.split(r'\s*-->\s*',lines[1])
            return {
                "id": int(lines[0]),
                "start": start.strip(),
                "end": end.strip(),
                "text":lines[2:]
            }
        except (ValueError,IndexError):
            return None
        
        
        
        
    
    @classmethod
    def str_to_obj(cls, raw_ts:str) -> 'Timestamp':
        
        data = cls._srt_parser(raw_ts)
        
        if data is None:
            return cls(id=-1, start_time='', end_time='', text_content=[])
        
        
        return cls(
            id=data["id"],
            start_time=data["start"],
            end_time=data["end"],
            text_content=data["text"]
        )
        
        
        
    def __str__(self):
        return (
            f"id:             {self.id}"
            f"start_time:     {self.start_time}"
            f"end_time:       {self.end_time}"
            f"text_content:   {self.text_content}"
            )
    

@dataclass
class srtFile:
    original_text:   str
    time_stamps:    list[Timestamp]
    
    
    
    @classmethod
    def from_file(cls,f):
        txt = f.read()
        tss = [Timestamp.str_to_obj(raw_ts =timestemp) for timestemp in txt.split('\n\n')]
        return cls(
            original_text  = txt,
            time_stamps = tss
        )
        
        
    
    def get_lines(self) -> list[str]:
        return [line for ts in self.time_stamps for line in ts.text_content]
        
        
    
    def get_all_text(self) -> str:
        return "\n".join(self.get_lines())
    
    def extract_names(self):
        return re.findall(r"[（\(](.*?)[）\)]",self.get_all_text())
    
    
    def get_all_text_without_names(self):
        return re.sub(r"[（\(].*[）\)]","",self.get_all_text())
    
    def get_all_sentence_cleaned(self):
        text = self.get_all_text_without_names()
        text = re.sub(r"[♪〜！…？”“）]*","",text)
        text = re.sub(r"\n+| ","\n",text)
        # text = re.sub(r" ","\n",text)
        return [line.strip() for line in text.splitlines() if line.strip()]
    
    def get_words(self):
        sentences = self.get_all_sentence_cleaned()
        l = []
        Tagger = fugashi.Tagger()
        for sentence in sentences:
            for word in Tagger(sentence):
                l.append(word)
        return l
        
        
        
        
