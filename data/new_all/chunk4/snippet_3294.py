# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76024991/how-can-i-fix-type-error-int-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(606980)

except ImportError:
    pass
def main():
    _l_(607011)

    list1 = []
    _l_(606981)
    for count in _c_(606983, _n_(606982, "range", lambda: range), 100):
        _l_(606993)

        number = _c_(606986, _a_(606985, _n_(606984, "random", lambda: random), "randint"), 1,100)
        _l_(606987)
        _c_(606991, _a_(606989, _n_(606988, "list1", lambda: list1), "append"), _n_(606990, "number", lambda: number))
        _l_(606992)
    for i in _c_(606995, _n_(606994, "range", lambda: range), 0,100,10):
        _l_(607010)

        _c_(607002, _n_(606996, "print", lambda: print), _c_(606999, _n_(606997, "change_list", lambda: change_list), _n_(606998, "number", lambda: number))[_n_(607000, "i", lambda: i):_n_(607001, "i", lambda: i)+9])
        _l_(607003)
        _c_(607008, _n_(607004, "print", lambda: print), _c_(607007, _n_(607005, "dir", lambda: dir), _n_(607006, "number", lambda: number)))
        _l_(607009)
def change_list(number):
    _l_(607018)

    list1 = _c_(607014, _n_(607012, "sorted", lambda: sorted), _n_(607013, "number", lambda: number))
    _l_(607015)
    aux = _n_(607016, "list1", lambda: list1)
    _l_(607017)
    return aux

_c_(607020, _n_(607019, "main", lambda: main))
_l_(607021)