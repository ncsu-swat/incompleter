# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def insert_elemnt_nth(lst, ele, n):
    _l_(55329)

    result = []
    _l_(55302)
    for st_idx in _c_(55308, _n_(55303, "range", lambda: range), 0, _c_(55306, _n_(55304, "len", lambda: len), _n_(55305, "lst", lambda: lst)), _n_(55307, "n", lambda: n)):
        _l_(55322)

        _c_(55315, _a_(55310, _n_(55309, "result", lambda: result), "extend"), _n_(55311, "lst", lambda: lst)[_n_(55312, "st_idx", lambda: st_idx):_n_(55313, "st_idx", lambda: st_idx) + _n_(55314, "n", lambda: n)])
        _l_(55316)
        _c_(55320, _a_(55318, _n_(55317, "result", lambda: result), "append"), _n_(55319, "ele", lambda: ele))
        _l_(55321)
    _c_(55325, _a_(55324, _n_(55323, "result", lambda: result), "pop"))
    _l_(55326)
    aux = _n_(55327, "result", lambda: result)
    _l_(55328)
    return aux
_c_(55331, _n_(55330, "print", lambda: print), 'Original list:')
_l_(55332)
_c_(55335, _n_(55333, "print", lambda: print), _n_(55334, "nums", lambda: nums))
_l_(55336)
i_ele = 'a'
_l_(55337)
i_ele_pos = 2
_l_(55338)
_c_(55342, _n_(55339, "print", lambda: print), '\nInsert', _n_(55340, "i_ele", lambda: i_ele), 'in the said list after', _n_(55341, "i_ele_pos", lambda: i_ele_pos), 'nd element:')
_l_(55343)
_c_(55350, _n_(55344, "print", lambda: print), _c_(55349, _n_(55345, "insert_elemnt_nth", lambda: insert_elemnt_nth), _n_(55346, "nums", lambda: nums), _n_(55347, "i_ele", lambda: i_ele), _n_(55348, "i_ele_pos", lambda: i_ele_pos)))
_l_(55351)
i_ele = 'b'
_l_(55352)
i_ele_pos = 4
_l_(55353)
_c_(55357, _n_(55354, "print", lambda: print), '\nInsert', _n_(55355, "i_ele", lambda: i_ele), 'in the said list after', _n_(55356, "i_ele_pos", lambda: i_ele_pos), 'th element:')
_l_(55358)
_c_(55365, _n_(55359, "print", lambda: print), _c_(55364, _n_(55360, "insert_elemnt_nth", lambda: insert_elemnt_nth), _n_(55361, "nums", lambda: nums), _n_(55362, "i_ele", lambda: i_ele), _n_(55363, "i_ele_pos", lambda: i_ele_pos)))
_l_(55366)