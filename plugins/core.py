#coding=utf-8

plugins = {}

def register(name):
	def register_(c):
		if name in plugins:
			plugins[name].append(c)	
		else :
			plugins[name] = [c]
	return register_

def run_plugin(name,params):
	if name in plugins:
		pls = plugins[name]
		for p in pls:
			p(params)

def import_(fn = False):
	module_imports = ["sample"]

	for m in module_imports:
		package_module = __name__
		package_name = package_module[0:-4]
		__import__(package_name + m)

	if fn != False:
		fn()


