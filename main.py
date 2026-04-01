
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
from functools import reduce
import operator
# from xml_filter.dataClasses import Entry, KanjiElement, ReadingElement, Sense
import config
from xml_filter.XML_node import XML_parser, XML_node



    


list_paths = XML_parser.get_list_paths(config.KANA_XML_FILE_PATH_JMDICT_E)

for path in sorted(list_paths, key=len):
    print(path)
























