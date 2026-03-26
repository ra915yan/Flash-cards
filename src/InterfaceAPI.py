
from abc import ABC,abstractmethod
import requests
import logging
from src import InterfaceDatabase
import config

class InterfaceAPI(ABC):
    def __init__(self, word:str, db: InterfaceDatabase):
        self._word = word
        self.setup_logging()
        self._db = db


    def get_word(self) -> str:
        return self._word
    
    def get_db(self) -> InterfaceDatabase:
        return self._db

    def _fetch(self):
        response = requests.get(url=self.get_URL())
        response.raise_for_status()
        return response.json()

    def get_data(self):
        logging.info(f"Retrieving the word: {self.get_word()}")
        
        # if self._db.exists(self._word):
        #     logging(f"found {self._word} in database")
        #     return self._db.get_data()

        logging.info(f"not found {self._word} in database")
        logging.info(f"fetch {self._word} from api: {self.get_name()}")

        try:
            data = self._fetch()
            logging.info("success")
            return data
        except Exception as e:
            logging.info("failed")
            print(e)
            return None

    def setup_logging(self):
        logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
        logging.FileHandler(fr"logs\{self.get_name()}.log", encoding='utf-8'),
        # logging.StreamHandler()
                    ]
                            )
    
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_URL(self):
        pass

    @abstractmethod
    def get_base_URL(self):
        pass




class JishoAPI(InterfaceAPI):

    def __init__(self, word, db = None):
        super().__init__(word, db)

    
    def get_name(self) -> str:
        return "jisho"

    def get_base_URL(self):
        return config.JISHO_BASE_URL


    def get_URL(self):
        return self.get_base_URL()+self._word
    




class DictionaryAPI(InterfaceAPI):

    def __init__(self, word, db = None):
        super().__init__(word, db)


    
    def get_name(self) -> str:
        return "DictionaryAPI"

    def get_base_URL(self):
        return config.DICTIONARY_API_BASE_URL


    def get_URL(self):
        return f"{self.get_base_URL()}/{self._word}?key={config.DICTIONARY_API_KEY}"


