# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/23319925/nameerror-when-running-pyopengl
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from OpenGL import *
    _l_(451753)

except ImportError:
    pass
try:
    from OpenGL.GLUT import *
    _l_(451755)

except ImportError:
    pass
try:
    from OpenGL.GLU import *
    _l_(451757)

except ImportError:
    pass


window = 0 
_l_(451758) 
width, height = 500,400
_l_(451759)

def draw():
    _l_(451768)

    _c_(451763, _n_(451760, "glClear", lambda: glClear), _n_(451761, "GL_COLOR_BUFFER_BIT", lambda: GL_COLOR_BUFFER_BIT) |_n_(451762, "GL_DEPTH_BUFFER_BIT", lambda: GL_DEPTH_BUFFER_BIT))           
    _l_(451764)           
    _c_(451766, _n_(451765, "glLoadIdentity", lambda: glLoadIdentity))
    _l_(451767)

_c_(451770, _n_(451769, "glutDwapBuffers", lambda: glutDwapBuffers))                                           
_l_(451771)                                           




#initialization
_c_(451773, _n_(451772, "glutInit", lambda: glutInit))
_l_(451774)
_c_(451780, _n_(451775, "glutInitDisplayMode", lambda: glutInitDisplayMode), _n_(451776, "GLUT_RGBA", lambda: GLUT_RGBA) | _n_(451777, "GLUT_DOUBLE", lambda: GLUT_DOUBLE) | _n_(451778, "GLUT_ALPHA", lambda: GLUT_ALPHA) | _n_(451779, "GLUT_DEPTH", lambda: GLUT_DEPTH))
_l_(451781)
_c_(451785, _n_(451782, "glutInitWindowSize", lambda: glutInitWindowSize), _n_(451783, "width", lambda: width),_n_(451784, "height", lambda: height))
_l_(451786)
_c_(451788, _n_(451787, "glutInitWindowPosition", lambda: glutInitWindowPosition), 0,0)
_l_(451789)
window = _c_(451791, _n_(451790, "glutCreateWindow", lambda: glutCreateWindow), b"noobtute")
_l_(451792)
_c_(451795, _n_(451793, "glutDisplayFunc", lambda: glutDisplayFunc), _n_(451794, "draw", lambda: draw))                                                                       
_l_(451796)                                                                       
_c_(451799, _n_(451797, "glutIdleFunc", lambda: glutIdleFunc), _n_(451798, "draw", lambda: draw))  
_l_(451800)  
_c_(451802, _n_(451801, "glutMainLoop", lambda: glutMainLoop))              
_l_(451803)              