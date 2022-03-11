import pygame #Imports the Pygame package, which is crucial for pretty much everything here.
import time #Imports the Time package, which makes the games internal timer system function.
pygame.init() #Initializes the Pygame module, which then allows everything that comes after to function.

white = (255, 255, 255) #Sets the RGB value for the background color.
black = (0, 0, 0) #Sets the RGB value for the player-controlled Snake.
red = (255, 0, 0) #Sets the RBG value for the squares the Snake has to collect.

dis_width = 800 #Sets the width of the Snake.
dis_height  = 600 #Sets the height of the Snake.
dis=pygame.display.set_mode((800,600)) #Creates the screen that users will use to view the game.
pygame.display.set_caption('Snake game by ya boi Zeke') #Credits the one and only creator of this script in the top of the screen.

game_over=False #Makes the default Game Over state as false, allowing you to play the game.

x1 = dis_width/2 #Sets the default starting value of the Snake on the x axis.
y1 = dis_height/2 #Sets the default starting value of the Snake on the y axis.
 
snake_block = 10 #Creates a variable that represents the Snake block.
 
x1_change = 0 #The variable that handles the change in x axis position.
y1_change = 0 #The variable that handles the change in y axis position.
 
clock = pygame.time.Clock() #Variable that keeps track of the time passed.
snake_speed = 30 #The variable that controls the speed of the Snake.


font_style = pygame.font.SysFont(None, 50) #The font of ingame text.

def message(msg,color): #This function is called whenever text needs to be displayed onscreen.
    mesg = font_style.render(msg, True, color) #This line determines the text's font and color.
    dis.blit(mesg, [dis_width/2, dis_height/2]) #This line determines the position of the text.

while not game_over: #Begins a while loop while the Game Over state is false.
    for event in pygame.event.get(): #Gets all of the actions that take place on the screen.
        if event.type==pygame.QUIT: #Makes it so that if the quit button is pressed on the UI, then the game quits.
            game_over=True #Makes the Game Over state true.
        if event.type == pygame.KEYDOWN: #Initiated if the user presses a key on the keyboard.
            if event.key == pygame.K_LEFT: #Initiated if the user pressed the left arrow key.
                x1_change = -10 #Moves the Snakes position to the left on the x axis.
                y1_change = 0 #Stays the same.
            elif event.key == pygame.K_RIGHT: #Initiated if the user pressed the right arrow key.
                x1_change = 10 #Moves the Snakes position to the right on the x axis.
                y1_change = 0 #Stays the same.
            elif event.key == pygame.K_UP: #Initiated if the user pressed the up arrow key.
                y1_change = -10 #Moves the Snakes position upwards on the y axis.
                x1_change = 0 #Stays the same.
            elif event.key == pygame.K_DOWN: #Initiated if the user pressed the down arrow key.
                y1_change = 10 #Moves the Snakes position downwards on the y axis.
                x1_change = 0 #Stays the same.
    
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #This elif checks every frame if the Snake is out-of-bounds or not.
        game_over = True #Initiates a Game Over if the player tries to go out-of-bounds.
                          
    x1 += x1_change #This is what actually moves the users x axis position after the key inputs.
    y1 += y1_change #This is what actually moves the users y axis position after the key inputs.
    dis.fill(white) #Applies the previous defined RGB values to the background.
    pygame.draw.rect(dis, black, [x1, y1, 10, 10]) #Draws the square-shaped snake.
 
    pygame.display.update() #Updates the active display of the game every other frame.
 
    clock.tick(snake_speed) #Makes the game at the snake's speed, which in this case is 30, so it runs at 30 FPS.

message("You lost",red) #Prints the text that indicates a Game Over on the screen.
pygame.display.update() #Updates the game screen to reflect the Game Over state.
time.sleep(2) #Makes the game wait for exactly 2 seconds before automatically closing itself.
    
pygame.quit() #Quits the game. Pretty self-explanatory.
quit() #Quits the Python script. Even MORE self-explanatory.