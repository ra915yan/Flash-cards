from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class KanjiElement:
    """Mapped directly from k_ele dict"""
    keb: str                                       # min 1, max 1
    ke_pri: List[str] = field(default_factory=list) # min 0, max 4
    ke_inf: List[str] = field(default_factory=list) # min 0, max 2

@dataclass
class ReadingElement:
    """Mapped directly from r_ele dict"""
    reb: str                                       # min 1, max 1
    re_nokanji: Optional[str] = None               # min 0, max 1 (Correction applied)
    re_restr: List[str] = field(default_factory=list) # min 0, max 5
    re_pri: List[str] = field(default_factory=list)   # min 0, max 5
    re_inf: List[str] = field(default_factory=list)   # min 0, max 2

@dataclass
class Sense:
    """Mapped directly from sense dict"""
    pos: List[str] = field(default_factory=list)      # min 1, max 6
    gloss: List[str] = field(default_factory=list)    # min 1, max 15
    xref: List[str] = field(default_factory=list)     # min 0, max 13
    s_inf: Optional[str] = None                       # min 0, max 1 (Correction applied)
    misc: List[str] = field(default_factory=list)     # min 0, max 5
    dial: List[str] = field(default_factory=list)     # min 0, max 3
    stagk: List[str] = field(default_factory=list)    # min 0, max 4
    stagr: List[str] = field(default_factory=list)    # min 0, max 4
    field_tag: List[str] = field(default_factory=list)# min 0, max 3
    lsource: List[str] = field(default_factory=list)  # min 0, max 4
    ant: List[str] = field(default_factory=list)      # min 0, max 2

@dataclass
class Entry:
    """Mapped directly from entry dict"""
    ent_seq: str                                      # min 1, max 1
    r_ele: List[ReadingElement] = field(default_factory=list) # min 1, max 40
    sense: List[Sense] = field(default_factory=list)          # min 1, max 26
    k_ele: List[KanjiElement] = field(default_factory=list)   # min 0, max 17