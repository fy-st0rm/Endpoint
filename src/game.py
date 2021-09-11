from engine import *
from entity.player import *
from map_generator import *
from mini_map import *

#-----------------#
# Main Game Class #
#-----------------#

class Game:
	def __init__(self, surface, display, scene_manager):
		self.surface = surface
		self.display = display
		self.scene_manager = scene_manager
		self.running = True

		# Frames
		self.fps = 60
		self.clock = pygame.time.Clock()

		self.camera = Camera()
		self.player = Player(self.display, [self.display.get_width()/2, self.display.get_height()/2], self.camera)

		# Map generations
		self.map_generator = MapGenerator(self.display, self.camera, 150, 25)

		self.mini_map = MiniMap(self.surface, self.display, self.map_generator, self.player, self.camera)
	
	def __event_handler(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.running = False

					# Changing the scene to main menu
					self.scene_manager.change_scene("main_menu")
					self.scene_manager.run_scene()
	
			self.mini_map.event(event)
			self.player.event(event)

	def run(self):
		while self.running:
			self.clock.tick(self.fps)

			self.display.fill((0, 0, 0))

			self.__event_handler()

			self.camera.follow(self.player.pos, [self.display.get_width(), self.display.get_height()])

			self.map_generator.generate()
			self.mini_map.draw()

			self.player.draw()
			
			self.surface.blit(pygame.transform.scale(self.display, (self.surface.get_width(), self.surface.get_height())), (0, 0))
			pygame.display.update()

