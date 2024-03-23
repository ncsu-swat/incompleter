# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import groupby
    _l_(88124)

except ImportError:
    pass

def pack_consecutive_duplicates(l_nums):
    _l_(88132)

    aux = [_c_(88127, _n_(88125, "list", lambda: list), _n_(88126, "group", lambda: group)) for (key, group) in _c_(88130, _n_(88128, "groupby", lambda: groupby), _n_(88129, "l_nums", lambda: l_nums))]
    _l_(88131)
    return aux
_c_(88134, _n_(88133, "print", lambda: print), 'Original list:')
_l_(88135)
_c_(88138, _n_(88136, "print", lambda: print), _n_(88137, "n_list", lambda: n_list))
_l_(88139)
_c_(88141, _n_(88140, "print", lambda: print), '\nAfter packing consecutive duplicates of the said list elements into sublists:')
_l_(88142)
_c_(88147, _n_(88143, "print", lambda: print), _c_(88146, _n_(88144, "pack_consecutive_duplicates", lambda: pack_consecutive_duplicates), _n_(88145, "n_list", lambda: n_list)))
_l_(88148)