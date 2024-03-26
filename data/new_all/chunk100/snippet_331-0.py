# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(110716)

except ImportError:
    pass
_c_(110718, _n_(110717, "print", lambda: print), 'Original DataFrame:')
_l_(110719)
_c_(110722, _n_(110720, "print", lambda: print), _n_(110721, "df", lambda: df))
_l_(110723)
_c_(110725, _n_(110724, "print", lambda: print), '\nIs lower (company_code)?')
_l_(110726)
_n_(110727, "df", lambda: df)['company_code_ul_cases'] = _c_(110735, _n_(110728, "list", lambda: list), _c_(110734, _n_(110729, "map", lambda: map), lambda x: _c_(110732, _a_(110731, _n_(110730, "x", lambda: x), "islower")), _n_(110733, "df", lambda: df)['company_code']))
_l_(110736)
_c_(110739, _n_(110737, "print", lambda: print), _n_(110738, "df", lambda: df))
_l_(110740)
_c_(110742, _n_(110741, "print", lambda: print), '\nIs Upper (company_code)?')
_l_(110743)
_n_(110744, "df", lambda: df)['company_code_ul_cases'] = _c_(110752, _n_(110745, "list", lambda: list), _c_(110751, _n_(110746, "map", lambda: map), lambda x: _c_(110749, _a_(110748, _n_(110747, "x", lambda: x), "isupper")), _n_(110750, "df", lambda: df)['company_code']))
_l_(110753)
_c_(110756, _n_(110754, "print", lambda: print), _n_(110755, "df", lambda: df))
_l_(110757)