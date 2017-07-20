#coding=utf-8

import collections
import sys

app = False
handlers = collections.OrderedDict()

def register(fn,entry_name = "default"):
	n = fn.__name__

	if entry_name in handlers :
		handlers[entry_name][n] = fn
	else :
		handlers[entry_name] = collections.OrderedDict()
		handlers[entry_name][n] = fn

def import_():
	module_imports = ["sample"]

	for m in module_imports:
		package_module = __name__
		package_name = package_module[0:-8]
		__import__(package_name + m)

def all_handlers(app_):
	entry_name = "default" if len(sys.argv) < 2 else sys.argv[1]
	global app
	app = app_

	if entry_name in handlers :
		for handler_name in handlers[entry_name]:
			handler_fn = handlers[entry_name][handler_name]
			config_item = app.config.handlers[handler_name] if handler_name in app.config.handlers else []
			handler_fn(config_item)		
	else :
		print "No entry defined %s  " % (entry_name)
