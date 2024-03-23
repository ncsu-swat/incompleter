# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def is_Sublist(l, s):
    _l_(73294)

    sub_set = False
    _l_(73248)
    if _n_(73249, "s", lambda: s) == []:
        _l_(73291)

        sub_set = True
        _l_(73250)
    elif _n_(73251, "s", lambda: s) == _n_(73252, "l", lambda: l):
        _l_(73290)

        sub_set = True
        _l_(73253)
    elif _c_(73256, _n_(73254, "len", lambda: len), _n_(73255, "s", lambda: s)) > _c_(73259, _n_(73257, "len", lambda: len), _n_(73258, "l", lambda: l)):
        _l_(73289)

        sub_set = False
        _l_(73260)
    else:
        for i in _c_(73265, _n_(73261, "range", lambda: range), _c_(73264, _n_(73262, "len", lambda: len), _n_(73263, "l", lambda: l))):
            _l_(73288)

            if _n_(73266, "l", lambda: l)[_n_(73267, "i", lambda: i)] == _n_(73268, "s", lambda: s)[0]:
                _l_(73287)

                n = 1
                _l_(73269)
                while _n_(73270, "n", lambda: n) < _c_(73273, _n_(73271, "len", lambda: len), _n_(73272, "s", lambda: s)) and _n_(73274, "l", lambda: l)[_n_(73275, "i", lambda: i) + _n_(73276, "n", lambda: n)] == _n_(73277, "s", lambda: s)[_n_(73278, "n", lambda: n)]:
                    _l_(73280)

                    n += 1
                    _l_(73279)
                if _n_(73281, "n", lambda: n) == _c_(73284, _n_(73282, "len", lambda: len), _n_(73283, "s", lambda: s)):
                    _l_(73286)

                    sub_set = True
                    _l_(73285)
    aux = _n_(73292, "sub_set", lambda: sub_set)
    _l_(73293)
    return aux
b = [4, 3]
_l_(73295)
c = [3, 7]
_l_(73296)
_c_(73302, _n_(73297, "print", lambda: print), _c_(73301, _n_(73298, "is_Sublist", lambda: is_Sublist), _n_(73299, "a", lambda: a), _n_(73300, "b", lambda: b)))
_l_(73303)
_c_(73309, _n_(73304, "print", lambda: print), _c_(73308, _n_(73305, "is_Sublist", lambda: is_Sublist), _n_(73306, "a", lambda: a), _n_(73307, "c", lambda: c)))
_l_(73310)