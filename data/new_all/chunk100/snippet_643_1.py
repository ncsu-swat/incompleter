# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def isPalindrome(string):
    _l_(66267)

    left_pos = 0
    _l_(66254)
    while _n_(66255, "right_pos", lambda: right_pos) >= _n_(66256, "left_pos", lambda: left_pos):
        _l_(66265)

        if not _n_(66257, "string", lambda: string)[_n_(66258, "left_pos", lambda: left_pos)] == _n_(66259, "string", lambda: string)[_n_(66260, "right_pos", lambda: right_pos)]:
            _l_(66262)

            aux = False
            _l_(66261)
            return aux
        left_pos += 1
        _l_(66263)
        right_pos -= 1
        _l_(66264)
    aux = True
    _l_(66266)
    return aux
_c_(66271, _n_(66268, "print", lambda: print), _c_(66270, _n_(66269, "isPalindrome", lambda: isPalindrome), 'aza'))
_l_(66272)