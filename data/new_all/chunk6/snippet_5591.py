# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46933027/combined-numbers-to-given-sum-typeerror-type-object-is-not-subscriptable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def subset_sum(numbers, target, partial=[]):
    _l_(335624)

    s = _c_(335585, _n_(335583, "sum", lambda: sum), _n_(335584, "partial", lambda: partial))
    _l_(335586)
    if _c_(335589, _n_(335587, "len", lambda: len), _n_(335588, "numbers", lambda: numbers)) == 0:
        _l_(335623)

        aux = ""
        _l_(335590)
        return aux
    elif _n_(335591, "s", lambda: s) == _n_(335592, "target", lambda: target):
        _l_(335622)

        _c_(335598, _n_(335593, "print", lambda: print), _c_(335597, _a_(335594, "sum({})={}", "format"), _n_(335595, "partial", lambda: partial), _n_(335596, "target", lambda: target)))
        _l_(335599)
        aux = ""
        _l_(335600)
        return aux
    else:
        for i in _c_(335605, _n_(335601, "range", lambda: range), _c_(335604, _n_(335602, "len", lambda: len), _n_(335603, "numbers", lambda: numbers))):
            _l_(335621)

            n = _n_(335606, "numbers", lambda: numbers)[_n_(335607, "i", lambda: i)]
            _l_(335608)
            remaining = _n_(335609, "numbers", lambda: numbers)[:_n_(335610, "i", lambda: i)] + _n_(335611, "numbers", lambda: numbers)[_n_(335612, "i", lambda: i)+1:]
            _l_(335613)
            _c_(335619, _n_(335614, "subset_sum", lambda: subset_sum), _n_(335615, "remaining", lambda: remaining), _n_(335616, "target", lambda: target), _n_(335617, "partial", lambda: partial) + [_n_(335618, "n", lambda: n)])
            _l_(335620)

s = [2, 4]
_l_(335625)
k = [22, 25, -11, 13, 58]
_l_(335626)
x = [100, 101, 23]
_l_(335627)
v = [77, 88, 99]
_l_(335628)

y = _n_(335629, "s", lambda: s)+_n_(335630, "k", lambda: k)+_n_(335631, "x", lambda: x)+_n_(335632, "v", lambda: v)
_l_(335633)

if _n_(335634, "__name__", lambda: __name__) == "__main__":
    _l_(335639)

    _c_(335637, _n_(335635, "subset_sum", lambda: subset_sum), _n_(335636, "y", lambda: y), 47)
    _l_(335638)