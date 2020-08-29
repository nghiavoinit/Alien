import pygame
'''
class Ship():
	def __init__(self,screen):
		self.screen=screen
		self.image =pygame.image.load('ship.bmp')
		self.image=pygame.transform.scale(self.image,(48,48))
		self.rect= self.image.get_rect()
		self.screen_rect=screen.get_rect()
		
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)

'''
class Ship():
	def __init__(self,setting,screen):
		self.screen=screen
		self.image=pygame.image.load('ship.bmp')
		self.size=(50,50)
		self.image=pygame.transform.scale(self.image,self.size)
		
	
		self.rect=self.image.get_rect()
		self.screen_rect= self.screen.get_rect()

		self.rect.centerx=float(self.screen_rect.centerx)
		self.rect.bottom=float(self.screen_rect.bottom)
	
		
		self.movingR=False
		self.movingL=False
		self.movingU=False
		self.movingD=False
		self.speedUp=False
		self.speedDown=False

		self.setting=setting
		
	def update(self):

		if self.movingR:
			self.rect.centerx =self.rect.centerx + self.setting.speed
		if self.movingL:
			self.rect.centerx -=self.setting.speed
		if self.movingU:
			self.rect.bottom -=self.setting.speed
		if self.movingD:
			self.rect.bottom+=self.setting.speed
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)
