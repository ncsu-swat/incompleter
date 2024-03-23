# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def merge_some_chars(lst, merge_from, merge_to):
    _l_(11248)

    result = _n_(11235, "lst", lambda: lst)
    _l_(11236)
    _n_(11237, "result", lambda: result)[_n_(11238, "merge_from", lambda: merge_from):_n_(11239, "merge_to", lambda: merge_to)] = [_c_(11244, _a_(11240, '', "join"), _n_(11241, "result", lambda: result)[_n_(11242, "merge_from", lambda: merge_from):_n_(11243, "merge_to", lambda: merge_to)])]
    _l_(11245)
    aux = _n_(11246, "result", lambda: result)
    _l_(11247)
    return aux
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
_l_(11249)
_c_(11251, _n_(11250, "print", lambda: print), 'Original lists:')
_l_(11252)
_c_(11255, _n_(11253, "print", lambda: print), _n_(11254, "chars", lambda: chars))
_l_(11256)
merge_to = 4
_l_(11257)
_c_(11261, _n_(11258, "print", lambda: print), '\nMerge items from', _n_(11259, "merge_from", lambda: merge_from), 'to', _n_(11260, "merge_to", lambda: merge_to), 'in the said List:')
_l_(11262)
_c_(11269, _n_(11263, "print", lambda: print), _c_(11268, _n_(11264, "merge_some_chars", lambda: merge_some_chars), _n_(11265, "chars", lambda: chars), _n_(11266, "merge_from", lambda: merge_from), _n_(11267, "merge_to", lambda: merge_to)))
_l_(11270)
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
_l_(11271)
merge_from = 3
_l_(11272)
merge_to = 7
_l_(11273)
_c_(11277, _n_(11274, "print", lambda: print), '\nMerge items from', _n_(11275, "merge_from", lambda: merge_from), 'to', _n_(11276, "merge_to", lambda: merge_to), 'in the said List:')
_l_(11278)
_c_(11285, _n_(11279, "print", lambda: print), _c_(11284, _n_(11280, "merge_some_chars", lambda: merge_some_chars), _n_(11281, "chars", lambda: chars), _n_(11282, "merge_from", lambda: merge_from), _n_(11283, "merge_to", lambda: merge_to)))
_l_(11286)