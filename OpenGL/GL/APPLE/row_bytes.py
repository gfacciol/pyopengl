'''OpenGL extension APPLE.row_bytes

This module customises the behaviour of the 
OpenGL.raw.GL.APPLE.row_bytes to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.APPLE.row_bytes import *
### END AUTOGENERATED SECTION