# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def is_Sublist(l, s):
    _l_(73483)

    sub_set = False
    _l_(73437)
    if _n_(73438, "s", lambda: s) == []:
        _l_(73480)

        sub_set = True
        _l_(73439)
    elif _n_(73440, "s", lambda: s) == _n_(73441, "l", lambda: l):
        _l_(73479)

        sub_set = True
        _l_(73442)
    elif _c_(73445, _n_(73443, "len", lambda: len), _n_(73444, "s", lambda: s)) > _c_(73448, _n_(73446, "len", lambda: len), _n_(73447, "l", lambda: l)):
        _l_(73478)

        sub_set = False
        _l_(73449)
    else:
        for i in _c_(73454, _n_(73450, "range", lambda: range), _c_(73453, _n_(73451, "len", lambda: len), _n_(73452, "l", lambda: l))):
            _l_(73477)

            if _n_(73455, "l", lambda: l)[_n_(73456, "i", lambda: i)] == _n_(73457, "s", lambda: s)[0]:
                _l_(73476)

                n = 1
                _l_(73458)
                while _n_(73459, "n", lambda: n) < _c_(73462, _n_(73460, "len", lambda: len), _n_(73461, "s", lambda: s)) and _n_(73463, "l", lambda: l)[_n_(73464, "i", lambda: i) + _n_(73465, "n", lambda: n)] == _n_(73466, "s", lambda: s)[_n_(73467, "n", lambda: n)]:
                    _l_(73469)

                    n += 1
                    _l_(73468)
                if _n_(73470, "n", lambda: n) == _c_(73473, _n_(73471, "len", lambda: len), _n_(73472, "s", lambda: s)):
                    _l_(73475)

                    sub_set = True
                    _l_(73474)
    aux = _n_(73481, "sub_set", lambda: sub_set)
    _l_(73482)
    return aux
a = [2, 4, 3, 5, 7]
_l_(73484)
c = [3, 7]
_l_(73485)
_c_(73491, _n_(73486, "print", lambda: print), _c_(73490, _n_(73487, "is_Sublist", lambda: is_Sublist), _n_(73488, "a", lambda: a), _n_(73489, "b", lambda: b)))
_l_(73492)
_c_(73498, _n_(73493, "print", lambda: print), _c_(73497, _n_(73494, "is_Sublist", lambda: is_Sublist), _n_(73495, "a", lambda: a), _n_(73496, "c", lambda: c)))
_l_(73499)