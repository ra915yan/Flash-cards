
import os
import xml.etree.ElementTree as ET
KANA_PATH = r"data\\Japanese_dictionary\\JMdict_e.xml"


entry_count = 0

def recursiveIterXML(PATH:str, number_of_top_nodes = 1):
    context = ET.iterparse(source= PATH, events=('end',))
    for _ in range(number_of_top_nodes):
        event, root = next(context)








   







