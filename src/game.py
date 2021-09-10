from engine import *
from entity.player import *

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

		self.camera = Camera(self.display)
		self.player = Player(self.display, [100, 100], self.camera)

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

			self.display.fill((0, 0, 0))

			self.__event_handler()
		
			self.camera.follow(self.player)
			self.player.draw()
			
			pygame.draw.rect(self.display, (255, 0, 0), [100 - self.camera.pos[0], 100 - self.camera.pos[1], 30, 30]) 

			self.surface.blit(pygame.transform.scale(self.display, (self.surface.get_width(), self.surface.get_height())), (0, 0))
			pygame.display.update()

