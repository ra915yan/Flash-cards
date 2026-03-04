import flashCards
import json

class engine:
    def __init__(self,word:str):
        self.word = word
        self.data = json.loads(open('data.txt','r').read())
        

    
    def get_words(self):
        words = []
        for word_data in self.data:
            words.append(word_data['meta']['id'])
        return words
    

    def get_Data(self):
        return self.data
    
    def run(self):
        
        target_words = []
        
        for word_data in self.data:
            if(word_data['meta']['id'])
        
        
        
obj = engine("led")

data = obj.get_Data()

for word in data[:1]:
    print(word['cxs'])

        
        
        
        
        
        
    
