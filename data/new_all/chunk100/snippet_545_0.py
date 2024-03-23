# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(54545)

except ImportError:
    pass
student = '01\tV\tDebby Pramod\n02\tV\tArtemiy Ellie\n03\tV\tBaptist Kamal\n04\tV\tLavanya Davide\n05\tV\tFulton Antwan\n06\tV\tEuanthe Sandeep\n07\tV\tEndzela Sanda\n08\tV\tVictoire Waman\n09\tV\tBriar Nur\n10\tV\tRose Lykos'
_l_(54546)
_c_(54548, _n_(54547, "print", lambda: print), 'Original text:')
_l_(54549)
_c_(54552, _n_(54550, "print", lambda: print), _n_(54551, "student", lambda: student))
_l_(54553)
text_lines = [_c_(54556, _a_(54555, _n_(54554, "r", lambda: r), "split"), '\t') for r in _n_(54557, "text_lines", lambda: text_lines)]
_l_(54558)
result = _c_(54564, _a_(54560, _n_(54559, "np", lambda: np), "array"), _n_(54561, "text_lines", lambda: text_lines), dtype=_a_(54563, _n_(54562, "np", lambda: np), "str"))
_l_(54565)
_c_(54567, _n_(54566, "print", lambda: print), '\nArray from the said text:')
_l_(54568)
_c_(54571, _n_(54569, "print", lambda: print), _n_(54570, "result", lambda: result))
_l_(54572)