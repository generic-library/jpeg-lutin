#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os


def get_type():
	return "LIBRARY"

def get_desc():
	return "JPEG 2000 reade writer"

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
	    'jpeg-9b/jaricom.c',
	    'jpeg-9b/jcapimin.c',
	    'jpeg-9b/jcapistd.c',
	    'jpeg-9b/jcarith.c',
	    'jpeg-9b/jccoefct.c',
	    'jpeg-9b/jccolor.c',
	    'jpeg-9b/jcdctmgr.c',
	    'jpeg-9b/jchuff.c',
	    'jpeg-9b/jcinit.c',
	    'jpeg-9b/jcmainct.c',
	    'jpeg-9b/jcmarker.c',
	    'jpeg-9b/jcmaster.c',
	    'jpeg-9b/jcomapi.c',
	    'jpeg-9b/jcparam.c',
	    'jpeg-9b/jcprepct.c',
	    'jpeg-9b/jcsample.c',
	    'jpeg-9b/jctrans.c',
	    'jpeg-9b/jdapimin.c',
	    'jpeg-9b/jdapistd.c',
	    'jpeg-9b/jdarith.c',
	    'jpeg-9b/jdatadst.c',
	    'jpeg-9b/jdatasrc.c',
	    'jpeg-9b/jdcoefct.c',
	    'jpeg-9b/jdcolor.c',
	    'jpeg-9b/jddctmgr.c',
	    'jpeg-9b/jdhuff.c',
	    'jpeg-9b/jdinput.c',
	    'jpeg-9b/jdmainct.c',
	    'jpeg-9b/jdmarker.c',
	    'jpeg-9b/jdmaster.c',
	    'jpeg-9b/jdmerge.c',
	    'jpeg-9b/jdpostct.c',
	    'jpeg-9b/jdsample.c',
	    'jpeg-9b/jdtrans.c',
	    'jpeg-9b/jerror.c',
	    'jpeg-9b/jfdctflt.c',
	    'jpeg-9b/jfdctfst.c',
	    'jpeg-9b/jfdctint.c',
	    'jpeg-9b/jidctflt.c',
	    'jpeg-9b/jidctfst.c',
	    'jpeg-9b/jidctint.c',
	    'jpeg-9b/jquant1.c',
	    'jpeg-9b/jquant2.c',
	    'jpeg-9b/jutils.c',
	    'jpeg-9b/jmemmgr.c',
	    'jpeg-9b/jmemnobs.c',
	    ])
	
	#    'jpeg-9b/jmemansi.c',
	#    'jpeg-9b/jmemname.c',
	# specific mac file 'jpeg-9b/jmemmac.c',
	# specific dos file 'jpeg-9b/jmemdos.c',
	"""
	my_module.add_flag('c', [
	    '-DMUTEX_pthread',
	    '-Dopenjp2_EXPORTS'
	    ])
	"""
	my_module.compile_version("c", 1999)
	my_module.add_depend([
	    'z',
	    'm',
	    ])
	my_module.add_header_file([
	    'jpeg-9b/jmorecfg.h',
	    'jpeg-9b/cderror.h',
	    'jpeg-9b/jpeglib.h',
	    'jpeg-9b/jmemsys.h',
	    'jpeg-9b/jversion.h',
	    'jpeg-9b/cdjpeg.h',
	    'jpeg-9b/jinclude.h',
	    'jpeg-9b/jdct.h',
	    'jpeg-9b/jpegint.h',
	    'jpeg-9b/jerror.h',
	    'generated/jconfig.h',
	    ],
	    destination_path="")
	return True

