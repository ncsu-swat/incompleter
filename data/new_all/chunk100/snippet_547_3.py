# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def insert_elemnt_nth(lst, ele, n):
    _l_(55394)

    result = []
    _l_(55367)
    for st_idx in _c_(55373, _n_(55368, "range", lambda: range), 0, _c_(55371, _n_(55369, "len", lambda: len), _n_(55370, "lst", lambda: lst)), _n_(55372, "n", lambda: n)):
        _l_(55387)

        _c_(55380, _a_(55375, _n_(55374, "result", lambda: result), "extend"), _n_(55376, "lst", lambda: lst)[_n_(55377, "st_idx", lambda: st_idx):_n_(55378, "st_idx", lambda: st_idx) + _n_(55379, "n", lambda: n)])
        _l_(55381)
        _c_(55385, _a_(55383, _n_(55382, "result", lambda: result), "append"), _n_(55384, "ele", lambda: ele))
        _l_(55386)
    _c_(55390, _a_(55389, _n_(55388, "result", lambda: result), "pop"))
    _l_(55391)
    aux = _n_(55392, "result", lambda: result)
    _l_(55393)
    return aux
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
_l_(55395)
_c_(55397, _n_(55396, "print", lambda: print), 'Original list:')
_l_(55398)
_c_(55401, _n_(55399, "print", lambda: print), _n_(55400, "nums", lambda: nums))
_l_(55402)
i_ele = 'a'
_l_(55403)
_c_(55407, _n_(55404, "print", lambda: print), '\nInsert', _n_(55405, "i_ele", lambda: i_ele), 'in the said list after', _n_(55406, "i_ele_pos", lambda: i_ele_pos), 'nd element:')
_l_(55408)
_c_(55415, _n_(55409, "print", lambda: print), _c_(55414, _n_(55410, "insert_elemnt_nth", lambda: insert_elemnt_nth), _n_(55411, "nums", lambda: nums), _n_(55412, "i_ele", lambda: i_ele), _n_(55413, "i_ele_pos", lambda: i_ele_pos)))
_l_(55416)
i_ele = 'b'
_l_(55417)
i_ele_pos = 4
_l_(55418)
_c_(55422, _n_(55419, "print", lambda: print), '\nInsert', _n_(55420, "i_ele", lambda: i_ele), 'in the said list after', _n_(55421, "i_ele_pos", lambda: i_ele_pos), 'th element:')
_l_(55423)
_c_(55430, _n_(55424, "print", lambda: print), _c_(55429, _n_(55425, "insert_elemnt_nth", lambda: insert_elemnt_nth), _n_(55426, "nums", lambda: nums), _n_(55427, "i_ele", lambda: i_ele), _n_(55428, "i_ele_pos", lambda: i_ele_pos)))
_l_(55431)