# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(117592)

except ImportError:
    pass
_c_(117594, _n_(117593, "print", lambda: print), 'Original DataFrame:')
_l_(117595)
_c_(117598, _n_(117596, "print", lambda: print), _n_(117597, "df", lambda: df))
_l_(117599)
_c_(117601, _n_(117600, "print", lambda: print), "\nMultiIndex using columns 't_id', ‘school_code’ and 'class':")
_l_(117602)
df1 = _c_(117605, _a_(117604, _n_(117603, "df", lambda: df), "set_index"), ['t_id', 'school_code', 'class'])
_l_(117606)
_c_(117609, _n_(117607, "print", lambda: print), _n_(117608, "df1", lambda: df1))
_l_(117610)
_c_(117612, _n_(117611, "print", lambda: print), '\nConvert 1st and 3rd levels in the index frame into columns:')
_l_(117613)
df2 = _c_(117616, _a_(117615, _n_(117614, "df1", lambda: df1), "reset_index"), level=['t_id', 'class'])
_l_(117617)
_c_(117620, _n_(117618, "print", lambda: print), _n_(117619, "df2", lambda: df2))
_l_(117621)