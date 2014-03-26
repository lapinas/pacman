import pygame

# COLOURS:
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)

# Window:
size = (700,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Pacman Version 0.1 | Press ESC to quit")

#Constants for game:
programOn = True
gameWon = False
clock = pygame.time.Clock()
steps = 1                                       # How many pixels should one step have
jumps = 10                                      # How many clock ticks should be skipped before every face change
directions = [False,False,False,False]          # List of direction keys pressed
scale = 30                                      # Width and Height of character

# Class for pacman:
class character():
    x = 0
    y = 0
    image = ''
    direction = 3
    closed = True

# List of pacman images:
pacman = [['UpClosed.gif','UpOpen.gif'],['DownClosed.gif','DownOpen.gif'],['RightClosed.gif','RightOpen.gif'],['LeftClosed.gif','LeftOpen.gif']]
for i in range(4):
    pacman[i][0]=pygame.transform.scale(pygame.image.load(pacman[i][0]).convert(),(scale,scale))
    pacman[i][1]=pygame.transform.scale(pygame.image.load(pacman[i][1]).convert(),(scale,scale))

# Constants for player:
buttonPressed = False
counter = 0
player = character
player.image = pacman[2][0]

# Functions for game logics:
def faceChanges(player):                        # Swaps between characters images
    if player.closed:
        player.closed = False
        player.image = pacman[player.direction-1][1]
    else:
        player.closed = True
        player.image = pacman[player.direction-1][0]
    return player

def moves(player):                              # Moves character to specified direction
    if player.direction == 1:
        player.y = player.y - steps
    elif player.direction == 2:
        player.y = player.y + steps
    elif player.direction == 3:
        player.x = player.x + steps
    elif player.direction == 4:
        player.x = player.x - steps
    return player

def chooseDirection(player):                    # chooses witch direction to go
    for i in range(4):
        if directions[i] and not directions[player.direction - 1]:
            player.direction = i+1
    return player

while programOn:
    # ALL EVENT PROCESSING:
    for event in pygame.event.get():            # User did something
        
        if event.type == pygame.QUIT:           # If user clicked close the window:
            programOn = False
            
        # User pressed down on a key:    
        if event.type == pygame.KEYDOWN: 
            # It's esc button:
            if event.key == pygame.K_ESCAPE: 
                programOn = False
            # It's up or 'w' button:
            if (event.key == pygame.K_UP) or (event.key == pygame.K_w): 
                buttonPressed = True
                player.direction = 1
                directions[0] = True
            # It's down or 's' button:
            if (event.key == pygame.K_DOWN) or (event.key == pygame.K_s): 
                buttonPressed = True
                player.direction = 2
                directions[1] = True
            # It's right or 'd' button:
            if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d): 
                buttonPressed = True
                player.direction = 3
                directions[2] = True
            # It's left or 'a' button:
            if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a): 
                buttonPressed = True
                player.direction = 4
                directions[3] = True

        # User let up on a key:        
        if event.type == pygame.KEYUP:
            # It's up or 'w' button:
            if (event.key == pygame.K_UP) or (event.key == pygame.K_w): 
                directions[0] = False
                chooseDirection(player)
            # It's down or 's' button:
            if (event.key == pygame.K_DOWN) or (event.key == pygame.K_s): 
                directions[1] = False
                chooseDirection(player)
            # It's right or 'd' button:
            if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d): 
                directions[2] = False
                chooseDirection(player)
            # It's left or 'a' button:
            if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a): 
                directions[3] = False
                chooseDirection(player)
              
    # END OF EVENT PROCESSING. 
    # ALL GAME LOGIC:
    if not (directions[0] or directions[1] or directions[2] or directions[3]): 
        buttonPressed = False
        
    if not gameWon:
        if buttonPressed:
            player = moves(player)
            if counter == jumps:
                player = faceChanges(player)
                counter = 0
            else:
                counter = counter + 1
        else:
            player.closed = True
            player.image = pacman[player.direction-1][0]
    # END OF GAME LOGIC. 
    # ALL CODE TO DRAW:
    screen.fill(black)                          # Clear the screen and set the screen background
    
    if not gameWon:
        screen.blit(player.image, [player.x,player.y])
        
    pygame.display.flip()                       # Shows what was drawn
    # END OF CODE TO DRAW.
    # Frames per second:
    clock.tick(120)

pygame.quit()
