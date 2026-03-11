from dataclasses import dataclass, field
from typing import Optional



@dataclass
class Sense:
    english_definitions:    list[str]
    parts_of_speech:        list[str]
    is_derogatory:          bool        = False
    see_also:               list[str]   = field(default=list)
    tags:                   list[str]   = field(default=list)
    
    @classmethod
    def from_dict(cls, sense_dict: dict) -> 'Sense':
        tags = sense_dict.get('tags',[])
        return cls(
            english_definitions=    sense_dict.get('english_definitions',[]),
            parts_of_speech=        sense_dict.get('parts_of_speech',[]),
            see_also=               sense_dict.get('see_also',[]),
            tags =                  tags,
            is_derogatory= 'Derogatory' in tags
        )
        
    def __str__(self):
        return f"""
english_definitions:
    {"\n".join(self.english_definitions)}
    
parts_of_speech:
    {"\n".join(self.parts_of_speech)}

see_also:
    {"\n".join(self.see_also)}
    
tags:
    {"\n".join(self.tags)}
"""
    

@dataclass
class JapaneseForm:
    kanji: Optional[str]
    reading: str
    
    
    @classmethod
    def from_dict(cls, japanese_word: dict) -> 'JapaneseForm':
        return cls(
            kanji = japanese_word.get("word"),
            reading = japanese_word.get('reading',"")
        )
        
    def __str__(self):
        if self.kanji is None:
            return f"reading: {self.reading}"
        else:
            return f"""
word: {self.kanji}
reading {self.reading}
"""
        
    
    
@dataclass  
class JishoWord:
    slug: str
    is_common: bool
    jlpt_level: list[str]
    forms: list[JapaneseForm]
    senses: list[Sense]
    
    @property
    def primary_definition(self):
        return ', '.join(self.senses[0].english_definitions)
    
    @property
    def info(self):
        return f"""
Word:       {self.slug}
Reading:    {self.forms[0].reading}
JLPT_level: {self.jlpt_level.get}
Definition: {self.primary_definition}
Common:     {'Yes' if self.is_common else 'No'}
        """
        
    @property
    def full_data(self):
        return f"""
    word:           {self.slug}
    is_common:      {self.is_common}
    is_derogatory:  {self.senses[0].is_derogatory}
    level:          {self.jlpt_level}

forms:
    {"\n--\n".join([str(f) for f in self.forms])}
    
    
senses:
    {"\n--\n".join([str(s) for s in self.senses])}

"""
    
    
    @classmethod
    def from_json(cls, data: dict) -> 'JishoWord':
        
        senses          = [ Sense.from_dict(s) for s in data['senses']]
        japanese_forms  = [ JapaneseForm.from_dict(f) for f in data['japanese']]
        
        return cls(
            slug        = data.get('slug', ""),
            is_common   = data.get('is_common', False),
            jlpt_level  = data.get('jlpt', []),
            forms       = japanese_forms,
            senses      = senses
            
        )
        