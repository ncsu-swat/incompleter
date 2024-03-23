# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def isPalindrome(string):
    _l_(66248)

    right_pos = _c_(66234, _n_(66232, "len", lambda: len), _n_(66233, "string", lambda: string)) - 1
    _l_(66235)
    while _n_(66236, "right_pos", lambda: right_pos) >= _n_(66237, "left_pos", lambda: left_pos):
        _l_(66246)

        if not _n_(66238, "string", lambda: string)[_n_(66239, "left_pos", lambda: left_pos)] == _n_(66240, "string", lambda: string)[_n_(66241, "right_pos", lambda: right_pos)]:
            _l_(66243)

            aux = False
            _l_(66242)
            return aux
        left_pos += 1
        _l_(66244)
        right_pos -= 1
        _l_(66245)
    aux = True
    _l_(66247)
    return aux
_c_(66252, _n_(66249, "print", lambda: print), _c_(66251, _n_(66250, "isPalindrome", lambda: isPalindrome), 'aza'))
_l_(66253)