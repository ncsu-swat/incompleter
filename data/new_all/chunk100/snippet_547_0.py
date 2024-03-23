# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def insert_elemnt_nth(lst, ele, n):
    _l_(55199)

    result = []
    _l_(55172)
    for st_idx in _c_(55178, _n_(55173, "range", lambda: range), 0, _c_(55176, _n_(55174, "len", lambda: len), _n_(55175, "lst", lambda: lst)), _n_(55177, "n", lambda: n)):
        _l_(55192)

        _c_(55185, _a_(55180, _n_(55179, "result", lambda: result), "extend"), _n_(55181, "lst", lambda: lst)[_n_(55182, "st_idx", lambda: st_idx):_n_(55183, "st_idx", lambda: st_idx) + _n_(55184, "n", lambda: n)])
        _l_(55186)
        _c_(55190, _a_(55188, _n_(55187, "result", lambda: result), "append"), _n_(55189, "ele", lambda: ele))
        _l_(55191)
    _c_(55195, _a_(55194, _n_(55193, "result", lambda: result), "pop"))
    _l_(55196)
    aux = _n_(55197, "result", lambda: result)
    _l_(55198)
    return aux
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
_l_(55200)
_c_(55202, _n_(55201, "print", lambda: print), 'Original list:')
_l_(55203)
_c_(55206, _n_(55204, "print", lambda: print), _n_(55205, "nums", lambda: nums))
_l_(55207)
i_ele = 'a'
_l_(55208)
i_ele_pos = 2
_l_(55209)
_c_(55213, _n_(55210, "print", lambda: print), '\nInsert', _n_(55211, "i_ele", lambda: i_ele), 'in the said list after', _n_(55212, "i_ele_pos", lambda: i_ele_pos), 'nd element:')
_l_(55214)
_c_(55221, _n_(55215, "print", lambda: print), _c_(55220, _n_(55216, "insert_elemnt_nth", lambda: insert_elemnt_nth), _n_(55217, "nums", lambda: nums), _n_(55218, "i_ele", lambda: i_ele), _n_(55219, "i_ele_pos", lambda: i_ele_pos)))
_l_(55222)
i_ele = 'b'
_l_(55223)
_c_(55227, _n_(55224, "print", lambda: print), '\nInsert', _n_(55225, "i_ele", lambda: i_ele), 'in the said list after', _n_(55226, "i_ele_pos", lambda: i_ele_pos), 'th element:')
_l_(55228)
_c_(55235, _n_(55229, "print", lambda: print), _c_(55234, _n_(55230, "insert_elemnt_nth", lambda: insert_elemnt_nth), _n_(55231, "nums", lambda: nums), _n_(55232, "i_ele", lambda: i_ele), _n_(55233, "i_ele_pos", lambda: i_ele_pos)))
_l_(55236)