#!/usr/bin/python
import realog.debug as debug
import lutin.tools as tools


def get_type():
	return "BINARY"

def get_name():
	return "jpeg-decompress"

def get_sub_type():
	return "TEST"

def get_desc():
	return "jpeg decompressor"

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
	    'jpeg-9b/cdjpeg.c',
	    'jpeg-9b/djpeg.c',
	    'jpeg-9b/wrppm.c',
	    'jpeg-9b/wrgif.c',
	    'jpeg-9b/wrtarga.c',
	    'jpeg-9b/wrrle.c',
	    'jpeg-9b/wrbmp.c',
	    'jpeg-9b/rdcolmap.c',
	    ])
	my_module.add_depend([
	    'jpeg'
	    ])
	return True

