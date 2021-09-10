import pygame


#---------------#
# Text Renderer #
#---------------#

class Text:
	def __init__(self, surface, font, text, color):
		self.surface = surface
		self.font = font
		self.text = text
		self.color = color
		
		self.texture = self.font.render(self.text, True, self.color)
		self.rect = self.texture.get_rect()

	def get_rect(self):
		return self.rect

	def set_center(self, point):
		rect = self.texture.get_rect(center=point)
		self.surface.blit(self.texture, rect)

	def draw(self, x, y):
		self.surface.blit(self.texture, (x, y))



#----------------#
# Default Button #
#----------------#

class Button:
	def __init__(self, surface, rect, active_color, inactive_color, text, font):
		self.surface = surface
		self.rect = pygame.Rect(rect)
		self.active_color = active_color
		self.inactive_color = inactive_color
		self.text = text
		self.font = font
		
		self.color = self.inactive_color
		self.active = False

	def is_clicked(self, event):
		if self.active:
			if event.type == pygame.MOUSEBUTTONDOWN:
				if pygame.mouse.get_pressed()[0]:
					return True
		return False

	def draw(self):
		mouse_pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(mouse_pos):
			self.color = self.active_color
			self.active = True
		else:
			self.color = self.inactive_color
			self.active = False

		# Rendering the rectangle
		pygame.draw.rect(self.surface, self.color, self.rect, 2)
		
		# Rendering text
		text = Text(self.surface, self.font, self.text, self.color)
	
		x = self.rect.x + (self.rect.width/2 - text.get_rect().width/2)
		y = self.rect.y + (self.rect.height/2 - text.get_rect().height/2)

		text.draw(x, y)


#---------------#
# Custom Button #
#---------------#

class CustomButton:
	def __init__(self, surface, rect, active_image, inactive_image):
		self.surface = surface
		self.rect = pygame.Rect(rect)
		self.active_image = active_image
		self.inactive_image = inactive_image

		self.image = self.inactive_image
		self.active = False

	def is_clicked(self, event):
		if self.active:
			if event.type == pygame.MOUSEBUTTONDOWN:
				if pygame.mouse.get_pressed()[0]:
					return True
		return False
	
	def draw(self):
		mouse_pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(mouse_pos):
			self.image = self.active_image
			self.active = True
		else:
			self.image = self.inactive_image
			self.active = False

		# Drawing the image
		self.surface.blit(self.image, (self.rect.x, self.rect.y))

#---------------#
# Imageloading  #
#---------------#

class Image:
	def __init__(self,surface, image, imagex, imagey):
		self.surface = surface
		self.image = image
		self.imagex = imagex
		self.imagey = imagey

	def draw(self):
		self.surface.blit(self.image, (self.imagex, self.imagey))	