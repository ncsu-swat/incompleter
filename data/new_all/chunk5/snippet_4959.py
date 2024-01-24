# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37632704/nameerror-when-running-pyglet
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pyglet.gl import *
    _l_(653347)

except ImportError:
    pass
try:
    from pyglet.window import key
    _l_(653349)

except ImportError:
    pass
try:
    from pyglet.window import mouse
    _l_(653351)

except ImportError:
    pass


window=_c_(653355, _a_(653354, _a_(653353, _n_(653352, "pyglet", lambda: pyglet), "window"), "Window"), resizable=True)
_l_(653356)

@_a_(653358, _n_(653357, "window", lambda: window), "event")
def on_draw():
    _l_(653386)


    _c_(653362, _n_(653359, "glutInitDisplayMode", lambda: glutInitDisplayMode), _n_(653360, "GLUT_RGB", lambda: GLUT_RGB) | _n_(653361, "GLUT_DOUBLE", lambda: GLUT_DOUBLE))
    _l_(653363)
    _c_(653367, _n_(653364, "glutInitWindowSize", lambda: glutInitWindowSize), _n_(653365, "width", lambda: width), _n_(653366, "height", lambda: height))
    _l_(653368)
    _c_(653370, _n_(653369, "glutInitWindowPosition", lambda: glutInitWindowPosition), 100, 100)
    _l_(653371)


    _c_(653373, _n_(653372, "glClearColor", lambda: glClearColor), 1.0, 1.0, 1.0, 1.0)
    _l_(653374)
    _c_(653378, _n_(653375, "glClear", lambda: glClear), _n_(653376, "GL_COLOR_BUFFER_BIT", lambda: GL_COLOR_BUFFER_BIT) | _n_(653377, "GL_DEPTH_BUFFER_BIT", lambda: GL_DEPTH_BUFFER_BIT))
    _l_(653379)
    _c_(653381, _n_(653380, "myObject", lambda: myObject))
    _l_(653382)
    _c_(653384, _n_(653383, "glutSwapBuffers", lambda: glutSwapBuffers)) 
    _l_(653385) 