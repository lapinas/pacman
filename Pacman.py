# This version uses less pictures for player.
# Also controls are a bit changed.
# Now player always moves unless left shift is pressed.
# 'wasd' buttons and arrow keys controls the direction player is faced.
# Also Player can't leave screen.
# Things needed to be done:
# Improvent for cheking if there is an obstacle.
# Improvement of controls
# stop the animation when obstacle reached. * Should be done last

import pygame

# COLOURS:
white = (255,255,255)                           # Code for white colour
black = (0,0,0)                                 # Code for black colour

# Window:
size = (700,500)                                # Size of a window
screen=pygame.display.set_mode(size)            # Create a window
pygame.display.set_caption("Pacman multiplayer | Press ESC to quit")

#Constants for game:
programOn = True                                # Program is still working
ingame = True                                   # Game is curently played
clock = pygame.time.Clock()                     # Clock for engine
steps = 1                                       # width of each step
animate = 15                                    # length between animations (players face change)

# Class for player:
class character():
    x = 0                                       # X coordinate
    y = 0                                       # Y coordinate
    image1 = ''                                 # Image 1
    image2 = ''                                 # Image 2
    direction = 0                               # Direction faced (0 = Right, 1 = Top, 2 = Left, 3 = Down)
    closed = True                               # Position of the mouth
    moves = True                                # Player is moving
    count = 0                                   # Face change count

# Set up player images:
scale = 30                                      # Width and Height of the image
images = ['PacmanClosed.png','PacmanOpen.png']  # List of player images
images[0]=pygame.transform.scale(pygame.image.load(images[0]).convert(),(scale,scale))
images[1]=pygame.transform.scale(pygame.image.load(images[1]).convert(),(scale,scale))

# Function for face direction:
def faceDirection(player,images):
    player.image1 = pygame.transform.rotate(images[0],player.direction*90)
    player.image2 = pygame.transform.rotate(images[1],player.direction*90)
    return player

# Moves character to specified direction:
def moves(player):                              
    if player.direction == 0:                                   # Go right:
        if canMove(player.x + steps + scale,player.y + scale):  # Can move:
            player.x = player.x + steps                         # Change X coordinate by step size    
    elif player.direction == 1:                                 # Go up:
        if canMove(player.x + scale,player.y - steps):          # Can move:
            player.y = player.y - steps                         # Change Y coordinate by step size
    elif player.direction == 2:                                 # Go left:
        if canMove(player.x - steps,player.y + scale):          # Can move:
            player.x = player.x - steps                         # Change X coordinate by step size
    elif player.direction == 3:                                 # Go down:
        if canMove(player.x + scale,player.y + steps + scale):  # Can move:
            player.y = player.y + steps                         # Change Y coordinate by step size
    return player

# Checks if character can move to given location:
def canMove(x,y):                                               # This function will be improved in the future.
    if x < 0 or y < 0 or x > size[0] or y > size[1]:            # Checks if it's beyond screen borders
        return False
    else:
        return True

# Constants for player:
player = character
player = faceDirection(player,images)                           # Set player's image

# Main loop:
while programOn:
    # ALL EVENT PROCESSING:
    for event in pygame.event.get():                                        # User did something        
        if event.type == pygame.QUIT:                                       # User Closed the window:
            programOn = False                                               #   Terminate program
        if event.type == pygame.KEYDOWN:                                    # User pressed down on a key:
            if event.key == pygame.K_ESCAPE:                                # It's esc button:
                programOn = False                                           #   Terminate program
            if (event.key == pygame.K_UP) or (event.key == pygame.K_w):     # It's up or 'w' button: 
                player.direction = 1                                        #   Player faces up
            if (event.key == pygame.K_DOWN) or (event.key == pygame.K_s):   # It's down or 's' button:
                player.direction = 3                                        #   Player faces down
            if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):  # It's right or 'd' button:
                player.direction = 0                                        #   Player faces right
            if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):   # It's left or 'a' button:
                player.direction = 2                                        #   Player faces left
            if (event.key == pygame.K_LSHIFT) :                             # It's a left shift button:
                player.moves = False                                        #   player moves
        if event.type == pygame.KEYUP:                                      # User let up on a key:
            if (event.key == pygame.K_LSHIFT):                              # It's a left shift button:
                player.moves = True                                         #   Player stops                
    # END OF EVENT PROCESSING.
    # ------------------------
    # ALL GAME LOGIC:
    if ingame:
        if player.moves:
            player = moves(player)
            if player.count == animate:                     # If time to animate:
                player.closed = not player.closed           # Change face
                player.count = 0                            # Resets counting
            player.count = player.count + 1                 # Counts till next animation
            player = faceDirection(player,images)           # Set player's image
        else:
            player.closed = True                            # Closes the mouth
            player = faceDirection(player,images)           # Set player's image
            player.count = 0                                # Resets counting
    # END OF GAME LOGIC.
    # ------------------------
    # ALL CODE TO DRAW:
    screen.fill(black)                                      # Clear the screen and set the screen background
    
    if ingame:                              
        if player.closed:
            screen.blit(player.image1, [player.x,player.y]) # Draw player on screen
        else:
            screen.blit(player.image2, [player.x,player.y]) # Draw player on screen
        
    pygame.display.flip()                                   # Shows what was drawn
    # END OF CODE TO DRAW.
    # ------------------------
    clock.tick(120)                                         # Frames per second (120)
# ---------------------------------------------------
pygame.quit()
