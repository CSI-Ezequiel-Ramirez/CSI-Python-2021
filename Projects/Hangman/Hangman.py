import random

def getMeme(): 
    HangmanWordList = ["MEME", "MEMES", "DAT-BOI", "SANIC", "WEEGEE", "I-WONDER-WHATS-FOR-DINNER", "YTP", "CRINGE", "FIDGET-SPINNER", "DEAD-MEME", "MLG", "AH-YES-THE-FLOOR-HERE-IS-MADE-OF-FLOOR", "GET-REAL", "NYAN-CAT", "WE-ARE-NUMBER-ONE", "STEAMED-HAMS", "DEEZ-NUTZ", "GOTTEM-GGS", "WE-LIVE-IN-A-SOCIETY", "YOUR-MOM-GAY", "BRUH-MOMENT", "MEGALOVANIA", "PEPE-HANDS", "WHY-ARE-WE-STILL-HERE", "LIGMA-BALLS", "BASED-AND-REDPILLED", "BIG-SHOT", "HIT-OR-MISS"]
    return random.choice(HangmanWordList).upper()

def Intro():
    Name = input("Welcome to Zeke's Epic Gamer Meme Hangman! Please enter your name so I can know if you're Based or Cringe: ")
    if Name == "Based":
        print("""Wow, you really are Based! Well then Based Department, let's begin!
              My Meme Machine will randomly select a meme, be it a word or short phrase. 
              You will have to guess that dank meme by inputting its characters before the man gets hanged.
              Don't feel too bad for him though, he plays Genshin Impact.""")
    else:
        print("What? Your name isn't the word Based written in this specific way? Now THAT's cringe. I don't want no normies in my Hangman, SCRAM!")
        exit()
        #Note: Yes Cobian, you cannot play if your name is not "Based". If you ran into this, that's simply a skill issue.

def PlayAgain():
    Prompt = input("Would you like to try another GAMER meme? Enter 'Y' for yes and literally anything else for no: ").upper()
    if Prompt == "Y":
        print("Alrighty then! Let's do this!")
        HangMeMan()
        
    else:
        print("I am judging you intensely.")
        exit()

Intro()

def HangMeMan():
    Characters = "QWERTYUIOPASDFGHJKLZXCVBNM-"
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
        Guess = input("Try guessing an letter, a - to represent a space or, if you're feeling lucky, try to guess the whole phrase: ").upper()
        
        if len(Guess) == 1:
            if Guess not in Characters:
                print("I said to input a letter, not whatever that is!")
            elif Guess in CharactersGuessed:
                print("You already tried that letter, you silly little STOOPID BOY!")
            elif Guess not in Meme:
                Attempts -= 1
                print(HungMan)
                print("Oops! That letter is not in the dank meme of choice.")
                CharactersGuessed.append(Guess)
                print(CharactersGuessed)
            elif Guess in Meme:
                print(HungMan)
                print("Poggers! That letter is in the meme!")
                CharactersGuessed.append(Guess)
                print(CharactersGuessed)
            else:
                print("Dude what the hell did you do get this???")
        
        elif len(Guess) == len(Meme):
            if Guess == Meme:
                print("PogChamp! You got got the meme correctly! :)")
                Guessed = True
                PlayAgain()
            else:
                Attempts -= 1
                print(HungMan)
                print("Congratulations, you got the meme WRONG! You absolute baffoon! >:)")
        
        else:
            Attempts -= 1
            print(HungMan)
            print("Bruh, the length of what you entered is not the same as the meme. -1 attempts for being STOOPID.")
        
        MemeStatus = ""
        
        if Guessed == False:
            for Characters in Meme:
                if Characters in CharactersGuessed:
                    MemeStatus += Characters
                else:
                    MemeStatus += "_"
            print(MemeStatus)
        
        if MemeStatus == Meme:
            print("PogChamp! You got got the meme correctly! :)")
            Guessed == True
            PlayAgain()
        elif Attempts == 0:
            print(HungMan)
            print("Imagine running out of attempts and losing the game. Literally could not be me.")
            PlayAgain()

HangMeMan()