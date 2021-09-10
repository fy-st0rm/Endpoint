from engine import *


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

		# Trying video playing
		self.cut_scene = CutScene(self.surface, "../Res/test.mp4")
		self.cut_scene.play()

	def __event_handler(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.cut_scene.stop()

	def run(self):
		while self.running:
			self.clock.tick(self.fps)

			self.surface.fill((0, 0, 0))

			self.__event_handler()


			pygame.display.update()

