import pygame
from pygame.sprite import Sprite
import random

class Monster(Sprite):
	def __init__(self,sett,screen):
		super(Monster,self).__init__()
		self.screen=screen
		self.monster=pygame.image.load('mons.bmp')
		self.monster=pygame.transform.scale(self.monster,(48,48))
		self.rectm=self.monster.get_rect()
		self.rect_screen=self.screen.get_rect()
	



		self.rectm.centerx=random.randint(100,1100)
		self.rectm.bottom=100
		self.range1=(int(self.rectm.centerx-24),int(self.rectm.centerx+24))
		self.speed=sett.monster_speed
		#self.range=sett.monster_range
	def update(self):
		self.rectm.y +=self.speed
	def blitme(self):
		self.screen.blit(self.monster,self.rectm)
	
	
		
