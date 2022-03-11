import pygame #Imports the Pygame package, which is crucial for pretty much everything here.

pygame.init() #Initializes the Pygame module, which then allows everything that comes after to function.

white = (255, 255, 255) #Sets the RGB value for the background color.
black = (0, 0, 0) #Sets the RGB value for the player-controlled Snake.
red = (255, 0, 0) #Sets the RBG value for the squares the Snake has to collect.

dis=pygame.display.set_mode((800,600)) #Creates the screen that users will use to view the game.
pygame.display.set_caption('Snake game by ya boi Zeke') #Credits the one and only creator of this script in the top of the screen.

game_over=False #Makes the default Game Over state as false, allowing you to play the game.

x1 = 300 #Sets the default starting value of the Snake on the x axis.
y1 = 300 #Sets the default starting value of the Snake on the y axis.
 
x1_change = 0 #The variable that handles the change in x axis position.
y1_change = 0 #The variable that handles the change in y axis position.
 
clock = pygame.time.Clock() #Variable that keeps track of the time passed.

while not game_over: #Begins a while loop while the Game Over state is false.
    for event in pygame.event.get(): #Gets all of the actions that take place on the screen.
        if event.type==pygame.QUIT: #Makes it so that if the quit button is pressed on the UI, then the game quits.
            game_over=True #Makes the Game Over state true.
        if event.type == pygame.KEYDOWN: #Initiated if the user presses a key on the keyboard.
            if event.key == pygame.K_LEFT: #Initiated if the user pressed the left arrow key.
                x1_change = -10 #Moves the Snakes position to the left on the x axis.
                y1_change = 0 #Stays the same.
            elif event.key == pygame.K_RIGHT:
                x1_change = 10 #Moves the Snakes position to the right on the x axis.
                y1_change = 0 #Stays the same.
            elif event.key == pygame.K_UP:
                y1_change = -10 #Moves the Snakes position upwards on the y axis.
                x1_change = 0 #Stays the same.
            elif event.key == pygame.K_DOWN:
                y1_change = 10 #Moves the Snakes position downwards on the y axis.
                x1_change = 0 #Stays the same.
                          
    x1 += x1_change #This is what actually moves the users x axis position after the key inputs.
    y1 += y1_change #This is what actually moves the users y axis position after the key inputs.
    dis.fill(white) #Applies the previous defined RGB values to the background.
    pygame.draw.rect(dis, black, [x1, y1, 10, 10]) #Draws the square-shaped snake.
 
    pygame.display.update() #Updates the active display of the game every frame.
 
    clock.tick(30)
    
pygame.quit() #Quits the game. Pretty self-explanatory.
quit() #Quits the Python script. Even MORE self-explanatory.