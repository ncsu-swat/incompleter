# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/646644/how-to-get-last-items-of-a-list-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(64717, "num_list", lambda: num_list)[-9:]
_l_(64718)

_n_(64719, "sequence", lambda: sequence)[_n_(64720, "start", lambda: start):_n_(64721, "stop", lambda: stop):_n_(64722, "step", lambda: step)]
_l_(64723)

list_copy = _n_(64724, "sequence", lambda: sequence)[:]
_l_(64725)

del my_list[:]
_l_(64726)

last_nine_slice = _c_(64728, _n_(64727, "slice", lambda: slice), -9, None)
_l_(64729)

_c_(64733, _n_(64730, "list", lambda: list), _c_(64732, _n_(64731, "range", lambda: range), 100))[_n_(64734, "last_nine_slice", lambda: last_nine_slice)]
_l_(64735)
[91, 92, 93, 94, 95, 96, 97, 98, 99]
_l_(64736)
try:
    from itertools import islice
    _l_(64738)

except ImportError:
    pass
_c_(64744, _n_(64739, "islice", lambda: islice), _c_(64743, _n_(64740, "reversed", lambda: reversed), _c_(64742, _n_(64741, "range", lambda: range), 100)), 0, 9)
_l_(64745)

_c_(64753, _n_(64746, "list", lambda: list), _c_(64752, _n_(64747, "islice", lambda: islice), _c_(64751, _n_(64748, "reversed", lambda: reversed), _c_(64750, _n_(64749, "range", lambda: range), 100)), 0, 9))
_l_(64754)
[99, 98, 97, 96, 95, 94, 93, 92, 91]
_l_(64755)

