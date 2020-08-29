''' A class to store all settings for Alien Invasion '''
import random
class Settings():
	def __init__(self):
		self.screen_width=1200
		self.screen_height=800
		self.bg_color=(230,230,230)
		self.speed=float(1.0)

		#bullet
		self.bullet_speed=2
		self.bullet_width=15
		self.bullet_height=15
		self.bullet_color=(60,60,60)
		self.appearb=False

		#monster
		self.monster_range=random.randint(100,1100)
		self.monster_speed=1
		self.appearm=False
