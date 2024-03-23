# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def permute_string(str):
    _l_(82570)

    if _c_(82533, _n_(82531, "len", lambda: len), _n_(82532, "str", lambda: str)) == 0:
        _l_(82535)

        aux = ['']
        _l_(82534)
        return aux
    next_list = []
    _l_(82536)
    for i in _c_(82541, _n_(82537, "range", lambda: range), 0, _c_(82540, _n_(82538, "len", lambda: len), _n_(82539, "prev_list", lambda: prev_list))):
        _l_(82567)

        for j in _c_(82546, _n_(82542, "range", lambda: range), 0, _c_(82545, _n_(82543, "len", lambda: len), _n_(82544, "str", lambda: str))):
            _l_(82566)

            new_str = _n_(82547, "prev_list", lambda: prev_list)[_n_(82548, "i", lambda: i)][0:_n_(82549, "j", lambda: j)] + _n_(82550, "str", lambda: str)[0] + _n_(82551, "prev_list", lambda: prev_list)[_n_(82552, "i", lambda: i)][_n_(82553, "j", lambda: j):_c_(82556, _n_(82554, "len", lambda: len), _n_(82555, "str", lambda: str)) - 1]
            _l_(82557)
            if _n_(82558, "new_str", lambda: new_str) not in _n_(82559, "next_list", lambda: next_list):
                _l_(82565)

                _c_(82563, _a_(82561, _n_(82560, "next_list", lambda: next_list), "append"), _n_(82562, "new_str", lambda: new_str))
                _l_(82564)
    aux = _n_(82568, "next_list", lambda: next_list)
    _l_(82569)
    return aux
_c_(82574, _n_(82571, "print", lambda: print), _c_(82573, _n_(82572, "permute_string", lambda: permute_string), 'ABCD'))
_l_(82575)