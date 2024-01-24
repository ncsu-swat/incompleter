# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50214624/nonetype-error-converting-opengl-script-from-py-to-exe-using-cx-freeze
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(385443)

except ImportError:
    pass
try:
    from pygame.locals import *
    _l_(385445)

except ImportError:
    pass
try:
    from OpenGL.GL import *
    _l_(385447)

except ImportError:
    pass
try:
    from OpenGL.GLU import *
    _l_(385449)

except ImportError:
    pass