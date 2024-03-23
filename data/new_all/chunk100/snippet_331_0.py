# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(33104)

except ImportError:
    pass
_c_(33106, _n_(33105, "print", lambda: print), 'Original DataFrame:')
_l_(33107)
_c_(33110, _n_(33108, "print", lambda: print), _n_(33109, "df", lambda: df))
_l_(33111)
_c_(33113, _n_(33112, "print", lambda: print), '\nIs lower (company_code)?')
_l_(33114)
_n_(33115, "df", lambda: df)['company_code_ul_cases'] = _c_(33123, _n_(33116, "list", lambda: list), _c_(33122, _n_(33117, "map", lambda: map), lambda x: _c_(33120, _a_(33119, _n_(33118, "x", lambda: x), "islower")), _n_(33121, "df", lambda: df)['company_code']))
_l_(33124)
_c_(33127, _n_(33125, "print", lambda: print), _n_(33126, "df", lambda: df))
_l_(33128)
_c_(33130, _n_(33129, "print", lambda: print), '\nIs Upper (company_code)?')
_l_(33131)
_n_(33132, "df", lambda: df)['company_code_ul_cases'] = _c_(33140, _n_(33133, "list", lambda: list), _c_(33139, _n_(33134, "map", lambda: map), lambda x: _c_(33137, _a_(33136, _n_(33135, "x", lambda: x), "isupper")), _n_(33138, "df", lambda: df)['company_code']))
_l_(33141)
_c_(33144, _n_(33142, "print", lambda: print), _n_(33143, "df", lambda: df))
_l_(33145)