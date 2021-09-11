from engine import *
import random
import math


class MapGenerator:
	def __init__(self, surface, map_size, planets_amt):
		self.surface = surface
		self.map_size = map_size
		self.planets_amt = planets_amt

		self.map_pos = (self.surface.get_width() / 2, self.surface.get_height() / 2)
		self.planets = []

		self.__generate_planets()

	def __generate_planets(self):
		for i in range(self.planets_amt):
			ang = random.uniform(0, 1) * 2 * math.pi
			hyp = math.sqrt(random.uniform(0, 1)) * self.map_size
			adj = math.cos(ang) * hyp
			opp = math.sin(ang) * hyp
	
			self.planets.append((self.map_pos[0] + adj, self.map_pos[1] + opp))


	def generate(self):
		pygame.draw.circle(self.surface, (255, 255, 255), self.map_pos, self.map_size, 1)

		for planet in self.planets:
			pygame.draw.circle(self.surface, (0, 255, 255), planet, 2)

