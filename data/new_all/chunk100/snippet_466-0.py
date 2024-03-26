# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def square_num(n):
    _l_(117526)

    aux = _n_(117523, "n", lambda: n) * _n_(117524, "n", lambda: n)
    _l_(117525)
    return aux
_c_(117529, _n_(117527, "print", lambda: print), 'Original List: ', _n_(117528, "nums", lambda: nums))
_l_(117530)
result = _c_(117534, _n_(117531, "map", lambda: map), _n_(117532, "square_num", lambda: square_num), _n_(117533, "nums", lambda: nums))
_l_(117535)
_c_(117537, _n_(117536, "print", lambda: print), 'Square the elements of the said list using map():')
_l_(117538)
_c_(117543, _n_(117539, "print", lambda: print), _c_(117542, _n_(117540, "list", lambda: list), _n_(117541, "result", lambda: result)))
_l_(117544)