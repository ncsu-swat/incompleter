# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def permute_string(str):
    _l_(82662)

    if _c_(82629, _n_(82627, "len", lambda: len), _n_(82628, "str", lambda: str)) == 0:
        _l_(82631)

        aux = ['']
        _l_(82630)
        return aux
    prev_list = _c_(82637, _n_(82632, "permute_string", lambda: permute_string), _n_(82633, "str", lambda: str)[1:_c_(82636, _n_(82634, "len", lambda: len), _n_(82635, "str", lambda: str))])
    _l_(82638)
    next_list = []
    _l_(82639)
    for i in _c_(82644, _n_(82640, "range", lambda: range), 0, _c_(82643, _n_(82641, "len", lambda: len), _n_(82642, "prev_list", lambda: prev_list))):
        _l_(82659)

        for j in _c_(82649, _n_(82645, "range", lambda: range), 0, _c_(82648, _n_(82646, "len", lambda: len), _n_(82647, "str", lambda: str))):
            _l_(82658)

            if _n_(82650, "new_str", lambda: new_str) not in _n_(82651, "next_list", lambda: next_list):
                _l_(82657)

                _c_(82655, _a_(82653, _n_(82652, "next_list", lambda: next_list), "append"), _n_(82654, "new_str", lambda: new_str))
                _l_(82656)
    aux = _n_(82660, "next_list", lambda: next_list)
    _l_(82661)
    return aux
_c_(82666, _n_(82663, "print", lambda: print), _c_(82665, _n_(82664, "permute_string", lambda: permute_string), 'ABCD'))
_l_(82667)