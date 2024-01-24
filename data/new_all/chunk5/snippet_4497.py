# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56572523/navernews-default-nameerror-name-navernews-is-not-defined
# Default.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(690777)

except ImportError:
    pass
_c_(690781, _a_(690780, _a_(690779, _n_(690778, "sys", lambda: sys), "path"), "append"), '/NaverNews/Main/Main')
_l_(690782)
try:
    from Main import *
    _l_(690784)

except ImportError:
    pass
@_n_(690785, "NaverNews", lambda: NaverNews)
def DefaultNews():
    _l_(690792)

    _c_(690787, _n_(690786, "print", lambda: print), "Shutting Down the Program")
    _l_(690788)
    aux = 0
    _l_(690791)
    exit(aux)
_c_(690794, _n_(690793, "DefaultNews", lambda: DefaultNews))
_l_(690795)