#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools


def get_type():
	return "BINARY"

def get_name():
	return "jpeg-compress"

def get_sub_type():
	return "TEST"

def get_desc():
	return "jpeg compressor"

def get_licence():
	return "BSD-2"

def get_compagny_type():
	return "org"

def get_compagny_name():
	return "ijg"

def get_maintainer():
	return "author.txt"

def get_version():
	return "version.txt"

def configure(target, my_module):
	my_module.add_src_file([
	    'jpeg-9b/cjpeg.c',
	    'jpeg-9b/rdppm.c',
	    'jpeg-9b/rdgif.c',
	    'jpeg-9b/rdtarga.c',
	    'jpeg-9b/rdrle.c',
	    'jpeg-9b/rdbmp.c',
	    'jpeg-9b/rdswitch.c',
	    'jpeg-9b/cdjpeg.c',
	    ])
	my_module.add_depend([
	    'jpeg'
	    ])
	return True

