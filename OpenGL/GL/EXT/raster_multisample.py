'''OpenGL extension EXT.raster_multisample

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.raster_multisample to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/raster_multisample.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.EXT.raster_multisample import *
from OpenGL.raw.GL.EXT.raster_multisample import _EXTENSION_NAME

def glInitRasterMultisampleEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION