import pygame, sys, random

class particles:
	#-----------------#
	# particle Handler#
	#-----------------#
	def __init__(self,surface, x, y, color, gravity, strength):
		self.surface = surface
		self.x = x
		self.y = y
		self.color = color
		self.gravity = bool(gravity)
		self.gravity_strength = strength
		self.particles = []

	def emmit(self):
		self.particles.append([[self.x,self.y],[random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6)])

		for particle in self.particles:
			particle[0][0] += particle[1][0]
			particle[0][1] += particle[1][1]
			particle[2] -= 0.1
			if self.gravity == True:
				particle[1][1] += self.gravity_strength

			# Draws Circle as particles
			pygame.draw.circle(self.surface, self.color, [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
			if particle[2] <= 0:
				self.particles.remove(particle)
