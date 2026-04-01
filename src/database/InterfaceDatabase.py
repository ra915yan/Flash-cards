from abc import ABC,abstractmethod
from src.core.module import InterfaceDataObject



class InterfaceDatabase(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def exists(self, word:str) -> bool:
        pass
    
    @abstractmethod
    def save(self, obj) -> bool:
        pass

    @abstractmethod
    def getFlashCard(self, word: str) -> InterfaceDataObject:
        pass