# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def square_num(n):
    _l_(49356)

    aux = _n_(49353, "n", lambda: n) * _n_(49354, "n", lambda: n)
    _l_(49355)
    return aux
_c_(49359, _n_(49357, "print", lambda: print), 'Original List: ', _n_(49358, "nums", lambda: nums))
_l_(49360)
result = _c_(49364, _n_(49361, "map", lambda: map), _n_(49362, "square_num", lambda: square_num), _n_(49363, "nums", lambda: nums))
_l_(49365)
_c_(49367, _n_(49366, "print", lambda: print), 'Square the elements of the said list using map():')
_l_(49368)
_c_(49373, _n_(49369, "print", lambda: print), _c_(49372, _n_(49370, "list", lambda: list), _n_(49371, "result", lambda: result)))
_l_(49374)