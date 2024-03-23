# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def shift_first_last(lst):
    _l_(78154)

    y = _c_(78137, _a_(78136, _n_(78135, "lst", lambda: lst), "pop"))
    _l_(78138)
    _c_(78142, _a_(78140, _n_(78139, "lst", lambda: lst), "insert"), 0, _n_(78141, "y", lambda: y))
    _l_(78143)
    _c_(78150, _a_(78145, _n_(78144, "lst", lambda: lst), "insert"), _c_(78148, _n_(78146, "len", lambda: len), _n_(78147, "lst", lambda: lst)), _n_(78149, "x", lambda: x))
    _l_(78151)
    aux = _n_(78152, "lst", lambda: lst)
    _l_(78153)
    return aux
nums = [1, 2, 3, 4, 5, 6, 7]
_l_(78155)
_c_(78157, _n_(78156, "print", lambda: print), 'Original list:')
_l_(78158)
_c_(78161, _n_(78159, "print", lambda: print), _n_(78160, "nums", lambda: nums))
_l_(78162)
_c_(78164, _n_(78163, "print", lambda: print), 'Shift last element to first position and first element to last position of the said list:')
_l_(78165)
_c_(78170, _n_(78166, "print", lambda: print), _c_(78169, _n_(78167, "shift_first_last", lambda: shift_first_last), _n_(78168, "nums", lambda: nums)))
_l_(78171)
chars = ['s', 'd', 'f', 'd', 's', 's', 'd', 'f']
_l_(78172)
_c_(78174, _n_(78173, "print", lambda: print), '\nOriginal list:')
_l_(78175)
_c_(78178, _n_(78176, "print", lambda: print), _n_(78177, "chars", lambda: chars))
_l_(78179)
_c_(78181, _n_(78180, "print", lambda: print), 'Shift last element to first position and first element to last position of the said list:')
_l_(78182)
_c_(78187, _n_(78183, "print", lambda: print), _c_(78186, _n_(78184, "shift_first_last", lambda: shift_first_last), _n_(78185, "chars", lambda: chars)))
_l_(78188)