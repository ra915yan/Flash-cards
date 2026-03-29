
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
from functools import reduce
import operator
# from xml_filter.dataClasses import Entry, KanjiElement, ReadingElement, Sense
import config
from xml_filter.XML_node import XML_parser, XML_node


def print_tree(current_node:'XML_node', level = 0):
    
    print(f"{'\t' * level}{current_node}")
    for child in current_node.get_children().values():
        print_tree(child, level + 1)
    


XML_parser.create_templet(config.KANA_XML_FILE_PATH_JMDICT_E)



























