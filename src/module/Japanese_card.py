from dataclasses import dataclass, field
from typing import Optional
from src.module.InterfaceDataObject import InterfaceDataObject,ColumnSetting


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
            return (
                f"reading: {self.reading}"
                    )
        else:
            return (
            f"word: {self.kanji}",
            f"reading {self.reading}"
                    )
        
    
    
@dataclass  
class JishoWord(InterfaceDataObject):

    slug:       str                 
    is_common:  bool                
    jlpt_level: list[str]           

    forms:      list[JapaneseForm]  
    senses:     list[Sense]     
    
    @property
    def primary_definition(self):
        return ', '.join(self.senses[0].english_definitions)
    
    @property
    def info(self):
        return (
            f"Word:       {self.slug}\n",
            f"Reading:    {self.forms[0].reading}\n",
            f"JLPT_level: {self.jlpt_level}\n",
            f"Definition: {self.primary_definition}\n",
            f"Common:     {'Yes' if self.is_common else 'No'}\n"
                    )
        
    @property
    def full_data(self):
        return "\n".join([
            f"\tword:           {self.slug}",
            f"\tis_common:      {self.is_common}",
            f"\tis_derogatory:  {self.senses[0].is_derogatory}",
            f"\tlevel:          {self.jlpt_level}\n",

            "forms:",
            f"{"\n--\n".join([str(f) for f in self.forms])}\n\n",
            
            "senses:",
            f"\t{"\n--\n".join([str(s) for s in self.senses])}",

                    ])
    
    
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
        