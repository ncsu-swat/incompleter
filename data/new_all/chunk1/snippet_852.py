# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61776922/python-3-exec-method-nameerror-name-of-a-defined-function-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def calcCycleOffset():
    _l_(404227)

    global cycleOffset, uc, cs
    _l_(404221)

    cycleOffset = _n_(404222, "uc", lambda: uc) - _n_(404223, "cs", lambda: cs)
    _l_(404224)
    aux = _n_(404225, "cycleOffset", lambda: cycleOffset)
    _l_(404226)
    return aux


def vir_main():
    _l_(404231)

    _c_(404229, _n_(404228, "calcCycleOffset", lambda: calcCycleOffset))
    _l_(404230)


_c_(404233, _n_(404232, "vir_main", lambda: vir_main))
_l_(404234)
#calcCycleOffset()


_c_(404237, _n_(404235, "print", lambda: print), "vir.py: cycleOffset: ", _n_(404236, "cycleOffset", lambda: cycleOffset) )
_l_(404238)