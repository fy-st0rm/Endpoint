from engine import *
from entity.player import *

#-----------------#
# Main Game Class #
#-----------------#

class Game:
	def __init__(self, surface, scene_manager):
		self.surface = surface
		self.scene_manager = scene_manager
		self.running = True

		# Frames
		self.fps = 60
		self.clock = pygame.time.Clock()

		self.player = Player(self.surface, [100, 100])

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
	
			self.player.event(event)

	def run(self):
		while self.running:
			self.clock.tick(self.fps)

			self.surface.fill((0, 0, 0))

			self.__event_handler()
		
			self.player.draw()

			pygame.display.update()

