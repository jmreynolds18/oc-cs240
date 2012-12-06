
import pygame
class Hero(object):
	def __init__(self):
		self.image = pygame.image.load('chgirl.png').convert_alpha()
		self.x = 60
		self.y = 100
		self.bullets = [[130, 200], [150, 200]]
		
	
	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))
		for bullet in self.bullets:
			pygame.draw.circle(screen, (255,255,255), (bullet[0], bullet[1]), 6)

	def update(self):
		self.y += 1
		for bullet in self.bullets:
			bullet[0] += 1
		self.y += 1
		if self.y % 100 == 0:
			self.bullets.append([130, self.y])
			self.bullets.append([150, self.y])
			self.bullets.append([170, self.y])


def init():
	width, height = 800,600
	pygame.init()
	return pygame.display.set_mode((width, height))

def main(screen):
	hero = Hero()
	running = True
	
	while running:
		screen.fill((0,0,0))
		hero.draw(screen)
		pygame.display.flip()
		hero.update
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
				running = False

		
		

screen = init()
main(screen)
