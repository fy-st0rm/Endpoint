from engine import *


class MainMenu:
	def __init__(self, surface, scene_manager):
		self.surface = surface
		self.scene_manager = scene_manager

		self.running = True

		#Menu details asset import
		self.backgroundimage = pygame.image.load(os.path.join("../Res/sprites/backgroundimage.png"))
		self.titleimage = pygame.image.load(os.path.join("../Res/sprites/titleimage.png"))

		#Menu button asset import
		self.buttonnormalimage =  pygame.image.load(os.path.join("../Res/sprites/ui/startnormal.png"))
		self.buttonnonnormalimage =  pygame.image.load(os.path.join("../Res/sprites/ui/startnonnormal.png"))
		self.quitnormalimage = pygame.image.load(os.path.join("../Res/sprites/ui/quitnormal.png"))
		self.quitnonnormalimage = pygame.image.load(os.path.join("../Res/sprites/ui/quitnonnormal.png"))

		#Background and label
		self.background = Image(self.surface,self.backgroundimage, 0,0) 
		self.title = Image(self.surface, self.titleimage, 10, 200)

		#Buttons
		self.playbutton = CustomButton(self.surface, [30,250,184,46], self.buttonnonnormalimage, self.buttonnormalimage) 
		self.quitbutton = CustomButton(self.surface, [30,300,184,46],  self.quitnormalimage, self.quitnonnormalimage)  

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
			self.background.draw()
			self.title.draw()

			#Buttons
			self.playbutton.draw()
			self.quitbutton.draw()
			

			pygame.display.update()
	