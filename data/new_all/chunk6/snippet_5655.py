# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46933027/combined-numbers-to-given-sum-typeerror-type-object-is-not-subscriptable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def subset_sum(numbers, target, partial=[]):
    _l_(338405)

    s = _c_(338366, _n_(338364, "sum", lambda: sum), _n_(338365, "partial", lambda: partial))
    _l_(338367)
    if _c_(338370, _n_(338368, "len", lambda: len), _n_(338369, "numbers", lambda: numbers)) == 0:
        _l_(338404)

        aux = ""
        _l_(338371)
        return aux
    elif _n_(338372, "s", lambda: s) == _n_(338373, "target", lambda: target):
        _l_(338403)

        _c_(338379, _n_(338374, "print", lambda: print), _c_(338378, _a_(338375, "sum({})={}", "format"), _n_(338376, "partial", lambda: partial), _n_(338377, "target", lambda: target)))
        _l_(338380)
        aux = ""
        _l_(338381)
        return aux
    else:
        for i in _c_(338386, _n_(338382, "range", lambda: range), _c_(338385, _n_(338383, "len", lambda: len), _n_(338384, "numbers", lambda: numbers))):
            _l_(338402)

            n = _n_(338387, "numbers", lambda: numbers)[_n_(338388, "i", lambda: i)]
            _l_(338389)
            remaining = _n_(338390, "numbers", lambda: numbers)[:_n_(338391, "i", lambda: i)] + _n_(338392, "numbers", lambda: numbers)[_n_(338393, "i", lambda: i)+1:]
            _l_(338394)
            _c_(338400, _n_(338395, "subset_sum", lambda: subset_sum), _n_(338396, "remaining", lambda: remaining), _n_(338397, "target", lambda: target), _n_(338398, "partial", lambda: partial) + [_n_(338399, "n", lambda: n)])
            _l_(338401)

s = [2, 4]
_l_(338406)
k = [22, 25, -11, 13, 58]
_l_(338407)
x = [100, 101, 23]
_l_(338408)
v = [77, 88, 99]
_l_(338409)

y = _n_(338410, "s", lambda: s)+_n_(338411, "k", lambda: k)+_n_(338412, "x", lambda: x)+_n_(338413, "v", lambda: v)
_l_(338414)

if _n_(338415, "__name__", lambda: __name__) == "__main__":
    _l_(338420)

    _c_(338418, _n_(338416, "subset_sum", lambda: subset_sum), _n_(338417, "y", lambda: y), 47)
    _l_(338419)