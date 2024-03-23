# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(54606)

except ImportError:
    pass
student = '01\tV\tDebby Pramod\n02\tV\tArtemiy Ellie\n03\tV\tBaptist Kamal\n04\tV\tLavanya Davide\n05\tV\tFulton Antwan\n06\tV\tEuanthe Sandeep\n07\tV\tEndzela Sanda\n08\tV\tVictoire Waman\n09\tV\tBriar Nur\n10\tV\tRose Lykos'
_l_(54607)
_c_(54609, _n_(54608, "print", lambda: print), 'Original text:')
_l_(54610)
_c_(54613, _n_(54611, "print", lambda: print), _n_(54612, "student", lambda: student))
_l_(54614)
text_lines = _c_(54617, _a_(54616, _n_(54615, "student", lambda: student), "splitlines"))
_l_(54618)
result = _c_(54624, _a_(54620, _n_(54619, "np", lambda: np), "array"), _n_(54621, "text_lines", lambda: text_lines), dtype=_a_(54623, _n_(54622, "np", lambda: np), "str"))
_l_(54625)
_c_(54627, _n_(54626, "print", lambda: print), '\nArray from the said text:')
_l_(54628)
_c_(54631, _n_(54629, "print", lambda: print), _n_(54630, "result", lambda: result))
_l_(54632)