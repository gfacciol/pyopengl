'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_transform_feedback_instanced'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_transform_feedback_instanced',False)

@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLsizei)
def glDrawTransformFeedbackInstanced( mode,id,primcount ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLsizei)
def glDrawTransformFeedbackStreamInstanced( mode,id,stream,primcount ):pass


def glInitTransformFeedbackInstancedARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )