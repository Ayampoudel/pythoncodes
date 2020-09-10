import json
data=json.load(open("data.json"))
from difflib import get_close_matches

def search(word):
    if word in data:
        a=data[word]
        if type(a)==list:
            for item in a:
                print (item)
        else:
            return print(a)

    elif(len(get_close_matches(word,data.keys())))>0:
        print("did you mean %s "%get_close_matches(word,data.keys())[0])
            
    else:
        return print("the word does not exist in the dictionary")



input=input("Enter the word you want to search")
x=input.lower()
search(x)
