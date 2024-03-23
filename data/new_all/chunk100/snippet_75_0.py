# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import groupby
    _l_(77172)

except ImportError:
    pass

def encode_list(s_list):
    _l_(77183)

    aux = [[_c_(77177, _n_(77173, "len", lambda: len), _c_(77176, _n_(77174, "list", lambda: list), _n_(77175, "group", lambda: group))), _n_(77178, "key", lambda: key)] for (key, group) in _c_(77181, _n_(77179, "groupby", lambda: groupby), _n_(77180, "s_list", lambda: s_list))]
    _l_(77182)
    return aux
n_list = [1, 1, 2, 3, 4, 4.3, 5, 1]
_l_(77184)
_c_(77186, _n_(77185, "print", lambda: print), 'Original list:')
_l_(77187)
_c_(77190, _n_(77188, "print", lambda: print), _n_(77189, "n_list", lambda: n_list))
_l_(77191)
_c_(77193, _n_(77192, "print", lambda: print), '\nList reflecting the run-length encoding from the said list:')
_l_(77194)
_c_(77199, _n_(77195, "print", lambda: print), _c_(77198, _n_(77196, "encode_list", lambda: encode_list), _n_(77197, "n_list", lambda: n_list)))
_l_(77200)
_c_(77202, _n_(77201, "print", lambda: print), '\nOriginal String:')
_l_(77203)
_c_(77206, _n_(77204, "print", lambda: print), _n_(77205, "n_list", lambda: n_list))
_l_(77207)
_c_(77209, _n_(77208, "print", lambda: print), '\nList reflecting the run-length encoding from the said string:')
_l_(77210)
_c_(77215, _n_(77211, "print", lambda: print), _c_(77214, _n_(77212, "encode_list", lambda: encode_list), _n_(77213, "n_list", lambda: n_list)))
_l_(77216)