'''OpenGL extension ARB.imaging_DEPRECATED

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/ARB/imaging_DEPRECATED.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_imaging'
GL_CONVOLUTION_1D = constant.Constant( 'GL_CONVOLUTION_1D', 0x8010 )
GL_CONVOLUTION_2D = constant.Constant( 'GL_CONVOLUTION_2D', 0x8011 )
GL_SEPARABLE_2D = constant.Constant( 'GL_SEPARABLE_2D', 0x8012 )
GL_CONVOLUTION_BORDER_MODE = constant.Constant( 'GL_CONVOLUTION_BORDER_MODE', 0x8013 )
GL_CONVOLUTION_FILTER_SCALE = constant.Constant( 'GL_CONVOLUTION_FILTER_SCALE', 0x8014 )
GL_CONVOLUTION_FILTER_BIAS = constant.Constant( 'GL_CONVOLUTION_FILTER_BIAS', 0x8015 )
GL_REDUCE = constant.Constant( 'GL_REDUCE', 0x8016 )
GL_CONVOLUTION_FORMAT = constant.Constant( 'GL_CONVOLUTION_FORMAT', 0x8017 )
GL_CONVOLUTION_WIDTH = constant.Constant( 'GL_CONVOLUTION_WIDTH', 0x8018 )
GL_CONVOLUTION_HEIGHT = constant.Constant( 'GL_CONVOLUTION_HEIGHT', 0x8019 )
GL_MAX_CONVOLUTION_WIDTH = constant.Constant( 'GL_MAX_CONVOLUTION_WIDTH', 0x801A )
GL_MAX_CONVOLUTION_HEIGHT = constant.Constant( 'GL_MAX_CONVOLUTION_HEIGHT', 0x801B )
GL_POST_CONVOLUTION_RED_SCALE = constant.Constant( 'GL_POST_CONVOLUTION_RED_SCALE', 0x801C )
GL_POST_CONVOLUTION_GREEN_SCALE = constant.Constant( 'GL_POST_CONVOLUTION_GREEN_SCALE', 0x801D )
GL_POST_CONVOLUTION_BLUE_SCALE = constant.Constant( 'GL_POST_CONVOLUTION_BLUE_SCALE', 0x801E )
GL_POST_CONVOLUTION_ALPHA_SCALE = constant.Constant( 'GL_POST_CONVOLUTION_ALPHA_SCALE', 0x801F )
GL_POST_CONVOLUTION_RED_BIAS = constant.Constant( 'GL_POST_CONVOLUTION_RED_BIAS', 0x8020 )
GL_POST_CONVOLUTION_GREEN_BIAS = constant.Constant( 'GL_POST_CONVOLUTION_GREEN_BIAS', 0x8021 )
GL_POST_CONVOLUTION_BLUE_BIAS = constant.Constant( 'GL_POST_CONVOLUTION_BLUE_BIAS', 0x8022 )
GL_POST_CONVOLUTION_ALPHA_BIAS = constant.Constant( 'GL_POST_CONVOLUTION_ALPHA_BIAS', 0x8023 )
GL_HISTOGRAM = constant.Constant( 'GL_HISTOGRAM', 0x8024 )
GL_PROXY_HISTOGRAM = constant.Constant( 'GL_PROXY_HISTOGRAM', 0x8025 )
GL_HISTOGRAM_WIDTH = constant.Constant( 'GL_HISTOGRAM_WIDTH', 0x8026 )
GL_HISTOGRAM_FORMAT = constant.Constant( 'GL_HISTOGRAM_FORMAT', 0x8027 )
GL_HISTOGRAM_RED_SIZE = constant.Constant( 'GL_HISTOGRAM_RED_SIZE', 0x8028 )
GL_HISTOGRAM_GREEN_SIZE = constant.Constant( 'GL_HISTOGRAM_GREEN_SIZE', 0x8029 )
GL_HISTOGRAM_BLUE_SIZE = constant.Constant( 'GL_HISTOGRAM_BLUE_SIZE', 0x802A )
GL_HISTOGRAM_ALPHA_SIZE = constant.Constant( 'GL_HISTOGRAM_ALPHA_SIZE', 0x802B )
GL_HISTOGRAM_LUMINANCE_SIZE = constant.Constant( 'GL_HISTOGRAM_LUMINANCE_SIZE', 0x802C )
GL_HISTOGRAM_SINK = constant.Constant( 'GL_HISTOGRAM_SINK', 0x802D )
GL_MINMAX = constant.Constant( 'GL_MINMAX', 0x802E )
GL_MINMAX_FORMAT = constant.Constant( 'GL_MINMAX_FORMAT', 0x802F )
GL_MINMAX_SINK = constant.Constant( 'GL_MINMAX_SINK', 0x8030 )
GL_TABLE_TOO_LARGE = constant.Constant( 'GL_TABLE_TOO_LARGE', 0x8031 )
GL_COLOR_MATRIX = constant.Constant( 'GL_COLOR_MATRIX', 0x80B1 )
glget.addGLGetConstant( GL_COLOR_MATRIX, (4,4) )
GL_COLOR_MATRIX_STACK_DEPTH = constant.Constant( 'GL_COLOR_MATRIX_STACK_DEPTH', 0x80B2 )
GL_MAX_COLOR_MATRIX_STACK_DEPTH = constant.Constant( 'GL_MAX_COLOR_MATRIX_STACK_DEPTH', 0x80B3 )
GL_POST_COLOR_MATRIX_RED_SCALE = constant.Constant( 'GL_POST_COLOR_MATRIX_RED_SCALE', 0x80B4 )
GL_POST_COLOR_MATRIX_GREEN_SCALE = constant.Constant( 'GL_POST_COLOR_MATRIX_GREEN_SCALE', 0x80B5 )
GL_POST_COLOR_MATRIX_BLUE_SCALE = constant.Constant( 'GL_POST_COLOR_MATRIX_BLUE_SCALE', 0x80B6 )
GL_POST_COLOR_MATRIX_ALPHA_SCALE = constant.Constant( 'GL_POST_COLOR_MATRIX_ALPHA_SCALE', 0x80B7 )
GL_POST_COLOR_MATRIX_RED_BIAS = constant.Constant( 'GL_POST_COLOR_MATRIX_RED_BIAS', 0x80B8 )
GL_POST_COLOR_MATRIX_GREEN_BIAS = constant.Constant( 'GL_POST_COLOR_MATRIX_GREEN_BIAS', 0x80B9 )
GL_POST_COLOR_MATRIX_BLUE_BIAS = constant.Constant( 'GL_POST_COLOR_MATRIX_BLUE_BIAS', 0x80BA )
GL_POST_COLOR_MATRIX_ALPHA_BIAS = constant.Constant( 'GL_POST_COLOR_MATRIX_ALPHA_BIAS', 0x80BB )
GL_COLOR_TABLE = constant.Constant( 'GL_COLOR_TABLE', 0x80D0 )
GL_POST_CONVOLUTION_COLOR_TABLE = constant.Constant( 'GL_POST_CONVOLUTION_COLOR_TABLE', 0x80D1 )
GL_POST_COLOR_MATRIX_COLOR_TABLE = constant.Constant( 'GL_POST_COLOR_MATRIX_COLOR_TABLE', 0x80D2 )
GL_PROXY_COLOR_TABLE = constant.Constant( 'GL_PROXY_COLOR_TABLE', 0x80D3 )
GL_PROXY_POST_CONVOLUTION_COLOR_TABLE = constant.Constant( 'GL_PROXY_POST_CONVOLUTION_COLOR_TABLE', 0x80D4 )
GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE = constant.Constant( 'GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE', 0x80D5 )
GL_COLOR_TABLE_SCALE = constant.Constant( 'GL_COLOR_TABLE_SCALE', 0x80D6 )
GL_COLOR_TABLE_BIAS = constant.Constant( 'GL_COLOR_TABLE_BIAS', 0x80D7 )
GL_COLOR_TABLE_FORMAT = constant.Constant( 'GL_COLOR_TABLE_FORMAT', 0x80D8 )
GL_COLOR_TABLE_WIDTH = constant.Constant( 'GL_COLOR_TABLE_WIDTH', 0x80D9 )
GL_COLOR_TABLE_RED_SIZE = constant.Constant( 'GL_COLOR_TABLE_RED_SIZE', 0x80DA )
GL_COLOR_TABLE_GREEN_SIZE = constant.Constant( 'GL_COLOR_TABLE_GREEN_SIZE', 0x80DB )
GL_COLOR_TABLE_BLUE_SIZE = constant.Constant( 'GL_COLOR_TABLE_BLUE_SIZE', 0x80DC )
GL_COLOR_TABLE_ALPHA_SIZE = constant.Constant( 'GL_COLOR_TABLE_ALPHA_SIZE', 0x80DD )
GL_COLOR_TABLE_LUMINANCE_SIZE = constant.Constant( 'GL_COLOR_TABLE_LUMINANCE_SIZE', 0x80DE )
GL_COLOR_TABLE_INTENSITY_SIZE = constant.Constant( 'GL_COLOR_TABLE_INTENSITY_SIZE', 0x80DF )
GL_CONSTANT_BORDER = constant.Constant( 'GL_CONSTANT_BORDER', 0x8151 )
GL_REPLICATE_BORDER = constant.Constant( 'GL_REPLICATE_BORDER', 0x8153 )
GL_CONVOLUTION_BORDER_COLOR = constant.Constant( 'GL_CONVOLUTION_BORDER_COLOR', 0x8154 )


def glInitImagingDeprecatedARB():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
