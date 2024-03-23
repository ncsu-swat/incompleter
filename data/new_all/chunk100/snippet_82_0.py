# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import groupby
    _l_(82957)

except ImportError:
    pass
_c_(82959, _n_(82958, "print", lambda: print), 'Original list:')
_l_(82960)
_c_(82963, _n_(82961, "print", lambda: print), _n_(82962, "uno_list", lambda: uno_list))
_l_(82964)
_c_(82967, _a_(82966, _n_(82965, "uno_list", lambda: uno_list), "sort"))
_l_(82968)
_c_(82971, _n_(82969, "print", lambda: print), _n_(82970, "uno_list", lambda: uno_list))
_l_(82972)
_c_(82974, _n_(82973, "print", lambda: print), '\nSort the said unordered list:')
_l_(82975)
_c_(82978, _n_(82976, "print", lambda: print), _n_(82977, "uno_list", lambda: uno_list))
_l_(82979)
_c_(82981, _n_(82980, "print", lambda: print), '\nFrequency of the elements of the said unordered list:')
_l_(82982)
result = [_c_(82987, _n_(82983, "len", lambda: len), _c_(82986, _n_(82984, "list", lambda: list), _n_(82985, "group", lambda: group))) for (key, group) in _c_(82990, _n_(82988, "groupby", lambda: groupby), _n_(82989, "uno_list", lambda: uno_list))]
_l_(82991)
_c_(82994, _n_(82992, "print", lambda: print), _n_(82993, "result", lambda: result))
_l_(82995)