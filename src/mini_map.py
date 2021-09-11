from engine import *


class MiniMap:
	def __init__(self, screen, surface, map_generator, player):
		self.screen = screen
		self.surface = surface
		self.map_generator = map_generator
		self.player = player

		self.camera = Camera()

		# Dimensions
		self.pos = [330, 10]
		self.size = [60, 60]
		self.prev_size = self.size.copy()
		self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
	
		# Minimap framework
		self.frame = pygame.Surface(self.size)

		# Opening and closing animations
		self.open_map = False

		self.horizontal_speed = 5.6
		self.vertical_speed = 4

	def __open_map(self):
		self.pos[0] -= self.horizontal_speed
		if self.pos[0] <= 10:
			self.pos[0] = 10

		self.size[0] += self.horizontal_speed
		if self.size[0] >= 380:
			self.size[0] = 380

		self.size[1] += self.vertical_speed
		if self.size[1] >= 280:
			self.size[1] = 280
			
		if self.prev_size != self.size:
			self.frame = pygame.Surface(self.size)
			self.prev_size = self.size.copy()

	def __close_map(self):
		self.pos[0] += self.horizontal_speed
		if self.pos[0] >= 330:
			self.pos[0] = 330

		self.size[0] -= self.horizontal_speed
		if self.size[0] <= 60:
			self.size[0] = 60

		self.size[1] -= self.vertical_speed
		if self.size[1] <= 60:
			self.size[1] = 60

		if self.prev_size != self.size:
			self.frame = pygame.Surface(self.size)
			self.prev_size = self.size.copy()

	def event(self, event):
		mouse_pos = pygame.mouse.get_pos()
		
		# Scalling the mouse pos due to zoom
		ratio_x = (self.screen.get_width() / self.surface.get_width())
		ratio_y = (self.screen.get_height() / self.surface.get_height())
		scaled_pos = (mouse_pos[0] / ratio_x, mouse_pos[1] / ratio_y)
		
		# Toggle of mini map
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_m:
				if self.open_map:
					self.open_map = False
				else:
					self.open_map = True
	
	def __camera(self):
		pos = self.player.pos.copy()
		
		pos[0] = (pos[0] / self.surface.get_width()) * 100
		pos[1] = (pos[1] / self.surface.get_height()) * 100
		
		pos[0] = (pos[0] / 100) * self.size[0]
		pos[1] = (pos[1] / 100) * self.size[1]

		self.camera.follow(pos, self.size)
		pygame.draw.circle(self.frame, (255, 0, 0), (pos[0], pos[1]), 2)

	def draw(self):
		if self.open_map:
			self.__open_map()
		else:
			self.__close_map()

		pygame.draw.rect(self.surface, (255, 255, 255), [self.pos[0]-1, self.pos[1]-1, self.size[0]+2, self.size[1]+2], 1)
	
		self.frame.fill((0, 0, 0))
		
		self.__camera()

		# Rendering the map
		pygame.draw.circle(self.frame, (255, 0, 0), (60/2 - self.camera.pos[0], 60/2 - self.camera.pos[1]), self.map_generator.map_size/2, 1)
		planets = self.map_generator.mini_planets.copy()

		for i in planets:
			i.surface = self.frame
			i.draw(self.camera)

		self.surface.blit(self.frame, (self.pos[0], self.pos[1]))
		
	

