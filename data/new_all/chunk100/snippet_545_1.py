# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(54574)

except ImportError:
    pass
_c_(54576, _n_(54575, "print", lambda: print), 'Original text:')
_l_(54577)
_c_(54580, _n_(54578, "print", lambda: print), _n_(54579, "student", lambda: student))
_l_(54581)
text_lines = _c_(54584, _a_(54583, _n_(54582, "student", lambda: student), "splitlines"))
_l_(54585)
text_lines = [_c_(54588, _a_(54587, _n_(54586, "r", lambda: r), "split"), '\t') for r in _n_(54589, "text_lines", lambda: text_lines)]
_l_(54590)
result = _c_(54596, _a_(54592, _n_(54591, "np", lambda: np), "array"), _n_(54593, "text_lines", lambda: text_lines), dtype=_a_(54595, _n_(54594, "np", lambda: np), "str"))
_l_(54597)
_c_(54599, _n_(54598, "print", lambda: print), '\nArray from the said text:')
_l_(54600)
_c_(54603, _n_(54601, "print", lambda: print), _n_(54602, "result", lambda: result))
_l_(54604)