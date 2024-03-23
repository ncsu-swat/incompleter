# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(72243)

except ImportError:
    pass
try:
    import re as re
    _l_(72245)

except ImportError:
    pass
df = _c_(72248, _a_(72247, _n_(72246, "pd", lambda: pd), "DataFrame"), {'company_code': ['Abcd', 'EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'], 'date_of_sale': ['12/05/2002', '16/02/1999', '05/09/1998', '12/02/2022', '15/09/1997'], 'address': ['9910 Surrey <b>Avenue</b>', '92 N. Bishop Avenue', '9910 <br>Golden Star Avenue', '102 Dunbar <i></i>St.', '17 West Livingston Court']})
_l_(72249)
_c_(72251, _n_(72250, "print", lambda: print), 'Original DataFrame:')
_l_(72252)
_c_(72255, _n_(72253, "print", lambda: print), _n_(72254, "df", lambda: df))
_l_(72256)

def remove_tags(string):
    _l_(72259)

    aux = _n_(72257, "result", lambda: result)
    _l_(72258)
    return aux
_n_(72260, "df", lambda: df)['with_out_tags'] = _c_(72266, _a_(72262, _n_(72261, "df", lambda: df)['address'], "apply"), lambda cw: _c_(72265, _n_(72263, "remove_tags", lambda: remove_tags), _n_(72264, "cw", lambda: cw)))
_l_(72267)
_c_(72269, _n_(72268, "print", lambda: print), "\nSentences without tags':")
_l_(72270)
_c_(72273, _n_(72271, "print", lambda: print), _n_(72272, "df", lambda: df))
_l_(72274)