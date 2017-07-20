#coding=utf-8

import core

@core.register("sample")
def one_simple(args):
	print "this is simple world"
	print args
