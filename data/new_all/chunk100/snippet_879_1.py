# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def common_in_nested_lists(nested_list):
    _l_(86344)

    result = _c_(86340, _n_(86332, "list", lambda: list), _c_(86339, _a_(86334, _n_(86333, "set", lambda: set), "intersection"), *_c_(86338, _n_(86335, "map", lambda: map), _n_(86336, "set", lambda: set), _n_(86337, "nested_list", lambda: nested_list))))
    _l_(86341)
    aux = _n_(86342, "result", lambda: result)
    _l_(86343)
    return aux
_c_(86346, _n_(86345, "print", lambda: print), '\nOriginal lists:')
_l_(86347)
_c_(86350, _n_(86348, "print", lambda: print), _n_(86349, "nested_list", lambda: nested_list))
_l_(86351)
_c_(86353, _n_(86352, "print", lambda: print), '\nCommon element(s) in nested lists:')
_l_(86354)
_c_(86359, _n_(86355, "print", lambda: print), _c_(86358, _n_(86356, "common_in_nested_lists", lambda: common_in_nested_lists), _n_(86357, "nested_list", lambda: nested_list)))
_l_(86360)