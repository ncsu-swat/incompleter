# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from operator import itemgetter
    _l_(86013)

except ImportError:
    pass

def index_on_inner_list(list_data, index_no):
    _l_(86023)

    result = _c_(86019, _n_(86014, "sorted", lambda: sorted), _n_(86015, "list_data", lambda: list_data), key=_c_(86018, _n_(86016, "itemgetter", lambda: itemgetter), _n_(86017, "index_no", lambda: index_no)))
    _l_(86020)
    aux = _n_(86021, "result", lambda: result)
    _l_(86022)
    return aux
students = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
_l_(86024)
_c_(86026, _n_(86025, "print", lambda: print), 'Original list:')
_l_(86027)
_c_(86030, _n_(86028, "print", lambda: print), _n_(86029, "students", lambda: students))
_l_(86031)
_c_(86034, _n_(86032, "print", lambda: print), '\nSort the said list of lists by a given index', '( Index = ', _n_(86033, "index_no", lambda: index_no), ') of the inner list')
_l_(86035)
_c_(86041, _n_(86036, "print", lambda: print), _c_(86040, _n_(86037, "index_on_inner_list", lambda: index_on_inner_list), _n_(86038, "students", lambda: students), _n_(86039, "index_no", lambda: index_no)))
_l_(86042)
index_no = 2
_l_(86043)
_c_(86046, _n_(86044, "print", lambda: print), '\nSort the said list of lists by a given index', '( Index = ', _n_(86045, "index_no", lambda: index_no), ') of the inner list')
_l_(86047)
_c_(86053, _n_(86048, "print", lambda: print), _c_(86052, _n_(86049, "index_on_inner_list", lambda: index_on_inner_list), _n_(86050, "students", lambda: students), _n_(86051, "index_no", lambda: index_no)))
_l_(86054)