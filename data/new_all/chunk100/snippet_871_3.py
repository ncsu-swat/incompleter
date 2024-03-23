# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from operator import itemgetter
    _l_(86099)

except ImportError:
    pass

def index_on_inner_list(list_data, index_no):
    _l_(86109)

    result = _c_(86105, _n_(86100, "sorted", lambda: sorted), _n_(86101, "list_data", lambda: list_data), key=_c_(86104, _n_(86102, "itemgetter", lambda: itemgetter), _n_(86103, "index_no", lambda: index_no)))
    _l_(86106)
    aux = _n_(86107, "result", lambda: result)
    _l_(86108)
    return aux
students = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
_l_(86110)
_c_(86112, _n_(86111, "print", lambda: print), 'Original list:')
_l_(86113)
_c_(86116, _n_(86114, "print", lambda: print), _n_(86115, "students", lambda: students))
_l_(86117)
index_no = 0
_l_(86118)
_c_(86121, _n_(86119, "print", lambda: print), '\nSort the said list of lists by a given index', '( Index = ', _n_(86120, "index_no", lambda: index_no), ') of the inner list')
_l_(86122)
_c_(86128, _n_(86123, "print", lambda: print), _c_(86127, _n_(86124, "index_on_inner_list", lambda: index_on_inner_list), _n_(86125, "students", lambda: students), _n_(86126, "index_no", lambda: index_no)))
_l_(86129)
_c_(86132, _n_(86130, "print", lambda: print), '\nSort the said list of lists by a given index', '( Index = ', _n_(86131, "index_no", lambda: index_no), ') of the inner list')
_l_(86133)
_c_(86139, _n_(86134, "print", lambda: print), _c_(86138, _n_(86135, "index_on_inner_list", lambda: index_on_inner_list), _n_(86136, "students", lambda: students), _n_(86137, "index_no", lambda: index_no)))
_l_(86140)