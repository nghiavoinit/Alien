import sys
import pygame
from settings import Settings
from ship import Ship
from monster import Monster
import function
from pygame.sprite import Group,Sprite
def run_game():
	pygame.init()
	sett=Settings()

	screen=pygame.display.set_mode((sett.screen_width,sett.screen_height))
	pygame.display.set_caption('Alien Invasion')
	bg_color=(230,30,230)

	ship=Ship(sett,screen)
	monster=Monster(sett,screen)
	
	bullets = Group()
	monsters= Group()
	time=0
	score=0
	while True:
		
		function.check_event(sett,ship,screen,bullets)
		ship.update()
		bullets.update()
		for bullet in bullets.copy():
			if bullet.rectb.bottom<=0:
				bullets.remove(bullet)

		#print(len(bullets))
			
		
		#for bullet in bullets.copy():
		#	if bullet.rect.bottom
		monsters.update()
		'''for mons in monsters.copy():
			if mons.rectm.bottom>=800:
				monsters.remove(mons)
		'''	
			
		function.removem(monsters,bullets,ship,score)
		
		function.update_screen(sett,ship,screen,bullets,monsters,monster,time)
		time+=1
	return score

run_game()
