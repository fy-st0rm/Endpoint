from engine import *
import random
import math



class Planet:
	def __init__(self, surface, sprite, pos, color):
		self.surface = surface
		self.sprite = sprite
		self.pos = pos
		self.color = color

		self.__generate_planets_info()

		print(self.color, self.climate, self.life)

	def __generate_planets_info(self):
		self.climates = {
			"blue": random.choices(["cold", "temp"], weights=[0.5, 0.5], k=1),
			"green": ["temp"],
			"red": random.choices(["hot", "dry"], weights=[0.5, 0.5], k=1),
			"purple": random.choices(["cold", "temp", "dry"], weights=[0.3, 0.4, 0.3], k=1)
		}

		self.life_form = {
			"cold": [False],
			"temp": [True],
			"hot" : [False],
			"dry" : random.choices([True, False], weights=[0.3, 0.7], k=1)
		}

		self.climate = self.climates[self.color][0]	
		self.life = self.life_form[self.climate][0]

	def draw(self):	
		self.surface.blit(pygame.transform.scale(self.sprite, (10, 10)), self.pos)


class MapGenerator:
	def __init__(self, surface, map_size, planets_amt):
		self.surface = surface
		self.map_size = map_size
		self.planets_amt = planets_amt

		# Map memories
		self.map_pos = (self.surface.get_width() / 2, self.surface.get_height() / 2)
		self.planets = []

		# Planet colors
		self.colors = ["blue", "green", "purple", "red"]

		# Planet sprites
		self.planet_sprites = Spritesheet(os.path.join("../Res/sprites/planets.png"))
		self.sprites = {
			"blue": self.planet_sprites.load_image(0, 0, 100, 100),
			"green": self.planet_sprites.load_image(1, 0, 100, 100),
			"purple": self.planet_sprites.load_image(2, 0, 100, 100),
			"red": self.planet_sprites.load_image(3, 0, 100, 100)
		}

		self.__generate_planets()

	def __generate_planets(self):
		for i in range(self.planets_amt):
			
			# Calculating position
			ang = random.uniform(0, 1) * 2 * math.pi
			hyp = math.sqrt(random.uniform(0, 1)) * self.map_size
			adj = math.cos(ang) * hyp
			opp = math.sin(ang) * hyp
			
			pos = (self.map_pos[0] + adj, self.map_pos[1] + opp)

			# Generating planets color
			color = random.choice(self.colors)
			sprite = self.sprites[color]
			
			# Generating new planet instants
			new_planet = Planet(self.surface, sprite, pos, color)

			self.planets.append(new_planet)


	def generate(self):
		pygame.draw.circle(self.surface, (255, 255, 255), self.map_pos, self.map_size, 1)

		for planet in self.planets:
			planet.draw()
