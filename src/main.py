from game import *


if __name__ == "__main__":
	pygame.init()

	WIN_SIZE = (800, 600)

	screen = pygame.display.set_mode(WIN_SIZE)

	game = Game(screen)
	game.run()

