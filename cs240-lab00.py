# Author: Joshua M Reynolds
# Date: September 19, 2012
# Assignment: Lab 00
# Description: This is a basic program of pygame that will display a
# blue background, display an olympic flag, and the ability to quit/exit
# program.

# Added September 24, 2012 : Added bird image to move across the map
# and spin at the same time.


import pygame   

pygame.init()   

# sets the screen size
width, height = 640, 480 
screen = pygame.display.set_mode((width, height))

# Loads image of the bird
bird = pygame.image.load("bird.gif").convert_alpha()
bird_rect = bird.get_rect()


horizontal = 2
vertical = 4

# This loop creates bluebackground, bird image to spin
# olympic flag, and creates an exit program feature

running = True
while running:
    # creates blue background                      
    screen.fill((173, 216, 230)) 
    
    # Adds the bird image and spins it
    screen.blit(bird, bird_rect)    
    bird = pygame.transform.rotate(bird, 90)

    # creates olympic flag                         
    pygame.draw.rect(screen,(255, 255, 255),(160,100,300,250)) # white rectangle
    pygame.draw.circle(screen,(0,0,255),(220,180), 50, 3)      # blue ring
    pygame.draw.circle(screen,(0,0,0),(310,180),50,3)          # black ring    
    pygame.draw.circle(screen,(255,0,0),(400,180),50,3)        # red ring
    pygame.draw.circle(screen,(255,255,0),(255,250),50,3)      # yellow ring
    pygame.draw.circle(screen,(0,255,0),(360,250),50,3)        # green ring
    
    # displays the images onto the screen
    pygame.display.flip()      

    # Move bird, 1 pixel horizontal, Move bird 1 pixel vertical
    bird_rect[0] += horizontal      
    bird_rect[1] += vertical        
    
    # this part will move the image across the screen
    if bird_rect.right >= width:
        horizontal = -1
    elif bird_rect.left <= 0:
        horizontal = 1
    if bird_rect.bottom >= height:
        vertical = -3
    elif bird_rect.top <= 0:
        vertical = 3
                                 
    
    # code to exit program
    for event in pygame.event.get():                      
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            running = False
    
    
