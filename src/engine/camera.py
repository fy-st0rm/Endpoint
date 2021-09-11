
class Camera:
	def __init__(self):
		self.pos = [0, 0]

	def follow(self, pos, size):
		self.pos[0] += (pos[0] - self.pos[0] - size[0] / 2) / 10
		self.pos[1] += (pos[1] - self.pos[1] - size[1] / 2) / 10

