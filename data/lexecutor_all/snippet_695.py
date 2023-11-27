# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1261875/what-does-nonlocal-do-in-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
a = 10
_l_(1538834)
def Outer(msg):
    _l_(1538865)

    a = 20
    _l_(1538835)
    b = 30
    _l_(1538836)
    def Inner():
        _l_(1538857)

        c = 50
        _l_(1538837)
        d = 60
        _l_(1538838)
        _c_(1538842, _n_(1538839, "print", lambda: print), "MU LCL =",_c_(1538841, _n_(1538840, "locals", lambda: locals)))
        _l_(1538843)
        nonlocal a
        _l_(1538844)
        a = 100
        _l_(1538845)
        ans = _n_(1538846, "a", lambda: a)+_n_(1538847, "c", lambda: c)
        _l_(1538848)
        _c_(1538851, _n_(1538849, "print", lambda: print), "Hello from Inner",_n_(1538850, "ans", lambda: ans))       
        _l_(1538852)       
        _c_(1538855, _n_(1538853, "print", lambda: print), "value of a Inner : ",_n_(1538854, "a", lambda: a))
        _l_(1538856)
    _c_(1538859, _n_(1538858, "Inner", lambda: Inner))
    _l_(1538860)
    _c_(1538863, _n_(1538861, "print", lambda: print), "value of a Outer : ",_n_(1538862, "a", lambda: a))
    _l_(1538864)

res = _c_(1538867, _n_(1538866, "Outer", lambda: Outer), "Hello World")
_l_(1538868)
_c_(1538871, _n_(1538869, "print", lambda: print), _n_(1538870, "res", lambda: res))
_l_(1538872)
_c_(1538875, _n_(1538873, "print", lambda: print), "value of a Global : ",_n_(1538874, "a", lambda: a))
_l_(1538876)

