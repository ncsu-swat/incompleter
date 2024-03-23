# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def swap_case_string(str1):
    _l_(30800)

    for item in _n_(30784, "str1", lambda: str1):
        _l_(30797)

        if _c_(30787, _a_(30786, _n_(30785, "item", lambda: item), "isupper")):
            _l_(30796)

            result_str += _c_(30790, _a_(30789, _n_(30788, "item", lambda: item), "lower"))
            _l_(30791)
        else:
            result_str += _c_(30794, _a_(30793, _n_(30792, "item", lambda: item), "upper"))
            _l_(30795)
    aux = _n_(30798, "result_str", lambda: result_str)
    _l_(30799)
    return aux
_c_(30804, _n_(30801, "print", lambda: print), _c_(30803, _n_(30802, "swap_case_string", lambda: swap_case_string), 'Python Exercises'))
_l_(30805)
_c_(30809, _n_(30806, "print", lambda: print), _c_(30808, _n_(30807, "swap_case_string", lambda: swap_case_string), 'Java'))
_l_(30810)
_c_(30814, _n_(30811, "print", lambda: print), _c_(30813, _n_(30812, "swap_case_string", lambda: swap_case_string), 'NumPy'))
_l_(30815)