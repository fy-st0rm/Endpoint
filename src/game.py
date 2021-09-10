import pygame


#-----------------#
# Main Game Class #
#-----------------#


class Game:
	def __init__(self, surface):
		self.surface = surface
		self.running = True

		# Frames
		self.fps = 60
		self.clock = pygame.time.Clock()

	def __event_handler(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

	def run(self):
		while self.running:
			self.clock.tick(self.fps)

			self.surface.fill((0, 0, 0))

			self.__event_handler()

			pygame.display.update()

