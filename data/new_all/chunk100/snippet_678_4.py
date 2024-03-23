# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(70274)

except ImportError:
    pass
a = _c_(70277, _a_(70276, _n_(70275, "np", lambda: np), "array"), [1, 2, 5])
_l_(70278)
b = _c_(70281, _a_(70280, _n_(70279, "np", lambda: np), "array"), [2, 1, 0])
_l_(70282)
_c_(70284, _n_(70283, "print", lambda: print), 'Original 1-d arrays:')
_l_(70285)
_c_(70288, _n_(70286, "print", lambda: print), _n_(70287, "a", lambda: a))
_l_(70289)
_c_(70292, _n_(70290, "print", lambda: print), _n_(70291, "b", lambda: b))
_l_(70293)
_n_(70294, "print", lambda: print)
_l_(70295)
result = _c_(70300, _a_(70297, _n_(70296, "np", lambda: np), "inner"), _n_(70298, "a", lambda: a), _n_(70299, "b", lambda: b))
_l_(70301)
_c_(70303, _n_(70302, "print", lambda: print), 'Inner product of the said vectors:')
_l_(70304)
y = _c_(70309, _a_(70308, _c_(70307, _a_(70306, _n_(70305, "np", lambda: np), "arange"), 3, 12), "reshape"), 3, 3)
_l_(70310)
_c_(70312, _n_(70311, "print", lambda: print), 'Higher dimension arrays:')
_l_(70313)
_c_(70316, _n_(70314, "print", lambda: print), _n_(70315, "x", lambda: x))
_l_(70317)
_c_(70320, _n_(70318, "print", lambda: print), _n_(70319, "y", lambda: y))
_l_(70321)
result = _c_(70326, _a_(70323, _n_(70322, "np", lambda: np), "inner"), _n_(70324, "x", lambda: x), _n_(70325, "y", lambda: y))
_l_(70327)
_c_(70329, _n_(70328, "print", lambda: print), 'Inner product of the said vectors:')
_l_(70330)
_c_(70333, _n_(70331, "print", lambda: print), _n_(70332, "result", lambda: result))
_l_(70334)