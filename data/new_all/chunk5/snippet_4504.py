# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56572523/navernews-default-nameerror-name-navernews-is-not-defined
# Default.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(694435)

except ImportError:
    pass
_c_(694439, _a_(694438, _a_(694437, _n_(694436, "sys", lambda: sys), "path"), "append"), '/NaverNews/Main/Main')
_l_(694440)
try:
    from Main import *
    _l_(694442)

except ImportError:
    pass
@_n_(694443, "NaverNews", lambda: NaverNews)
def DefaultNews():
    _l_(694450)

    _c_(694445, _n_(694444, "print", lambda: print), "Shutting Down the Program")
    _l_(694446)
    aux = 0
    _l_(694449)
    exit(aux)
_c_(694452, _n_(694451, "DefaultNews", lambda: DefaultNews))
_l_(694453)