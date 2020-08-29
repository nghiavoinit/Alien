import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self,sett,screen,ship):
		super(Bullet,self).__init__()
		self.screen=screen
		
		self.rectb=pygame.Rect(0,0,sett.bullet_width,sett.bullet_height)
		self.rectb.centerx=ship.rect.centerx
		self.rectb.bottom=ship.rect.top
		
		#self.stop=False
		
		self.color=sett.bullet_color
		self.speed=sett.bullet_speed
	def update(self):
		self.rectb.y-=self.speed
		
	def draw(self):
		pygame.draw.rect(self.screen,self.color,self.rectb)

