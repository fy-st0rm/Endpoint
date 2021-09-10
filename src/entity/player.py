from engine import *
import os


class Player:
	def __init__(self, surface, pos, camera):
		self.surface = surface
		self.pos = pos
		self.camera = camera
		
		self.player_sprite = Spritesheet(os.path.join("../Res/sprites/player.png"))
		self.player_size = [32, 32]

		# Player animations
		self.animator = Animator()
		self.animation_tree = {
			"idle": {
				"left": self.player_sprite.load_strip([0, 32, self.player_size[0], self.player_size[1]], 1),
				"right": self.player_sprite.load_strip([0, 0, self.player_size[0], self.player_size[1]], 1),
				"up": self.player_sprite.load_strip([0, 64, self.player_size[0], self.player_size[1]], 1),
				"down": self.player_sprite.load_strip([0, 96, self.player_size[0], self.player_size[1]], 1)
			},

			"walk":	{
				"left": self.animator.load_image(self.player_sprite.load_strip([0, 32, self.player_size[0], self.player_size[1]], 3), 1),
				"right": self.animator.load_image(self.player_sprite.load_strip([0, 0, self.player_size[0], self.player_size[1]], 3), 1),
				"up":  self.animator.load_image(self.player_sprite.load_strip([0, 64, self.player_size[0], self.player_size[1]], 3), 1),
				"down":  self.animator.load_image(self.player_sprite.load_strip([0, 96, self.player_size[0], self.player_size[1]], 3), 1)
			}
		}

		# Player states
		self.side = "right"
		self.state = "idle"
		self.frame = 0

		# Movements
		self.speed = 3
		self.left = False
		self.right = False
		self.up = False
		self.down = False

	def event(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				self.left = True
			if event.key == pygame.K_d:
				self.right = True
			if event.key == pygame.K_w:
				self.up = True
			if event.key == pygame.K_s:
				self.down = True

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				self.left = False
			if event.key == pygame.K_d:
				self.right = False
			if event.key == pygame.K_w:
				self.up = False
			if event.key == pygame.K_s:
				self.down = False

	def __update(self):
		if self.left:
			self.side = "left"
			self.state = "walk"

			self.pos[0] -= self.speed

		if self.right:
			self.side = "right"
			self.state = "walk"

			self.pos[0] += self.speed

		if self.up:
			self.side = "up"
			self.state = "walk"

			self.pos[1] -= self.speed

		if self.down:
			self.side = "down"
			self.state = "walk"

			self.pos[1] += self.speed

		if not self.left and not self.right and not self.up and not self.down:
			self.state = "idle"

	def draw(self):
		self.__update()

		self.current_animation = self.animation_tree[self.state][self.side]
		
		# Incrementing the frame
		self.frame += 1
		if self.frame >= len(self.current_animation):
			self.frame = 0

		image = self.current_animation[self.frame]
		self.surface.blit(image, (self.pos[0] - self.camera.pos[0], self.pos[1] - self.camera.pos[1]))

