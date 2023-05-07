import re

def welcomeMessage():
    print("welcom to us \n playing with me and inter an objective \n")

def read_tamplate(path):
    try:
      with open(path , 'r') as f:
        global file 
        file= f.read()
    except FileNotFoundError:
       print("missing.txt")
       

def parse_template(text):
    global new_text,tupleWord
    new_text = re.sub(r'{.*?}', '{}', text)
    matchesWord = re.findall(r'{(.*?)}', text)
    tupleWord = tuple(matchesWord)
    return (new_text,tupleWord)

def prompt():
    userInput=input("enter the word needs !!")
    global tupleUser
    tupleUser=tuple(userInput)

def merge():
    for word in new_text:
       madlibText= word.insert(tupleUser)
    print(madlibText) 








