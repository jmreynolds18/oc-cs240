# Joshua M Reynolds
# 10/28/2012
# Pygame 2
# This is a space game that creates a space background. Have a ship fly around the map.
# Create a meteor that moves across the map. The last image is a bird which I still have to figure out
# what I want that image to do. The ship will have to be movable with the keyboard.

import random
import pygame

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

    bird = load_bird()
    meteor = load_meteor()
    space = build_space(screen)
    ship = load_ship()
    
    while running:
        screen.blit(space, (0, 0))
        screen.blit(bird, (100, 100))
        screen.blit(meteor, (200,80))
        screen.blit(ship, (0,0))

        # Meteor Spinning
        meteor = pygame.transform.rotate(meteor, 90)
        pygame.display.flip()


        # Not Working, I want the meteor to spin around the map.
        
##        pygame.display.flip()           # Display screen in window
##        # Move meteor, 1 pixel horizontal, Move meteor 1 pixel vertical
##        meteor[0] += horizontal      
##        meteor[1] += vertical        
##        
##        # bound checking
##        if meteor.right >= width:
##            horizontal = -1
##        elif meteor.left <= 0:
##            horizontal = 1
##        if meteor.bottom >= height:
##            vertical = -3
##        elif meteor.top <= 0:
##            vertical = 3
##        pygame.display.flip()           # Display screen in window

        # Code to exit program
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # exit()
                running = False


screen = init()
main(screen)
