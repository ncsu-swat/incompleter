# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def insert_elemnt_nth(lst, ele, n):
    _l_(55524)

    result = []
    _l_(55497)
    for st_idx in _c_(55503, _n_(55498, "range", lambda: range), 0, _c_(55501, _n_(55499, "len", lambda: len), _n_(55500, "lst", lambda: lst)), _n_(55502, "n", lambda: n)):
        _l_(55517)

        _c_(55510, _a_(55505, _n_(55504, "result", lambda: result), "extend"), _n_(55506, "lst", lambda: lst)[_n_(55507, "st_idx", lambda: st_idx):_n_(55508, "st_idx", lambda: st_idx) + _n_(55509, "n", lambda: n)])
        _l_(55511)
        _c_(55515, _a_(55513, _n_(55512, "result", lambda: result), "append"), _n_(55514, "ele", lambda: ele))
        _l_(55516)
    _c_(55520, _a_(55519, _n_(55518, "result", lambda: result), "pop"))
    _l_(55521)
    aux = _n_(55522, "result", lambda: result)
    _l_(55523)
    return aux
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
_l_(55525)
_c_(55527, _n_(55526, "print", lambda: print), 'Original list:')
_l_(55528)
_c_(55531, _n_(55529, "print", lambda: print), _n_(55530, "nums", lambda: nums))
_l_(55532)
i_ele_pos = 2
_l_(55533)
_c_(55537, _n_(55534, "print", lambda: print), '\nInsert', _n_(55535, "i_ele", lambda: i_ele), 'in the said list after', _n_(55536, "i_ele_pos", lambda: i_ele_pos), 'nd element:')
_l_(55538)
_c_(55545, _n_(55539, "print", lambda: print), _c_(55544, _n_(55540, "insert_elemnt_nth", lambda: insert_elemnt_nth), _n_(55541, "nums", lambda: nums), _n_(55542, "i_ele", lambda: i_ele), _n_(55543, "i_ele_pos", lambda: i_ele_pos)))
_l_(55546)
i_ele = 'b'
_l_(55547)
i_ele_pos = 4
_l_(55548)
_c_(55552, _n_(55549, "print", lambda: print), '\nInsert', _n_(55550, "i_ele", lambda: i_ele), 'in the said list after', _n_(55551, "i_ele_pos", lambda: i_ele_pos), 'th element:')
_l_(55553)
_c_(55560, _n_(55554, "print", lambda: print), _c_(55559, _n_(55555, "insert_elemnt_nth", lambda: insert_elemnt_nth), _n_(55556, "nums", lambda: nums), _n_(55557, "i_ele", lambda: i_ele), _n_(55558, "i_ele_pos", lambda: i_ele_pos)))
_l_(55561)