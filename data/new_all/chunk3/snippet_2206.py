# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58138056/summing-a-list-of-floatstypeerror-int-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
range_list = _c_(532468, _n_(532467, "range", lambda: range), 1, 97)
_l_(532469)


for p in _n_(532470, "range_list", lambda: range_list):
    _l_(532490)


    p_numerator = 4*((-1)**(_n_(532471, "p", lambda: p)+1))
    _l_(532472)
    p_denominator = 2*_n_(532473, "p", lambda: p) - 1
    _l_(532474)

    function_ofK = _c_(532477, _n_(532475, "float", lambda: float), _n_(532476, "p_numerator", lambda: p_numerator))/_c_(532480, _n_(532478, "float", lambda: float), _n_(532479, "p_denominator", lambda: p_denominator))
    _l_(532481)


    total = _c_(532484, _n_(532482, "sum", lambda: sum), _n_(532483, "function_ofK", lambda: function_ofK))
    _l_(532485)
    _c_(532488, _n_(532486, "print", lambda: print), _n_(532487, "total", lambda: total))
    _l_(532489)