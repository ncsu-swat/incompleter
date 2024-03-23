# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def merge_some_chars(lst, merge_from, merge_to):
    _l_(11352)

    result = _n_(11339, "lst", lambda: lst)
    _l_(11340)
    _n_(11341, "result", lambda: result)[_n_(11342, "merge_from", lambda: merge_from):_n_(11343, "merge_to", lambda: merge_to)] = [_c_(11348, _a_(11344, '', "join"), _n_(11345, "result", lambda: result)[_n_(11346, "merge_from", lambda: merge_from):_n_(11347, "merge_to", lambda: merge_to)])]
    _l_(11349)
    aux = _n_(11350, "result", lambda: result)
    _l_(11351)
    return aux
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
_l_(11353)
_c_(11355, _n_(11354, "print", lambda: print), 'Original lists:')
_l_(11356)
_c_(11359, _n_(11357, "print", lambda: print), _n_(11358, "chars", lambda: chars))
_l_(11360)
merge_from = 2
_l_(11361)
_c_(11365, _n_(11362, "print", lambda: print), '\nMerge items from', _n_(11363, "merge_from", lambda: merge_from), 'to', _n_(11364, "merge_to", lambda: merge_to), 'in the said List:')
_l_(11366)
_c_(11373, _n_(11367, "print", lambda: print), _c_(11372, _n_(11368, "merge_some_chars", lambda: merge_some_chars), _n_(11369, "chars", lambda: chars), _n_(11370, "merge_from", lambda: merge_from), _n_(11371, "merge_to", lambda: merge_to)))
_l_(11374)
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
_l_(11375)
merge_from = 3
_l_(11376)
merge_to = 7
_l_(11377)
_c_(11381, _n_(11378, "print", lambda: print), '\nMerge items from', _n_(11379, "merge_from", lambda: merge_from), 'to', _n_(11380, "merge_to", lambda: merge_to), 'in the said List:')
_l_(11382)
_c_(11389, _n_(11383, "print", lambda: print), _c_(11388, _n_(11384, "merge_some_chars", lambda: merge_some_chars), _n_(11385, "chars", lambda: chars), _n_(11386, "merge_from", lambda: merge_from), _n_(11387, "merge_to", lambda: merge_to)))
_l_(11390)