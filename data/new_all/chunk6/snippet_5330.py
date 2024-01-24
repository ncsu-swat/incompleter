# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66599287/i-have-already-translated-the-type-into-int-but-still-suffered-a-type-error-pyt
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def get_positive_int():
    _l_(365086)

    while True:
        _l_(365085)

        n = _c_(365078, _n_(365075, "int", lambda: int), _c_(365077, _n_(365076, "input", lambda: input), "Height: "))
        _l_(365079)
        if _n_(365080, "n", lambda: n) > 0 and _n_(365081, "n", lambda: n) < 9:
            _l_(365084)

            aux = _n_(365082, "n", lambda: n)
            _l_(365083)
            return aux
def print(n):
    _l_(365098)

    for i in _c_(365089, _n_(365087, "range", lambda: range), _n_(365088, "n", lambda: n)):
        _l_(365097)

        _c_(365095, _n_(365090, "print", lambda: print), " " * (_n_(365091, "n", lambda: n) - _n_(365092, "i", lambda: i)) + "#" * _n_(365093, "i", lambda: i) + " " + "#" * _n_(365094, "i", lambda: i))
        _l_(365096)
def main():
    _l_(365106)

    n = _c_(365100, _n_(365099, "get_positive_int", lambda: get_positive_int))
    _l_(365101)
    _c_(365104, _n_(365102, "print", lambda: print), _n_(365103, "n", lambda: n))
    _l_(365105)
if _n_(365107, "__name__", lambda: __name__) == "__main__":
    _l_(365111)

    _c_(365109, _n_(365108, "main", lambda: main))
    _l_(365110)