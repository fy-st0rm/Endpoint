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

		# Engine test things
		self.font = pygame.font.SysFont("Consolas", 32)

		self.button = Button(self.surface, [200, 200, 300, 80], (255, 255, 255), (165, 165, 165), "Click Me!", self.font)

	def __event_handler(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

			if self.button.is_clicked(event):
				print("Clicked")

	def run(self):
		while self.running:
			self.clock.tick(self.fps)

			self.surface.fill((0, 0, 0))

			self.__event_handler()

			# Engine tests
			text = Text(self.surface, self.font, "Hello World", (255, 255, 255))
			text.draw(100, 100)

			self.button.draw()

			pygame.display.update()

