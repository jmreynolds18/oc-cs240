# Author: Joshua M Reynolds
# Date: September 19, 2012
# Assignment: Lab 00
# Description: This is a basic program of pygame that will display a
# blue background, display an olympic flag, and the ability to quit/exit
# program.


import pygame   # imports pygame

pygame.init()   # intializes pygame

width, height = 640, 480  # sets the screen size
screen = pygame.display.set_mode((width, height))



running = True

# This while loop rewrites the background, creates the rings for the olympic flag
# and creates an exit or a quit for the program. 

while running:                      
    screen.fill((173, 216, 230)) # Will fill the back ground light blue
    pygame.draw.rect(screen,(255, 255, 255),(160,100,300,250)) # makes the white rectangle in the middle of the screen
    pygame.draw.circle(screen,(0,0,255),(220,180), 50, 3) #code for blue ring
    pygame.draw.circle(screen,(0,0,0),(310,180),50,3)     #code for black ring    
    pygame.draw.circle(screen,(255,0,0),(400,180),50,3)   #code for red ring
    pygame.draw.circle(screen,(255,255,0),(255,250),50,3) #code for yellow ring
    pygame.draw.circle(screen,(0,255,0),(360,250),50,3)   #code for green ring
    pygame.display.flip()                                 #displays the images onto the screen
    for event in pygame.event.get():                      #code to exit program
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):#if you press the red x button or press q it will close the program.
            running = False
    
    
