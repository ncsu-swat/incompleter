# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def is_Sublist(l, s):
    _l_(73357)

    sub_set = False
    _l_(73311)
    if _n_(73312, "s", lambda: s) == []:
        _l_(73354)

        sub_set = True
        _l_(73313)
    elif _n_(73314, "s", lambda: s) == _n_(73315, "l", lambda: l):
        _l_(73353)

        sub_set = True
        _l_(73316)
    elif _c_(73319, _n_(73317, "len", lambda: len), _n_(73318, "s", lambda: s)) > _c_(73322, _n_(73320, "len", lambda: len), _n_(73321, "l", lambda: l)):
        _l_(73352)

        sub_set = False
        _l_(73323)
    else:
        for i in _c_(73328, _n_(73324, "range", lambda: range), _c_(73327, _n_(73325, "len", lambda: len), _n_(73326, "l", lambda: l))):
            _l_(73351)

            if _n_(73329, "l", lambda: l)[_n_(73330, "i", lambda: i)] == _n_(73331, "s", lambda: s)[0]:
                _l_(73350)

                n = 1
                _l_(73332)
                while _n_(73333, "n", lambda: n) < _c_(73336, _n_(73334, "len", lambda: len), _n_(73335, "s", lambda: s)) and _n_(73337, "l", lambda: l)[_n_(73338, "i", lambda: i) + _n_(73339, "n", lambda: n)] == _n_(73340, "s", lambda: s)[_n_(73341, "n", lambda: n)]:
                    _l_(73343)

                    n += 1
                    _l_(73342)
                if _n_(73344, "n", lambda: n) == _c_(73347, _n_(73345, "len", lambda: len), _n_(73346, "s", lambda: s)):
                    _l_(73349)

                    sub_set = True
                    _l_(73348)
    aux = _n_(73355, "sub_set", lambda: sub_set)
    _l_(73356)
    return aux
a = [2, 4, 3, 5, 7]
_l_(73358)
b = [4, 3]
_l_(73359)
_c_(73365, _n_(73360, "print", lambda: print), _c_(73364, _n_(73361, "is_Sublist", lambda: is_Sublist), _n_(73362, "a", lambda: a), _n_(73363, "b", lambda: b)))
_l_(73366)
_c_(73372, _n_(73367, "print", lambda: print), _c_(73371, _n_(73368, "is_Sublist", lambda: is_Sublist), _n_(73369, "a", lambda: a), _n_(73370, "c", lambda: c)))
_l_(73373)