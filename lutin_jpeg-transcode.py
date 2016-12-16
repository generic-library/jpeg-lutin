#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools


def get_type():
	return "BINARY"

def get_name():
	return "jpeg-trancode"

def get_sub_type():
	return "TEST"

def get_desc():
	return "jpeg transcode"

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
	    'jpeg-9b/jpegtran.c',
	    'jpeg-9b/transupp.c',
	    
	    'jpeg-9b/cdjpeg.c',
	    'jpeg-9b/wrppm.c',
	    'jpeg-9b/wrgif.c',
	    'jpeg-9b/wrtarga.c',
	    'jpeg-9b/wrrle.c',
	    'jpeg-9b/wrbmp.c',
	    'jpeg-9b/rdcolmap.c',
	    
	    'jpeg-9b/rdppm.c',
	    'jpeg-9b/rdgif.c',
	    'jpeg-9b/rdtarga.c',
	    'jpeg-9b/rdrle.c',
	    'jpeg-9b/rdbmp.c',
	    'jpeg-9b/rdswitch.c',
	    ])
	my_module.add_header_file([
	    'jpeg-9b/transupp.h',
	    ])
	my_module.add_depend([
	    'jpeg'
	    ])
	return True

