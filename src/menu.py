from engine import *


class MainMenu:
	def __init__(self, surface, scene_manager):
		self.surface = surface
		self.scene_manager = scene_manager

		# Capping the frame
		self.fps = 60
		self.clock = pygame.time.Clock()

		#Animation stuff
		self.animator = Animator()
		self.frame = 0
		self.planet_image = Spritesheet(os.path.join("../Res/sprites/Earthsprite.png"))
		self.animation = self.animator.load_image(self.planet_image.load_strip([0, 0, 100, 100], 20), 1)

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
				#Fades the screen
				self.FadeEffect(800, 600, 1)

				self.running = False

				# Changing the scene to the game
				self.scene_manager.change_scene("game")
				self.scene_manager.run_scene()

			#Quitting if the button is pressed	
			if self.quitbutton.is_clicked(event):
				self.running = False	
			



	def run(self):
		while self.running:
			self.clock.tick(self.fps)
			self.surface.fill((0, 0, 0))

			self.__event()
			
			#Label and bg stuff
			self.surface.blit(self.background_image, (0, 0))
			self.surface.blit(self.title_image, (10, 200))

			#Buttons
			self.playbutton.draw()
			self.quitbutton.draw()


			#Animation stuff
			self.image = self.animation[self.frame]
			self.image = pygame.transform.scale(self.image, (600,600))
			self.frame += 1
			if self.frame >= len(self.animation):
				self.frame = 0
			self.surface.blit(self.image, (300,200))
				

			pygame.display.update()
	
	#Redraws stuff for faded effect
	def redraw(self):
		self.surface.fill((0, 0, 0))
		#Label and bg stuff
		self.surface.blit(self.background_image, (0, 0))
		self.surface.blit(self.title_image, (10, 200))
		#Buttons
		self.playbutton.draw()
		self.quitbutton.draw()

		#Buttons
		self.playbutton.draw()
		self.quitbutton.draw()

		#Rotating planet
		self.surface.blit(self.image, (300,200))

	#Fade effect function 	
	def FadeEffect(self, width, height, delay):
		self.width = width
		self.height = height
		self.delay = delay
		self.fadeSurface = pygame.Surface((self.width, self.height))
		self.fadeSurface.fill((0,0,0))
		for alpha in range(0,255):
			self.fadeSurface.set_alpha(alpha)
			self.redraw()
			self.surface.blit(self.fadeSurface, (0,0))
			pygame.display.update()
			pygame.time.delay(self.delay)
