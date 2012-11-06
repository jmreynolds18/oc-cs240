# Joshua M Reynolds
# 10/28/2012
# Pygame 2
# This is a space game that creates a space background. Have a ship fly around
# the map with the keyboard. Insert 2 more images to have a total of 3 images
# in space. 


import random
import pygame
from pygame.locals import * 

width, height = 800, 600

def init():
    pygame.init()   # Initialized pygame module

    # Screen
    return pygame.display.set_mode((width, height))

def draw_space(surface, stars):
    surface.fill((0, 0, 0))          # Draw the vacuum of space
    for s in stars:
        if s[2] == 3:
            star = pygame.Color(255, 255, 255)
        elif s[2] == 2:
            star = pygame.Color(200, 200, 255)
        elif s[2] == 1:
            star = pygame.Color(255, 170, 170)
        pygame.draw.circle(surface, star, s[:2], s[2])

def build_space(screen):
    # Get a new surface and its parameters
    space = screen.copy()
    width, height = screen.get_size()

    stars = []
    for star in range(60):
        x = random.randint(0, width)
        y = random.randint(0, height)
        rand = random.randint(1, 10)
        if rand <= 6:
            r = 1
        elif rand <= 9:
            r = 2
        else:
            r = 3
        stars.append((x, y, r))

    draw_space(space, stars)
    return space

def load_bird():
    bird = pygame.image.load('bird.gif').convert_alpha()
    return bird

def load_meteor():
    meteor = pygame.image.load('asteroid-sprite.gif').convert_alpha()
    return meteor

def load_ship():
    ship = pygame.image.load('ship.gif').convert_alpha()
    return ship

def main(screen):
    running = True

    # Assign image loads to variables
    bird = load_bird()
    meteor = load_meteor()
    space = build_space(screen)
    ship = load_ship()

    # Sets the x and y coordinates for the ship movement
    x, y = (0,0)
    while running:
        # key handle to move ship
        key = pygame.key.get_pressed()
        if key[K_LEFT]:
            x-=1
        if key[K_RIGHT]:
            x+=1
        if key[K_UP]:
            y-=1
        if key[K_DOWN]:
            y+=1

        # display images
        screen.blit(space, (0, 0))
        screen.blit(bird, (180, 200))
        screen.blit(meteor, (200,80))
        screen.blit(ship, [x,y])        
        pygame.display.flip()

        # Code to exit program
        for event in pygame.event.get():                      
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                running = False
                
        
        

screen = init()
main(screen)
