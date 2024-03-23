# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(58267)

except ImportError:
    pass
_c_(58269, _n_(58268, "print", lambda: print), 'Original array of string values:')
_l_(58270)
_c_(58273, _n_(58271, "print", lambda: print), _n_(58272, "str1", lambda: str1))
_l_(58274)
_c_(58276, _n_(58275, "print", lambda: print), "\nReplace '-' with '=' character in the said array of string values:")
_l_(58277)
_c_(58288, _n_(58278, "print", lambda: print), _c_(58287, _a_(58281, _a_(58280, _n_(58279, "np", lambda: np), "char"), "strip"), _c_(58286, _a_(58284, _a_(58283, _n_(58282, "np", lambda: np), "char"), "replace"), _n_(58285, "str1", lambda: str1), '-', '==')))
_l_(58289)
_c_(58291, _n_(58290, "print", lambda: print), "\nReplace '-' with ' ' character in the said array of string values:")
_l_(58292)
_c_(58303, _n_(58293, "print", lambda: print), _c_(58302, _a_(58296, _a_(58295, _n_(58294, "np", lambda: np), "char"), "strip"), _c_(58301, _a_(58299, _a_(58298, _n_(58297, "np", lambda: np), "char"), "replace"), _n_(58300, "str1", lambda: str1), '-', ' ')))
_l_(58304)