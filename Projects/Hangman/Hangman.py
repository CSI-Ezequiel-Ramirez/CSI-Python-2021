import random

def getMeme(): 
    HangmanWordList = ["MEME", "MEMES", "DAT BOI", "SANIC", "WEEGEE", "I WONDER WHATS FOR DINNER", "YTP", "CRINGE", "FIDGET SPINNER", "DEAD MEME", "MLG", "AH YES THE FLOOR HERE IS MADE OF FLOOR", "GET REAL", "NYAN CAT", "WE ARE NUMBER ONE", "STEAMED HAMS", "DEEZ NUTZ", "GOTTEM GGS", "WE LIVE IN A SOCIETY", "YOUR MOM GAY", "BRUH MOMENT", "MEGALOVANIA", "PEPE HANDS", "WHY ARE WE STILL HERE", "LIGMA BALLS", "BASED AND REDPILLED", "BIG SHOT", "HIT OR MISS"]
    return random.choice(HangmanWordList).upper()

def Intro():
    Name = input("Welcome to Zeke's Epic Gamer Meme Hangman! Please enter your name so I can know if you're Based or Cringe: ")
    if Name == "Based":
        print("""Wow, you really are Based! Well then Based Department, let's begin!
              My Meme Machine will randomly select a meme, be it a word or short phrase. 
              You will have to guess that dank meme by inputting its letters before the man gets hanged.
              Don't feel too bad for him though, he plays Genshin Impact.""")
    else:
        print("What? Your name isn't the word Based written in this specific way? Now THAT's cringe. I don't want no normies in my Hangman, SCRAM!")
        #Note: Yes Cobian, you cannot play if your name is not "Based". If you ran into this, that's simply a skill issue.

def PlayAgain():
    Prompt = input("Would you like to try another GAMER meme? Enter 'Y' for yes and 'N' for no: ").upper()
    if Prompt == "Y":
        print("THIS IS A PLACEHOLDER")
        #Placeholder for now.
    else:
        print("I am judging you intensely.")

def HangMeMan():
    Intro()
    
    Characters = "QWERTYUIOPASDFGHJKLZXCVBNM"
    Meme = getMeme()
    CharactersGuessed = []
    Attempts = 6
    Guessed = False
    print()
    
    def HungMan():
        if Attempts == 6:
            print("""   +--------+
                        |        |
                        |        
                        |       
                        |       
                        |
                        |
                        |
                     ___|______________""")
        elif Attempts == 5:
            print("""   +--------+
                        |        |
                        |        O
                        |       
                        |       
                        |
                        |
                        |
                     ___|______________""")
        elif Attempts == 4:
            print("""   +--------+
                        |        |
                        |        O
                        |        |
                        |       
                        |
                        |
                        |
                     ___|______________""")
        elif Attempts == 3:
            print("""   +--------+
                        |        |
                        |        O
                        |       -|
                        |       
                        |
                        |
                        |
                     ___|______________""")
        elif Attempts == 2:
            print("""   +--------+
                        |        |
                        |        O
                        |       -|-
                        |       
                        |
                        |
                        |
                     ___|______________""")
        elif Attempts == 1:
            print("""   +--------+
                        |        |
                        |        O
                        |       -|-
                        |       /
                        |
                        |
                        |
                     ___|______________""")
        else:
            print("""   +--------+
                        |        |
                        |        O
                        |       -|-
                        |       / /
                        |
                        |
                        |
                     ___|______________""")
            
    print(HungMan)
    print("The meme contains ", len(Meme), " characters.")
    print(len(Meme) * "_")
    
    while Guessed == False and Attempts > 0:
        print("You have " + str(Attempts) + " attempts remaining.")
        Guess = input("Try guessing a letter or, if you're feeling lucky, try to guess the whole phrase: ").upper()
        if len(Guess) == 1:
            if Guess not in Characters:
                print("I said to input a letter, not whatever that is!")
            elif Guess in CharactersGuessed:
                print("You already tried that letter, you silly little STOOPID BOY!")
            elif Guess not in Meme:
                print("Oops! That letter is not in the dank meme of choice.")
                CharactersGuessed.append(Guess)
                Attempts = -1
                print(HungMan)