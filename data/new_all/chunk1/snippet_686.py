# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57457958/fibonacci-memoization-cannot-understand-the-reason-for-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def memoize(f):
    _l_(401005)

    memo = {}
    _l_(400989)
    def helper(x):
        _l_(401002)

        if _n_(400990, "x", lambda: x) not in _n_(400991, "memo", lambda: memo):
            _l_(401001)

            _n_(400992, "memo", lambda: memo)[_n_(400993, "x", lambda: x)] = _c_(400996, _n_(400994, "f", lambda: f), _n_(400995, "x", lambda: x))
            _l_(400997)
            aux = _n_(400998, "memo", lambda: memo)[_n_(400999, "x", lambda: x)]
            _l_(401000)
            return aux
    aux = _n_(401003, "helper", lambda: helper)
    _l_(401004)
    return aux
def fib(n):
    _l_(401019)

    if _n_(401006, "n", lambda: n)==0:
        _l_(401008)

        aux = 0
        _l_(401007)
        return aux
    if _n_(401009, "n", lambda: n) == 1:
        _l_(401018)

        aux = 1
        _l_(401010)
        return aux
    else:
        aux = _c_(401013, _n_(401011, "fib", lambda: fib), _n_(401012, "n", lambda: n)-1)+_c_(401016, _n_(401014, "fib", lambda: fib), _n_(401015, "n", lambda: n)-2)
        _l_(401017)
        return aux

fib = _c_(401022, _n_(401020, "memoize", lambda: memoize), _n_(401021, "fib", lambda: fib))
_l_(401023)

_c_(401027, _n_(401024, "print", lambda: print), _c_(401026, _n_(401025, "fib", lambda: fib), 10))
_l_(401028)