import requests


#goal to ask the user and return a word
def get_word()->str:
    
    
    word = input("Enter the word you want: ")
    sentence = "sentence" #currently let it hardcoded
    
    data ={
        "word":word,
        "sentence":sentence
    }
    return data

file = open("data.txt",'a+')





while(True):
    pass
    tup = get_word()
    
    if(tup[0] == 'exit'):
        break
    
    file.write(f"{tup[0]}\t{tup[1]}\n")
    file.flush()
    print(f"saved: {tup[0]}")
    

