# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def insert_elemnt_nth(lst, ele, n):
    _l_(55263)

    for st_idx in _c_(55242, _n_(55237, "range", lambda: range), 0, _c_(55240, _n_(55238, "len", lambda: len), _n_(55239, "lst", lambda: lst)), _n_(55241, "n", lambda: n)):
        _l_(55256)

        _c_(55249, _a_(55244, _n_(55243, "result", lambda: result), "extend"), _n_(55245, "lst", lambda: lst)[_n_(55246, "st_idx", lambda: st_idx):_n_(55247, "st_idx", lambda: st_idx) + _n_(55248, "n", lambda: n)])
        _l_(55250)
        _c_(55254, _a_(55252, _n_(55251, "result", lambda: result), "append"), _n_(55253, "ele", lambda: ele))
        _l_(55255)
    _c_(55259, _a_(55258, _n_(55257, "result", lambda: result), "pop"))
    _l_(55260)
    aux = _n_(55261, "result", lambda: result)
    _l_(55262)
    return aux
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
_l_(55264)
_c_(55266, _n_(55265, "print", lambda: print), 'Original list:')
_l_(55267)
_c_(55270, _n_(55268, "print", lambda: print), _n_(55269, "nums", lambda: nums))
_l_(55271)
i_ele = 'a'
_l_(55272)
i_ele_pos = 2
_l_(55273)
_c_(55277, _n_(55274, "print", lambda: print), '\nInsert', _n_(55275, "i_ele", lambda: i_ele), 'in the said list after', _n_(55276, "i_ele_pos", lambda: i_ele_pos), 'nd element:')
_l_(55278)
_c_(55285, _n_(55279, "print", lambda: print), _c_(55284, _n_(55280, "insert_elemnt_nth", lambda: insert_elemnt_nth), _n_(55281, "nums", lambda: nums), _n_(55282, "i_ele", lambda: i_ele), _n_(55283, "i_ele_pos", lambda: i_ele_pos)))
_l_(55286)
i_ele = 'b'
_l_(55287)
i_ele_pos = 4
_l_(55288)
_c_(55292, _n_(55289, "print", lambda: print), '\nInsert', _n_(55290, "i_ele", lambda: i_ele), 'in the said list after', _n_(55291, "i_ele_pos", lambda: i_ele_pos), 'th element:')
_l_(55293)
_c_(55300, _n_(55294, "print", lambda: print), _c_(55299, _n_(55295, "insert_elemnt_nth", lambda: insert_elemnt_nth), _n_(55296, "nums", lambda: nums), _n_(55297, "i_ele", lambda: i_ele), _n_(55298, "i_ele_pos", lambda: i_ele_pos)))
_l_(55301)