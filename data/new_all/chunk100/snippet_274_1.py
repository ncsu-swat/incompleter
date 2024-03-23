# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import accumulate
    _l_(22148)

except ImportError:
    pass

def cumsum(lst):
    _l_(22155)

    aux = _c_(22153, _n_(22149, "list", lambda: list), _c_(22152, _n_(22150, "accumulate", lambda: accumulate), _n_(22151, "lst", lambda: lst)))
    _l_(22154)
    return aux
nums = [1, 2, 3, 4]
_l_(22156)
_c_(22158, _n_(22157, "print", lambda: print), 'Original list elements:')
_l_(22159)
_c_(22162, _n_(22160, "print", lambda: print), _n_(22161, "nums", lambda: nums))
_l_(22163)
_c_(22165, _n_(22164, "print", lambda: print), 'Cumulative sum of the elements of the said list:')
_l_(22166)
_c_(22171, _n_(22167, "print", lambda: print), _c_(22170, _n_(22168, "cumsum", lambda: cumsum), _n_(22169, "nums", lambda: nums)))
_l_(22172)
_c_(22174, _n_(22173, "print", lambda: print), '\nOriginal list elements:')
_l_(22175)
_c_(22178, _n_(22176, "print", lambda: print), _n_(22177, "nums", lambda: nums))
_l_(22179)
_c_(22181, _n_(22180, "print", lambda: print), 'Cumulative sum of the elements of the said list:')
_l_(22182)
_c_(22187, _n_(22183, "print", lambda: print), _c_(22186, _n_(22184, "cumsum", lambda: cumsum), _n_(22185, "nums", lambda: nums)))
_l_(22188)