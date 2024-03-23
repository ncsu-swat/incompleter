# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(85822)

except ImportError:
    pass
_c_(85825, _a_(85824, _n_(85823, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(85826)
_c_(85828, _n_(85827, "print", lambda: print), 'Original Orders DataFrame:')
_l_(85829)
_c_(85832, _n_(85830, "print", lambda: print), _n_(85831, "df", lambda: df))
_l_(85833)
_n_(85834, "df", lambda: df)['ord_date'] = _c_(85838, _a_(85836, _n_(85835, "pd", lambda: pd), "to_datetime"), _n_(85837, "df", lambda: df)['ord_date'])
_l_(85839)
_c_(85841, _n_(85840, "print", lambda: print), '\nMonth wise purchase amount:')
_l_(85842)
result = _c_(85853, _a_(85851, _c_(85850, _a_(85846, _c_(85845, _a_(85844, _n_(85843, "df", lambda: df), "set_index"), 'ord_date'), "groupby"), _c_(85849, _a_(85848, _n_(85847, "pd", lambda: pd), "Grouper"), freq='M')), "agg"), {'purch_amt': _n_(85852, "sum", lambda: sum)})
_l_(85854)
_c_(85857, _n_(85855, "print", lambda: print), _n_(85856, "result", lambda: result))
_l_(85858)