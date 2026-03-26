import os
from dotenv import load_dotenv

load_dotenv()

KANJI_PATTERN       = "\u4e00-\u9faf"
Hiragana_PATTERN    = "\u3040-\u309f"
Katakana_PATTERN    = "\u30a0-\u30ff"
JP_PATTERN          = "\u3000-\u303f"

DICTIONARY_API_BASE_URL = r"https://www.dictionaryapi.com/api/v3/references/learners/json"
DICTIONARY_API_KEY = os.getenv("dictionaryapi_key")



JISHO_BASE_URL = r"https://jisho.org/api/v1/search/words?keyword="

LOGS_PATH = r"logs"