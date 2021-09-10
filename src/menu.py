from engine import *


class MainMenu:
	def __init__(self, surface, scene_manager):
		self.surface = surface
		self.scene_manager = scene_manager

		self.running = True

		# Buttons
		self.font = pygame.font.SysFont("consolas", 32)
		self.button = Button(self.surface, [200, 200, 300, 50], (255, 255, 255), (165, 165, 165), "PLAY", self.font)

	def __event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

			if self.button.is_clicked(event):
				self.running = False

				# Changing the scene to the game
				self.scene_manager.change_scene("game")
				self.scene_manager.run_scene()

	def run(self):
		while self.running:
			self.surface.fill((0, 0, 0))

			self.__event()
			
			self.button.draw()

			pygame.display.update()
