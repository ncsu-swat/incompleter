# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59409208/getting-a-typeerror-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
n= 5
_l_(345033)
def fact(n):
    _l_(345042)

    if _n_(345034, "n", lambda: n)== 0:
        _l_(345041)

        aux = 1
        _l_(345035)
        return aux
    else:
        aux = (_n_(345036, "n", lambda: n)*_c_(345039, _n_(345037, "fact", lambda: fact), _n_(345038, "n", lambda: n)-1))
        _l_(345040)
        return aux

_c_(345047, _n_(345043, "print", lambda: print), _c_(345046, _n_(345044, "fact", lambda: fact), _n_(345045, "n", lambda: n)))
_l_(345048)