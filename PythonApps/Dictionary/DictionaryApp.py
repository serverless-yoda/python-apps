import json
import os
from difflib import get_close_matches

#get script filename location
absFilePath = os.path.abspath(__file__)

#get folder of the dictionary
path, filename = os.path.split(absFilePath)
#print("Script file path is {}, filename is {}".format(path, filename))

dictionaryPath = path + "\data.json"

#load json and return dictionary
data = json.load(open(dictionaryPath))
#print(type(data))

def wordmeaning(word):   
    if word in data:
        return data[word]     
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:
        matches = len(get_close_matches(word,data.keys()))
        answer = input("There are possible %s matches. Do you want to return them? Type 'Y' for Yes, 'S' to skip and other letter to exit: " % matches)
        if answer.upper() == 'Y':
            return get_close_matches(word,data.keys())
        elif answer.upper() == 'S':
            firstmatch = get_close_matches(word,data.keys())[0]
            answer = input("Do you want to get the first match? Type 'Y' for Yes, 'S' to skip: ")            
            if answer.upper() == 'Y':
                return data[firstmatch]
            else:
                return "Word not found"
        else:
            return 'EXIT' #exit
    else:
        return "Word not found"

flag = ''
while flag != 'EXIT':
    word = input("Enter word:")
    if word != "EXIT":
        if(len(word) >= 3):        
            meaning = wordmeaning(word.lower())

            if(type(meaning) == list):
                for item in meaning:
                    print(item)
            elif meaning.upper() == 'EXIT': #exit
                flag = 'EXIT'
            else:
                print(meaning)
        else:
            print("\nEnter more than two letters")
    else:
        flag = "EXIT"



