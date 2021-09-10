
class Camera:
	def __init__(self, surface):
		self.pos = [0, 0]
		self.surface = surface

	def follow(self, entity):
		self.pos[0] += (entity.pos[0] - self.pos[0] - self.surface.get_width() / 2) / 10
		self.pos[1] += (entity.pos[1] - self.pos[1] - self.surface.get_height() / 2) / 10

