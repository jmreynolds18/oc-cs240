# Author: Joshua M Reynolds
# Date: September 19, 2012
# Assignment: Lab 00
# Description: This is a basic program of pygame that will display a
# blue background, display an olympic flag, and the ability to quit/exit
# program.

# Added September 24, 2012 : Added bird image to move across the map
# and spin at the same time.

width, height = 640, 480 
horizontal = 2
vertical = 4


import pygame   
def init():
    pygame.init()   

    # sets the screen size
    return pygame.display.set_mode((width, height))

def draw_flag(screen, width, height):
     # creates olympic flag                         
        pygame.draw.rect(screen,(255, 255, 255),(160,100,300,250)) # white rectangle
        pygame.draw.circle(screen,(0,0,255),(220,180), 50, 3)      # blue ring
        pygame.draw.circle(screen,(0,0,0),(310,180),50,3)          # black ring    
        pygame.draw.circle(screen,(255,0,0),(400,180),50,3)        # red ring
        pygame.draw.circle(screen,(255,255,0),(255,250),50,3)      # yellow ring
        pygame.draw.circle(screen,(0,255,0),(360,250),50,3)        # green ring
    

def main(screen,width,height,vertical,horizontal):
    running = True
    bird = pygame.image.load("bird.gif").convert_alpha()
    bird_rect = bird.get_rect()
    while running:
        running = True
        # creates blue background                      
        screen.fill((173, 216, 230))
        
        # Adds the bird image and spins it
        screen.blit(bird, bird_rect)    
        bird = pygame.transform.rotate(bird, 90)

        # Drasws flag and displays it
        draw_flag(screen,width,height)
        pygame.display.flip()      

        # Move bird, 1 pixel horizontal, Move bird 1 pixel vertical
        bird_rect[0] += horizontal      
        bird_rect[1] += vertical        
        
        # bound checking
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
screen=init()
draw_flag(screen,width,height) 
main(screen,width,height,vertical,horizontal)
    
