import sqlite3
from modules.japanese.Japanese_card import JishoWord,JapaneseForm,Sense
class AnkiDatabase:
    
    def __init__(self):
        self.conn = sqlite3.connect(r"data\anki_japanese.db")
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self._create_tables()
        
    def _create_tables(self):
        cursor = self.conn.cursor()
        for script in tables_script():
            cursor.execute(script)
            
        self.conn.commit()
        
        
    def add_word(self, obj: JishoWord ):
        
        
        cursor = self.conn.cursor()
        
        
        cursor.execute(
            "INSERT INTO vocabulary (is_common, jlpt_level) VALUES (?,?)",
            (obj.is_common, obj.jlpt_level)
        )
        
        vocab_id = cursor.lastrowid
        for index, form in enumerate(obj.forms):
            is_primary = 1 if index == 0 else 0
            cursor.execute(
                "INSERT INTO forms (vid, kanji, reading, is_primary) Values (?,?,?,?)",
                (vocab_id, form.kanji, form.reading, is_primary)
            )
        
        for sense in obj.senses:
            english_definitions = ",".join(sense.english_definitions)
            parts_of_speech = ",".join(sense.parts_of_speech)
            cursor.execute(
                "Insert Into senses (vid, english_def, part_of_speech, is_derogatory) Values (?,?,?,?)",
                (vocab_id, sense.english_definitions, parts_of_speech, sense.is_derogatory)
        )
            
        self.conn.commit()
        
        
        
    def exists(self, word:str ) -> bool:
        """Checks if a word (Kanji or Reading) already exists in the database."""
        cursor = self.conn.cursor()
        quary = "Select 1 From form where kanji = ? OR reading = ? Limit 1"
        cursor.execute(quary, (word,word))
        return cursor.fetchone() is not None