# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56572523/navernews-default-nameerror-name-navernews-is-not-defined
# Default.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(660842)

except ImportError:
    pass
_c_(660846, _a_(660845, _a_(660844, _n_(660843, "sys", lambda: sys), "path"), "append"), '/NaverNews/Main/Main')
_l_(660847)
try:
    from Main import *
    _l_(660849)

except ImportError:
    pass
@_n_(660850, "NaverNews", lambda: NaverNews)
def DefaultNews():
    _l_(660857)

    _c_(660852, _n_(660851, "print", lambda: print), "Shutting Down the Program")
    _l_(660853)
    aux = 0
    _l_(660856)
    exit(aux)
_c_(660859, _n_(660858, "DefaultNews", lambda: DefaultNews))
_l_(660860)