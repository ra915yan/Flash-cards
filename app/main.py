
from src.database.InterfaceAPI import JishoAPI
import config
# obj = JishoAPI("母", None)

obj = JishoAPI("kasan")

file = open("data/buffer.txt",encoding='utf-8',mode='w')
file.write(obj.get_word())






   







