# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import groupby
    _l_(119979)

except ImportError:
    pass

def encode_list(s_list):
    _l_(119990)

    aux = [[_c_(119984, _n_(119980, "len", lambda: len), _c_(119983, _n_(119981, "list", lambda: list), _n_(119982, "group", lambda: group))), _n_(119985, "key", lambda: key)] for key, group in _c_(119988, _n_(119986, "groupby", lambda: groupby), _n_(119987, "s_list", lambda: s_list))]
    _l_(119989)
    return aux
_c_(119992, _n_(119991, "print", lambda: print), 'Original list:')
_l_(119993)
_c_(119996, _n_(119994, "print", lambda: print), _n_(119995, "n_list", lambda: n_list))
_l_(119997)
_c_(119999, _n_(119998, "print", lambda: print), '\nList reflecting the run-length encoding from the said list:')
_l_(120000)
_c_(120005, _n_(120001, "print", lambda: print), _c_(120004, _n_(120002, "encode_list", lambda: encode_list), _n_(120003, "n_list", lambda: n_list)))
_l_(120006)
n_list = 'automatically'
_l_(120007)
_c_(120009, _n_(120008, "print", lambda: print), '\nOriginal String:')
_l_(120010)
_c_(120013, _n_(120011, "print", lambda: print), _n_(120012, "n_list", lambda: n_list))
_l_(120014)
_c_(120016, _n_(120015, "print", lambda: print), '\nList reflecting the run-length encoding from the said string:')
_l_(120017)
_c_(120022, _n_(120018, "print", lambda: print), _c_(120021, _n_(120019, "encode_list", lambda: encode_list), _n_(120020, "n_list", lambda: n_list)))
_l_(120023)