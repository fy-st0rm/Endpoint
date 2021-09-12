import pygame
import os
from engine import*

class Inventory:
	def __init__(self, surface, darkcrystal_ammount, fuel_ammount):

		self.surface = surface
		self.colorDark = (92, 89, 112)
		self.colorFuel = (168, 134, 200)
		self.colorLight = (255, 255, 255)

		self.darkcrystal_ammount = darkcrystal_ammount
		self.fuel_ammount = fuel_ammount

		self.darkcrystal_maxcapacity = 50
		self.fuel_maxcapacity = 300


		self.font = pygame.font.SysFont("../Res/Font/FFFFORWA.ttf", 20)

		#Importing 
		self.resources_image = Spritesheet(os.path.join("../Res/sprites/resources.png"))

		self.darkcrystal_image = self.resources_image.load_strip([0,0,30,30],1)
		self.fuel_image = self.resources_image.load_strip([30,0,30,30],1)

		self.darkcrystal_image[0] = pygame.transform.scale(self.darkcrystal_image[0], (20,20))
		self.fuel_image[0] = pygame.transform.scale(self.fuel_image[0], (20,20))

		self.controls_text = Text(self.surface, self.font, "[M] MAP", self.colorLight)
		#self.fuel_image_rect = pygame.rect((0,20,20,10))


	def draw(self):
		self.darkcrystal_bar = self.darkcrystal_ammount/self.darkcrystal_maxcapacity * 50
		self.fuel_bar = self.fuel_ammount/self.fuel_maxcapacity * 50

		pygame.draw.rect(self.surface, self.colorLight, pygame.Rect((0,0,50,10)))
		pygame.draw.rect(self.surface, self.colorLight, pygame.Rect((0,20,50,10)))

		pygame.draw.rect(self.surface, self.colorDark, pygame.Rect((0,0,self.darkcrystal_bar,10)))
		pygame.draw.rect(self.surface, self.colorFuel, pygame.Rect((0,20,self.fuel_bar,10)))
		self.surface.blit(self.darkcrystal_image[0], (0,0))	
		self.surface.blit(self.fuel_image[0], (0,20))

		self.controls_text.draw(0,270)




