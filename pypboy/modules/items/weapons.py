import pypboy
import pygame
import game
import config


class Module(pypboy.SubModule):

	label = " Weapons "

	def __init__(self, *args, **kwargs):
		super(Module, self).__init__(*args, **kwargs)
		handlers = []
		for i in config.INVENTORY:
			handlers.add(self.change_items)
		self.menu = pypboy.ui.Menu(100, config.INVENTORY, handlers, 0)
		self.menu.rect[0] = 4
		self.menu.rect[1] = 60
		self.add(self.menu)
		
	def change_items(self):
		print "Changing"