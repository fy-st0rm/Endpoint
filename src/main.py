from menu import *
from game import *


class SceneManager:
	def __init__(self):
		self.scene = None

	def change_scene(self, scene_name):
		if scene_name == "main_menu":
			self.scene = MainMenu(screen, self)
		elif scene_name == "game":
			self.scene = Game(screen, self)

	def run_scene(self):
		if self.scene:
			self.scene.run()
		else:
			print("Scene not selected")


if __name__ == "__main__":
	pygame.init()

	WIN_SIZE = (800, 600)
	screen = pygame.display.set_mode(WIN_SIZE)

	scene_manager = SceneManager()
	scene_manager.change_scene("main_menu")
	scene_manager.run_scene()


