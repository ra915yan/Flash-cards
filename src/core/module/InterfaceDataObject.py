from dataclasses import dataclass,asdict,field,fields
from abc import ABC
from enum import Enum

att_eq_sql = {"str":"TEXT","int":"INTEGER","bool":"boolean"}

def ColumnSetting(default=None, primary_key=False, nullable=True, foreign_key=None):
    metadata = {
        "primary_key"   : primary_key,
        "nullable"      : nullable,
        "foreign_key"   : foreign_key
    }
    return field(default=default, metadata=metadata)

@dataclass
class InterfaceDataObject:

    @property
    def get_name_class(self):
        return self.__class__.__name__
    
    def get_attributes_names(self):
        return asdict(self).keys()




