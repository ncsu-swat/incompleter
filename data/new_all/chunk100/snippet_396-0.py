# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(114276)

except ImportError:
    pass
_c_(114278, _n_(114277, "print", lambda: print), 'Original DataFrame:')
_l_(114279)
_c_(114282, _n_(114280, "print", lambda: print), _n_(114281, "df", lambda: df))
_l_(114283)
_c_(114285, _n_(114284, "print", lambda: print), '\nIs proper case or title case?')
_l_(114286)
_n_(114287, "df", lambda: df)['company_code_is_title'] = _c_(114295, _n_(114288, "list", lambda: list), _c_(114294, _n_(114289, "map", lambda: map), lambda x: _c_(114292, _a_(114291, _n_(114290, "x", lambda: x), "istitle")), _n_(114293, "df", lambda: df)['company_code']))
_l_(114296)
_c_(114299, _n_(114297, "print", lambda: print), _n_(114298, "df", lambda: df))
_l_(114300)