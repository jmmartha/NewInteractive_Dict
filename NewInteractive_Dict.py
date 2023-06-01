import json

#opening the dictionary.json file in read mode
today = open("C:\\Users\DELL\Desktop\python 1\Dictionary\dictionary.json", "r")

#reading the contents for the json file to database object
database = json.load(today)

# the function displays words with a specific letter
def specletter():
    letter = input("Cool! So which letter? ")
    for i in database:
        if i.startswith(letter):
            print (i)

#user just wants to know if the word exists
def partword():
    word = input("Interesting! So which word is it? ").lower()
    found = False
    for i in database:
        if i == word:
            found = True
            if found == False:
                print("Oh sorry, I don't know that word")
            else:
                print("Well you are in luck! The word totally exixts...")

#this shows the meaning of the word
def meaning():
    word = input("Good choice! So which word do you want to know about? ").lower()
    found = False
    for key, value in database.items():
        #key is the word and value is the meaning
        if key == word:
            found = True
            print("{} means {}".format(key,value))
    if found == False:
        print("Oh sorry, I can't find that word")

#function gives the word and its meaning and also every word and their meaning in whose meaning it appears
def wordincl():
     word = input("Great! So what is it? ").lower()
     found = False
     for key,value in database.items():
         if key == word or word in value:
             found = True
             print("For {}; Here you go {}".format(key,value))
     if found == False:
         print("Oh I'm sorry. That particular one I don't have!")
    
#function gets words with specified number of letters
def numlet():
    num = int(input("Nice! So how many letters? ")) 
    found = False
    for key in database:
        if len(key)==num:
            print(key)
            found = True
    if found == False:
        print("Oh sorry! I find that I don't have words with that number of letters")    
    

#menu for interactive dictionary
while True:
    try:
        print("""
        HI THERE, I AM A DICTIONARY SPECIALLY MADE FOR YOU!
        WOULD YOU LIKE TO TRY ME OUT? YES?
        OKAY THEN LET'S GET STARTED....SHALL WE?
        ================================================== 
        
        1. Are you looking for some words that begin with a specific letter?
        2. Or would you like to just know if a particular  word exists?
        3. Perhaps you are trying to figure out the meaning of some word?
        4. How about info on a word including where it appears in a meaning description?
        5. Well maybe its words with a fixed number of letters you want?
        6. None of the above? Okay it was really nice to have you though. Bye!

        """)

#forming new variable asking user to enter a number 
        option = int(input("Hey could you choose one of the options by number. It's 1 - 6: "))
        if option == 1:
            specletter()
        elif option == 2:
            partword()
        elif option == 3:
            meaning()
        elif option == 4:
            wordincl()
        elif option == 5:
            numlet()
        elif option == 6:
            break
        else:
            print("Sorry let me explain this; you see, you have to choose only from 1, 2, 3, 4, 5, or 6")

    except:
        print("I'm sorry I don't understand you!")