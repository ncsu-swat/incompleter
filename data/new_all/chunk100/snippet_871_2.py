# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from operator import itemgetter
    _l_(86056)

except ImportError:
    pass

def index_on_inner_list(list_data, index_no):
    _l_(86066)

    result = _c_(86062, _n_(86057, "sorted", lambda: sorted), _n_(86058, "list_data", lambda: list_data), key=_c_(86061, _n_(86059, "itemgetter", lambda: itemgetter), _n_(86060, "index_no", lambda: index_no)))
    _l_(86063)
    aux = _n_(86064, "result", lambda: result)
    _l_(86065)
    return aux
_c_(86068, _n_(86067, "print", lambda: print), 'Original list:')
_l_(86069)
_c_(86072, _n_(86070, "print", lambda: print), _n_(86071, "students", lambda: students))
_l_(86073)
index_no = 0
_l_(86074)
_c_(86077, _n_(86075, "print", lambda: print), '\nSort the said list of lists by a given index', '( Index = ', _n_(86076, "index_no", lambda: index_no), ') of the inner list')
_l_(86078)
_c_(86084, _n_(86079, "print", lambda: print), _c_(86083, _n_(86080, "index_on_inner_list", lambda: index_on_inner_list), _n_(86081, "students", lambda: students), _n_(86082, "index_no", lambda: index_no)))
_l_(86085)
index_no = 2
_l_(86086)
_c_(86089, _n_(86087, "print", lambda: print), '\nSort the said list of lists by a given index', '( Index = ', _n_(86088, "index_no", lambda: index_no), ') of the inner list')
_l_(86090)
_c_(86096, _n_(86091, "print", lambda: print), _c_(86095, _n_(86092, "index_on_inner_list", lambda: index_on_inner_list), _n_(86093, "students", lambda: students), _n_(86094, "index_no", lambda: index_no)))
_l_(86097)