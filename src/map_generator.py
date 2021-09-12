from engine import *
import random
import math

#------------------#
# Planet structure #
#------------------#

class Planet:
	def __init__(self, surface, sprite, pos, size, color):
		self.surface = surface
		self.sprite = sprite
		self.pos = pos
		self.size = size
		self.color = color

		self.pos_info = self.pos.copy()

		self.__generate_planets_info()

	def __generate_planets_info(self):
		
		# Climates cases according to the color of the planet
		self.climates = {
			"blue": random.choices(["cold", "temp"], weights=[0.5, 0.5], k=1),
			"green": ["temp"],
			"red": random.choices(["hot", "dry"], weights=[0.5, 0.5], k=1),
			"purple": random.choices(["cold", "temp", "dry"], weights=[0.3, 0.4, 0.3], k=1)
		}
		
		# Life form cases according to climatic conditions
		self.life_form = {
			"cold": [False],
			"temp": [True],
			"hot" : [False],
			"dry" : random.choices([True, False], weights=[0.3, 0.7], k=1)
		}

		self.climate = self.climates[self.color][0]	
		self.life = self.life_form[self.climate][0]

	def draw(self, camera):	
		self.surface.blit(pygame.transform.scale(self.sprite, self.size), (self.pos[0] - camera.pos[0], self.pos[1] - camera.pos[1]))


#------------------------#
# Map generation handler #
#------------------------#

class MapGenerator:
	def __init__(self, surface, camera, map_size, planets_amt):
		self.surface = surface
		self.camera = camera
		self.map_size = map_size
		self.planets_amt = planets_amt

		# Map memories
		self.map_pos = (self.surface.get_width() / 2, self.surface.get_height() / 2)
		self.planets = []
		self.mini_planets = []

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
			a   = random.uniform(0, 1)
			b   = random.uniform(0, 1)

			ang = a * 2 * math.pi
			hyp = math.sqrt(b) * self.map_size
			hyp_mini = math.sqrt(b) * self.map_size/2

			adj = math.cos(ang) * hyp
			opp = math.sin(ang) * hyp

			adj_mini = math.cos(ang) * hyp_mini
			opp_mini = math.sin(ang) * hyp_mini

			pos = [self.map_pos[0] + adj, self.map_pos[1] + opp]
			pos_mini = [adj_mini, opp_mini]

			# Generating planets color
			color = random.choice(self.colors)
			sprite = self.sprites[color]
			
			# Generating new planet instants
			new_planet = Planet(self.surface, sprite, pos, (20, 20), color)
			mini_planet = Planet(self.surface,sprite, pos_mini, (10, 10), color)

			self.planets.append(new_planet)
			self.mini_planets.append(mini_planet)


	def generate(self):
		pygame.draw.circle(self.surface, (255, 255, 255), (self.map_pos[0] - self.camera.pos[0], self.map_pos[1] - self.camera.pos[1]), self.map_size, 1)
		
		#[TODO] Render the only visible planets
		for planet in self.planets:
			planet.draw(self.camera)
