from engine import *


class MainMenu:
	def __init__(self, surface, scene_manager):
		self.surface = surface
		self.scene_manager = scene_manager

		self.running = True

		#Menu details asset import
		self.background_image = pygame.image.load(os.path.join("../Res/sprites/backgroundimage.png"))
		self.title_image = pygame.image.load(os.path.join("../Res/sprites/titleimage.png"))

		#Menu button asset import
		self.button_sprites = Spritesheet(os.path.join("../Res/sprites/ui/buttons.png"))

		self.play_buttons = self.button_sprites.load_strip([362, 0, 181, 47], 2)		
		self.quit_buttons = self.button_sprites.load_strip([0, 0, 181, 47], 2)
	
		#Buttons
		self.playbutton = CustomButton(self.surface, [30,250,184,46], self.play_buttons[0], self.play_buttons[1]) 
		self.quitbutton = CustomButton(self.surface, [30,300,184,46],  self.quit_buttons[1], self.quit_buttons[0])  

	def __event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

			if self.playbutton.is_clicked(event):
				self.running = False

				# Changing the scene to the game
				self.scene_manager.change_scene("game")
				self.scene_manager.run_scene()

			#Quitting if the button is pressed	
			if self.quitbutton.is_clicked(event):
				self.running = False	
	

	def run(self):
		while self.running:
			self.surface.fill((0, 0, 0))

			self.__event()
			
			#Label and bg stuff
			self.surface.blit(self.background_image, (0, 0))
			self.surface.blit(self.title_image, (10, 200))

			#Buttons
			self.playbutton.draw()
			self.quitbutton.draw()
			

			pygame.display.update()
	
