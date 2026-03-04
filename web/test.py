import requests
import bs4
import os
import time
from urllib.parse import unquote
# headers = {
#     'User-Agent': 'YourBotName/1.0',
#     'Cache-Control': 'no-cache',
#     'Pragma': 'no-cache'
# }
# res = requests.get(r"https://commons.wikimedia.org/wiki/Hiragana",headers=headers)

# # res.raise_for_status()
# file = open('web.txt','wb')
# for chunk in res.iter_content(100000):
#         file.write(chunk)
        
# file.close()


# data = open('web.txt','r',encoding='utf-8').read()

# d = bs4.BeautifulSoup(data, 'html.parser')

# l = []
# for img in d.find_all('img',class_='mw-file-element'):
#     l.append(img.get('src'))
    

# file = open('links.txt','w')

# for img in l:
#     file.write(img)
#     file.write('\n')





# os.chdir(r'./web')
# paths = open('links.txt','r',encoding='utf-8').readlines()
# paths = [path[:-1] for path in paths]
# # paths = [path.replace('/thumb/','/')]

# link = []
# for img in paths:
    
#     img = img.replace('/thumb/','/')
    
#     if '.svg' in img:
#         img = img.split('.svg')[0] + '.svg'
#     elif 'gif' in img:
#        img = img.split('.gif')[0] + '.gif' 
       
#     link.append(img)
    
    
# [print(a) for a in link]
    
# dirPath = r'D:\_programming\Python_Anki_Project\web\data'
# os.makedirs(dirPath, exist_ok=True)
# headers = {'User-Agent': 'HiraganaProject/1.0 (contact: your@email.com)'}
# filesPath = os.path.join(os.getcwd(),"files")
# for url in link:
    
#     if not url:
#         continue
    
#     fileName = url.split('/')[-1]
    
#     filePath = os.path.join(filesPath,fileName)
    
#     try:
#         res = requests.get(url,headers=headers,stream=True,timeout=15)
#         res.raise_for_status()
        
#         with open(filePath ,'wb') as f:
#             for chunk in res.iter_content(chunk_size=8129):
#                 f.write(chunk)
            
#         time.sleep(2)
#     except Exception as e:
#         print(e)
            
    
    
    
    




# files_path = r'D:\_programming\Python_Anki_Project\web\files'


# for file in os.listdir(files_path):
#     if '%' in file:
        
#         new_name = unquote(file)
#         old_full_name = os.path.join(files_path, file)
#         new_full_name = os.path.join(files_path, new_name)
        
#         try:
#             os.rename(old_full_name,new_full_name)
#             print(new_full_name)
#         except Exception as e:
#             print(e)
# print("done")






from gtts import gTTS
import os
import time
import shutil
# 1. Setup
# sound_path = r'D:\_programming\Python_Anki_Project\web\sounds'
# os.makedirs(sound_path, exist_ok=True)

# 2. List of characters to generate
hiragana_to_romaji = {
    'あ': 'A',  'い': 'I',  'う': 'U',  'え': 'E',  'お': 'O',
    'か': 'KA', 'き': 'KI', 'く': 'KU', 'け': 'KE', 'こ': 'KO',
    'さ': 'SA', 'し': 'SHI', 'す': 'SU', 'せ': 'SE', 'そ': 'SO',
    'た': 'TA', 'ち': 'CHI', 'つ': 'TSU', 'て': 'TE', 'と': 'TO',
    'な': 'NA', 'に': 'NI', 'ぬ': 'NU', 'ね': 'NE', 'の': 'NO',
    'は': 'HA', 'ひ': 'HI', 'ふ': 'FU', 'へ': 'HE', 'ほ': 'HO',
    'ま': 'MA', 'み': 'MI', 'む': 'MU', 'め': 'ME', 'も': 'MO',
    'や': 'YA', 'ゆ': 'YU', 'よ': 'YO',
    'ら': 'RA', 'り': 'RI', 'る': 'RU', 'れ': 'RE', 'ろ': 'RO',
    'わ': 'WA', 'を': 'WO',
    'ん': 'N'
}

os.makedirs(os.path.join('web','data'),exist_ok=True)

romaji_to_hiragana = {value: key for key, value in hiragana_to_romaji.items()}
sounds_path = "web\sounds"
for file_name in os.listdir(sounds_path):
    file_path = os.path.join(sounds_path,file_name)
    file_
    file_new_path = os.path.join('web','data','')
    