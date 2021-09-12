from moviepy.editor import *


class CutScene:
	def __init__(self, surface, video):
		self.video = video
		self.clip = VideoFileClip(self.video).resize((surface.get_width(), surface.get_height()))
	
	def stop(self):
		del self.clip.reader
		del self.clip

	def play(self):
		self.clip.preview()	
