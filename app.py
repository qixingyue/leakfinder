#coding=utf-8

import lib
import config
from plugins import run_plugin , import_

class App:

	def __init__(self):
		self.run_plugin = run_plugin
		self.config = config
		lib.all_handlers(self)

if __name__ == "__main__":
	import_()	
	App()
