
from dataclasses import dataclass, field
from typing import Dict, Optional
import math
import xml.etree.ElementTree as ET


@dataclass
class XML_node:
    
    tag:        str
    path:       str
    parent:     Optional['XML_node'] = None
    children:   Dict[str, 'XML_node'] = field(default_factory=dict)
    
    relation_with_children: Dict['XML_node', dict] = field(default_factory=dict)
    
    def update_bounds(self, occurrence_number:int):
        if occurrence_number > self.max_occurrence:
            self.max_occurrence = occurrence_number
        if occurrence_number < self.min_occurrence:
            self.min_occurrence = occurrence_number
            
            
    def get_parent(self):
        return self.parent
    
    def get_children(self):
        return self.children
    
    
    def __str__(self):
        return (
            f"tag:      {self.tag}"
            f"path:     {self.path}"
        )
            


@dataclass
class XML_parser:
    file_path: str
    root: 'XML_node'
    
    
    @staticmethod
    def get_list_paths(file_path:str) -> dict:
        paths = set()
        current_path = []
        
        context = ET.iterparse(file_path, events=('start','end'))
        
        for event, element in context:
            
            if event == 'start':
                current_path.append(element.tag)
                paths.add(".".join(current_path))
                
                
            if event == 'end':
                current_path.pop()
                element.clear()
                
        return sorted(list(paths))
    
    
    
    @staticmethod
    def get_tree_structure(file_path:str) -> 'XML_node':
        
        root :'XML_node'    = None
        paths:list[str]     = XML_parser.get_list_paths(file_path)
        nodes:Dict[str, 'XML_node'] = {}
        
        for path in paths:
            path_parts = path.split('.')
            tag = path_parts[-1]
            
            new_node = XML_node(path=path, tag=tag)
            
            if len(path_parts) == 1:
                root = new_node
            else:
                parent_path = '.'.join(path_parts[:-1])
                parent_node = nodes[parent_path]
                new_node.parent = parent_node
                
                
                parent_node.children[tag] = new_node
            
            nodes[path] = new_node
            
            
        return root
                      
                    
                
    
    
    
    
    @staticmethod
    def xml_relation(file_path: str):
        root_data = {}
        node_to_children = {}
        
        context = ET.iterparse(file_path, events=('end',))
        
        for event, elem in context:
            node_to_children[elem.tag] = node_to_children.get(elem.tag, 0) + 1
            
            if elem.tag not in root_data:
                root_data[elem.tag] = {}
                
            current_counts = {}
            for child in elem:
                current_counts[child.tag] = current_counts.get(child.tag, 0) + 1
                
                if child.tag not in root_data[elem.tag]:
                    initial_min = 0 if node_to_children[elem.tag] > 1 else 1
                    root_data[elem.tag][child.tag] = {'max': 0, 'min': initial_min}
                    
            for known_child, stats in root_data[elem.tag].items():
                
                actual_count = current_counts.get(known_child, 0)
                
                if actual_count > stats['max']:
                    stats['max'] = actual_count
                if actual_count < stats['min']:
                    stats['min'] = actual_count
                    
            elem.clear()
            
        return root_data


    def get_object_attribute_relation(key:str, dic:dict[str,int], child_type: str = 'str'):
        min_occurrence = dic['min']
        max_occurrence = dic['max']
        if max == 1:
            if min == 1:
                return f"{key}:{child_type}"
            else:
                return f"Optional[{key}]"
        else:
            
            f"list[{key}] = field(default_factory=list)"
            
                
    
    
    @staticmethod
    def create_templet(file_path):
        dic = XML_parser.xml_relation(file_path)
        
        for key, value in dic.items():
            
            if len(value) > 0:
                print((
                    
                      "@dataclass\n"
                      f"class {key}\n"
                      ))
        
                
                
                
        
    
    
    
            
        
        
    
    
    
        
        
        
        
    
    
    


# def get_python_type(self) -> str:
#         """Determines the exact Python type hint based on math rules."""
#         if self.max_occurrences > 1:
#             return "List[str] = field(default_factory=list)"
#         elif self.min_occurrences == 0:
#             return "Optional[str] = None"
#         else:
#             return "str"