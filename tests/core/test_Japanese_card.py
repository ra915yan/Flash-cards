import pytest
from src.module.Japanese_card import Sense,JishoWord,JapaneseForm


Sense_sample = {
                    "english_definitions": ["mother"],
                    "parts_of_speech": ["Noun"],
                    "tags": ["Humble (kenjougo) language"],
                    "see_also": ["\u7236"]
                }

@pytest.fixture
def sense_class():
    return Sense.from_dict(sense_dict= Sense_sample)


def test_Sense_english_definitions_attribute(sense_class: Sense):
    assert sense_class.english_definitions  == ['mother']
def test_Sense_parts_of_speech_attribute(sense_class: Sense):    
    assert sense_class.parts_of_speech      == ['Noun']
def test_Sense_tags_attribute(sense_class: Sense):
    assert sense_class.tags                 == [ "Humble (kenjougo) language"]
def test_Sense_see_also_attribute(sense_class: Sense):
    assert sense_class.see_also             == ["\u7236"]