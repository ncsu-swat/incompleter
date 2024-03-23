# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_last_n(nums, N):
    _l_(11923)

    result = _n_(11915, "nums", lambda: nums)[:_c_(11918, _n_(11916, "len", lambda: len), _n_(11917, "nums", lambda: nums)) - _n_(11919, "N", lambda: N)]
    _l_(11920)
    aux = _n_(11921, "result", lambda: result)
    _l_(11922)
    return aux
nums = [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
_l_(11924)
_c_(11926, _n_(11925, "print", lambda: print), 'Original lists:')
_l_(11927)
_c_(11930, _n_(11928, "print", lambda: print), _n_(11929, "nums", lambda: nums))
_l_(11931)
N = 3
_l_(11932)
_c_(11935, _n_(11933, "print", lambda: print), '\nRemove the last', _n_(11934, "N", lambda: N), 'elements from the said list:')
_l_(11936)
_c_(11942, _n_(11937, "print", lambda: print), _c_(11941, _n_(11938, "remove_last_n", lambda: remove_last_n), _n_(11939, "nums", lambda: nums), _n_(11940, "N", lambda: N)))
_l_(11943)
_c_(11946, _n_(11944, "print", lambda: print), '\nRemove the last', _n_(11945, "N", lambda: N), 'elements from the said list:')
_l_(11947)
_c_(11953, _n_(11948, "print", lambda: print), _c_(11952, _n_(11949, "remove_last_n", lambda: remove_last_n), _n_(11950, "nums", lambda: nums), _n_(11951, "N", lambda: N)))
_l_(11954)
N = 1
_l_(11955)
_c_(11958, _n_(11956, "print", lambda: print), '\nRemove the last', _n_(11957, "N", lambda: N), 'element from the said list:')
_l_(11959)
_c_(11965, _n_(11960, "print", lambda: print), _c_(11964, _n_(11961, "remove_last_n", lambda: remove_last_n), _n_(11962, "nums", lambda: nums), _n_(11963, "N", lambda: N)))
_l_(11966)