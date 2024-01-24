# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40317307/python-typeerror-unsupported-operand-types-for-int-and-nonetype
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from functools import reduce
    _l_(431916)

except ImportError:
    pass
def char2num(s1):
    _l_(431922)

    if _n_(431917, "s1", lambda: s1) == '.':
        _l_(431921)

        pass
        _l_(431918)
    else:
        aux = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[_n_(431919, "s1", lambda: s1)]
        _l_(431920)
        return aux

def str2float(s):
    _l_(431953)

    count = 0
    _l_(431923)

    ans = _c_(431931, _n_(431924, "reduce", lambda: reduce), lambda x, y: 10*_n_(431925, "x", lambda: x) + _n_(431926, "y", lambda: y),_c_(431930, _n_(431927, "map", lambda: map), _n_(431928, "char2num", lambda: char2num),_n_(431929, "s", lambda: s)))
    _l_(431932)

    for x in _c_(431937, _n_(431933, "range", lambda: range), _c_(431936, _n_(431934, "len", lambda: len), _n_(431935, "s", lambda: s))):
        _l_(431945)

        if _n_(431938, "s", lambda: s)[_n_(431939, "x", lambda: x)] == '.':
            _l_(431944)

            count = _n_(431940, "x", lambda: x)
            _l_(431941)
            break
            _l_(431942)
        else:
            pass
            _l_(431943)
    for n in _c_(431948, _n_(431946, "range", lambda: range), _n_(431947, "count", lambda: count)):
        _l_(431950)

        ans /= 10
        _l_(431949)
    aux = _n_(431951, "ans", lambda: ans)
    _l_(431952)
    return aux
_c_(431957, _n_(431954, "print", lambda: print), 'str2float(\'123.456\') =', _c_(431956, _n_(431955, "str2float", lambda: str2float), '123.456'))
_l_(431958)