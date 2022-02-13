import random

def getMeme(): 
    HangmanWordList = ["MEME", "MEMES", "DAT BOI", "SANIC", "WEEGEE", "I WONDER WHATS FOR DINNER", "YTP", "CRINGE", "FIDGET SPINNER", "DEAD MEME", "MLG", "AH YES THE FLOOR HERE IS MADE OF FLOOR", "GET REAL", "NYAN CAT", "WE ARE NUMBER ONE", "STEAMED HAMS", "DEEZ NUTZ", "GOTTEM GGS", "WE LIVE IN A SOCIETY", "YOUR MOM GAY", "BRUH MOMENT", "MEGALOVANIA", "PEPE HANDS", "WHY ARE WE STILL HERE", "LIGMA BALLS", "BASED AND REDPILLED"]
    return random.choice(HangmanWordList).upper()

def Intro():
    Name = input("Welcome to Zeke's Epic Gamer Meme Hangman! Please enter your name so I can know if you're Based or Cringe: ")
    if Name == "Based":
        print("Wow, you really are Based! Well then Based Department, let's begin!")
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