# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def is_Sublist(l, s):
    _l_(73419)

    if _n_(73374, "s", lambda: s) == []:
        _l_(73416)

        sub_set = True
        _l_(73375)
    elif _n_(73376, "s", lambda: s) == _n_(73377, "l", lambda: l):
        _l_(73415)

        sub_set = True
        _l_(73378)
    elif _c_(73381, _n_(73379, "len", lambda: len), _n_(73380, "s", lambda: s)) > _c_(73384, _n_(73382, "len", lambda: len), _n_(73383, "l", lambda: l)):
        _l_(73414)

        sub_set = False
        _l_(73385)
    else:
        for i in _c_(73390, _n_(73386, "range", lambda: range), _c_(73389, _n_(73387, "len", lambda: len), _n_(73388, "l", lambda: l))):
            _l_(73413)

            if _n_(73391, "l", lambda: l)[_n_(73392, "i", lambda: i)] == _n_(73393, "s", lambda: s)[0]:
                _l_(73412)

                n = 1
                _l_(73394)
                while _n_(73395, "n", lambda: n) < _c_(73398, _n_(73396, "len", lambda: len), _n_(73397, "s", lambda: s)) and _n_(73399, "l", lambda: l)[_n_(73400, "i", lambda: i) + _n_(73401, "n", lambda: n)] == _n_(73402, "s", lambda: s)[_n_(73403, "n", lambda: n)]:
                    _l_(73405)

                    n += 1
                    _l_(73404)
                if _n_(73406, "n", lambda: n) == _c_(73409, _n_(73407, "len", lambda: len), _n_(73408, "s", lambda: s)):
                    _l_(73411)

                    sub_set = True
                    _l_(73410)
    aux = _n_(73417, "sub_set", lambda: sub_set)
    _l_(73418)
    return aux
a = [2, 4, 3, 5, 7]
_l_(73420)
b = [4, 3]
_l_(73421)
c = [3, 7]
_l_(73422)
_c_(73428, _n_(73423, "print", lambda: print), _c_(73427, _n_(73424, "is_Sublist", lambda: is_Sublist), _n_(73425, "a", lambda: a), _n_(73426, "b", lambda: b)))
_l_(73429)
_c_(73435, _n_(73430, "print", lambda: print), _c_(73434, _n_(73431, "is_Sublist", lambda: is_Sublist), _n_(73432, "a", lambda: a), _n_(73433, "c", lambda: c)))
_l_(73436)