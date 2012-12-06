# Joshua M Reynolds
# 11/12/2012
# Newship.py
# Notes on Marcus's newship.py. Basically Marcus made a ship's
# doors animate.




import random
import pygame

class NewShip(object):
	def __init__(self):
		self.image = pygame.image.load('ship.png').convert()
		self.x = 100
		self.y = 0
		self.size  = self.image.get_size()
		colorkey = self.image.get_at((self.size[0] - 1, self.size[1] -1))
		self.frame = 0

		width, height = 96, 56
		
		self.engines = self.image.subsurface((0,0) width, height)).copy()

		colorkey = self.image.get_at((self.size[0] - 1, self.size[1] +1))		
		self.image.set_colorkey(colorkey)

	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))
	
	def update(self):
		engine_part = self.frame / 20
		width, height= 24, 28
		row = engine_part / 4 * height
		col = (engine_part % 4) * width
		engine = self.engines.subsurface((col, row, width, height))

		gap_x, gap_y = 156, 28
		self.image.blit(engine, (gap_x, gap_y))

		self.frame = (self.frame + 1) % 160
		
		d = random.randint(1, 8)
		if d < 5:
			self.x += 2
		else:
			self.x += -2
		self.y += 1


def init():
	width, height = 800,600
	pygame.init()
	return pygame.display.set_mode((width, height))

def main(screen):
	ship = NewShip()
	running = True
	
	while running:
		screen.fill((0,0,0))
		ship.draw(screen)
		ship.update()
		pygame.display.flip()

		for event in pygame.event.get():                      
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                running = False

screen = init()
main(screen)