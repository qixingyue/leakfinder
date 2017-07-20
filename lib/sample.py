#coding=utf-8

import handlers

@handlers.register
def sample_hello(config_):
	plugin_ = handlers.app.run_plugin("sample",[1,2,3])
	print config_
	
