# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/33380936/typeerror-function-object-is-not-subscriptable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sumList(l):
    _l_(447435)

    if _n_(447429, "l", lambda: l) == []:
        _l_(447434)

        aux = 0
        _l_(447430)
        return aux
    else:
        aux = _n_(447431, "sumList", lambda: sumList)[1:] + [_n_(447432, "l", lambda: l)[0]]
        _l_(447433)
        return aux
def main():
    _l_(447443)

    l=[3,2,5,3]
    _l_(447436)
    _c_(447441, _n_(447437, "print", lambda: print), _c_(447440, _n_(447438, "sumList", lambda: sumList), _n_(447439, "l", lambda: l)))
    _l_(447442)

_c_(447445, _n_(447444, "main", lambda: main))
_l_(447446)