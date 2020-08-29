import sys
import pygame
from bullet import Bullet
from monster import Monster
from ship import Ship
def check_event(sett,ship,screen,bullets):
	for event in pygame.event.get():
		
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_RIGHT:
				ship.movingR=True
				
			elif event.key==pygame.K_LEFT:
				ship.movingL=True
				
			elif event.key==pygame.K_UP:
				ship.movingU=True
				
			elif event.key==pygame.K_DOWN:
				ship.movingD=True
			elif event.key==pygame.K_q:
				if sett.speed<5:
					sett.speed +=0.5
			elif event.key==pygame.K_w:
				if sett.speed>1:				
					sett.speed -=0.5

			if event.key==pygame.K_SPACE:
				
				sett.appearb=True
				
				
			
			

		elif event.type==pygame.KEYUP:
			if event.key==pygame.K_RIGHT:
				ship.movingR=False
				
			elif event.key==pygame.K_LEFT:
				ship.movingL=False
				
			elif event.key==pygame.K_UP:
				ship.movingU=False
				
			elif event.key==pygame.K_DOWN:
				ship.movingD=False
			if event.key==pygame.K_SPACE:
				sett.appearb=False

def update_screen(sett,ship,screen,bullets,monsters,monster,time):
	
	screen.fill(sett.bg_color)
	if sett.appearb:
		new_bullet=Bullet(sett,screen,ship)
		if time%10==0:
			bullets.add(new_bullet)
	for bullet in bullets.sprites():
		bullet.draw()
		'''
	new_bullet=Bullet(sett,screen,ship)
	if appear(sett.appearb,new_bullet,bullets)
		bullet.draw()'''
	
	if time%100==0:
		new_monster=Monster(sett,screen)
		monsters.add(new_monster)
	for mons in monsters.sprites():	
		mons.blitme()
	ship.blitme()
	pygame.display.flip()


"""def appear(appear,obj,groups):
	# appear:t/f    # group: list of object
	#obj: new objects create from class
	i=0
	if appear:
		groups.add(obj)
	for obj in groups.sprites():
		i+=1
		if i%10==0:
			obj.draw()
"""	
def removem(objl,objl1,ship,score):
	
	for mons in objl.copy():
		if mons.rectm.bottom>=800:
			objl.remove(mons)
		area=mons.rectm.centerx
		score=score+1
		
		if mons.rectm.bottom== ship.rect.bottom:
			if int(ship.rect.centerx) in range(area-24,area+24):
				print(score)
				sys.exit()
		for bull in objl1.copy():
			
			if bull.rectb.bottom==mons.rectm.bottom:
				if bull.rectb.centerx in range(area-48,area+48):
					objl.remove(mons)
					objl1.remove(bull)
					print('+1')
					score=score+1
					print(score)
	return score
	
