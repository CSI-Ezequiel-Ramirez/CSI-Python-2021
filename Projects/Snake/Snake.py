import pygame #Imports the Pygame package, which is crucial for pretty much everything here.
pygame.init() #Initializes the Pygame module, which then allows everything that comes after to function.
dis=pygame.display.set_mode((400,300)) #Creates the screen that users will use to view the game.
pygame.display.update() #This method updates any changes made to said screen.
pygame.display.set_caption('Snake game by ya boi Zeke') #Credits the one and only creator of this script in the top of the screen.
game_over=False #Makes the default Game Over state as false, allowing you to play the game.
while not game_over: #Begins a while loop while the Game Over state is false.
    for event in pygame.event.get(): #Gets all of the actions that take place on the screen.
        if event.type==pygame.QUIT: #Makes it so that if the quit button is pressed on the UI, then the game quits.
            game_over=True #Makes the Game Over state true.

pygame.quit() #Quits the game. Pretty self-explanatory.
quit() #Quits the Python script. Even MORE self-explanatory.