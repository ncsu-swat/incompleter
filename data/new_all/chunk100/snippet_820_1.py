# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def permute_string(str):
    _l_(82621)

    if _c_(82578, _n_(82576, "len", lambda: len), _n_(82577, "str", lambda: str)) == 0:
        _l_(82580)

        aux = ['']
        _l_(82579)
        return aux
    prev_list = _c_(82586, _n_(82581, "permute_string", lambda: permute_string), _n_(82582, "str", lambda: str)[1:_c_(82585, _n_(82583, "len", lambda: len), _n_(82584, "str", lambda: str))])
    _l_(82587)
    for i in _c_(82592, _n_(82588, "range", lambda: range), 0, _c_(82591, _n_(82589, "len", lambda: len), _n_(82590, "prev_list", lambda: prev_list))):
        _l_(82618)

        for j in _c_(82597, _n_(82593, "range", lambda: range), 0, _c_(82596, _n_(82594, "len", lambda: len), _n_(82595, "str", lambda: str))):
            _l_(82617)

            new_str = _n_(82598, "prev_list", lambda: prev_list)[_n_(82599, "i", lambda: i)][0:_n_(82600, "j", lambda: j)] + _n_(82601, "str", lambda: str)[0] + _n_(82602, "prev_list", lambda: prev_list)[_n_(82603, "i", lambda: i)][_n_(82604, "j", lambda: j):_c_(82607, _n_(82605, "len", lambda: len), _n_(82606, "str", lambda: str)) - 1]
            _l_(82608)
            if _n_(82609, "new_str", lambda: new_str) not in _n_(82610, "next_list", lambda: next_list):
                _l_(82616)

                _c_(82614, _a_(82612, _n_(82611, "next_list", lambda: next_list), "append"), _n_(82613, "new_str", lambda: new_str))
                _l_(82615)
    aux = _n_(82619, "next_list", lambda: next_list)
    _l_(82620)
    return aux
_c_(82625, _n_(82622, "print", lambda: print), _c_(82624, _n_(82623, "permute_string", lambda: permute_string), 'ABCD'))
_l_(82626)