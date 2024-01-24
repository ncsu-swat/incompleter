# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37632704/nameerror-when-running-pyglet
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pyglet.gl import *
    _l_(669135)

except ImportError:
    pass
try:
    from pyglet.window import key
    _l_(669137)

except ImportError:
    pass
try:
    from pyglet.window import mouse
    _l_(669139)

except ImportError:
    pass


window=_c_(669143, _a_(669142, _a_(669141, _n_(669140, "pyglet", lambda: pyglet), "window"), "Window"), resizable=True)
_l_(669144)

@_a_(669146, _n_(669145, "window", lambda: window), "event")
def on_draw():
    _l_(669174)


    _c_(669150, _n_(669147, "glutInitDisplayMode", lambda: glutInitDisplayMode), _n_(669148, "GLUT_RGB", lambda: GLUT_RGB) | _n_(669149, "GLUT_DOUBLE", lambda: GLUT_DOUBLE))
    _l_(669151)
    _c_(669155, _n_(669152, "glutInitWindowSize", lambda: glutInitWindowSize), _n_(669153, "width", lambda: width), _n_(669154, "height", lambda: height))
    _l_(669156)
    _c_(669158, _n_(669157, "glutInitWindowPosition", lambda: glutInitWindowPosition), 100, 100)
    _l_(669159)


    _c_(669161, _n_(669160, "glClearColor", lambda: glClearColor), 1.0, 1.0, 1.0, 1.0)
    _l_(669162)
    _c_(669166, _n_(669163, "glClear", lambda: glClear), _n_(669164, "GL_COLOR_BUFFER_BIT", lambda: GL_COLOR_BUFFER_BIT) | _n_(669165, "GL_DEPTH_BUFFER_BIT", lambda: GL_DEPTH_BUFFER_BIT))
    _l_(669167)
    _c_(669169, _n_(669168, "myObject", lambda: myObject))
    _l_(669170)
    _c_(669172, _n_(669171, "glutSwapBuffers", lambda: glutSwapBuffers)) 
    _l_(669173) 