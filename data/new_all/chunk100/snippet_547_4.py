# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def insert_elemnt_nth(lst, ele, n):
    _l_(55459)

    result = []
    _l_(55432)
    for st_idx in _c_(55438, _n_(55433, "range", lambda: range), 0, _c_(55436, _n_(55434, "len", lambda: len), _n_(55435, "lst", lambda: lst)), _n_(55437, "n", lambda: n)):
        _l_(55452)

        _c_(55445, _a_(55440, _n_(55439, "result", lambda: result), "extend"), _n_(55441, "lst", lambda: lst)[_n_(55442, "st_idx", lambda: st_idx):_n_(55443, "st_idx", lambda: st_idx) + _n_(55444, "n", lambda: n)])
        _l_(55446)
        _c_(55450, _a_(55448, _n_(55447, "result", lambda: result), "append"), _n_(55449, "ele", lambda: ele))
        _l_(55451)
    _c_(55455, _a_(55454, _n_(55453, "result", lambda: result), "pop"))
    _l_(55456)
    aux = _n_(55457, "result", lambda: result)
    _l_(55458)
    return aux
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
_l_(55460)
_c_(55462, _n_(55461, "print", lambda: print), 'Original list:')
_l_(55463)
_c_(55466, _n_(55464, "print", lambda: print), _n_(55465, "nums", lambda: nums))
_l_(55467)
i_ele = 'a'
_l_(55468)
i_ele_pos = 2
_l_(55469)
_c_(55473, _n_(55470, "print", lambda: print), '\nInsert', _n_(55471, "i_ele", lambda: i_ele), 'in the said list after', _n_(55472, "i_ele_pos", lambda: i_ele_pos), 'nd element:')
_l_(55474)
_c_(55481, _n_(55475, "print", lambda: print), _c_(55480, _n_(55476, "insert_elemnt_nth", lambda: insert_elemnt_nth), _n_(55477, "nums", lambda: nums), _n_(55478, "i_ele", lambda: i_ele), _n_(55479, "i_ele_pos", lambda: i_ele_pos)))
_l_(55482)
i_ele_pos = 4
_l_(55483)
_c_(55487, _n_(55484, "print", lambda: print), '\nInsert', _n_(55485, "i_ele", lambda: i_ele), 'in the said list after', _n_(55486, "i_ele_pos", lambda: i_ele_pos), 'th element:')
_l_(55488)
_c_(55495, _n_(55489, "print", lambda: print), _c_(55494, _n_(55490, "insert_elemnt_nth", lambda: insert_elemnt_nth), _n_(55491, "nums", lambda: nums), _n_(55492, "i_ele", lambda: i_ele), _n_(55493, "i_ele_pos", lambda: i_ele_pos)))
_l_(55496)