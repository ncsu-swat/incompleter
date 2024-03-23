# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(96229)

except ImportError:
    pass
sr_data = _c_(96232, _a_(96231, _n_(96230, "pd", lambda: pd), "Series"), [68, 75, 86, 80, None])
_l_(96233)
_c_(96235, _n_(96234, "print", lambda: print), 'Original DataFrame:')
_l_(96236)
_c_(96239, _n_(96237, "print", lambda: print), _n_(96238, "df_data", lambda: df_data))
_l_(96240)
_c_(96242, _n_(96241, "print", lambda: print), '\nOriginal Series:')
_l_(96243)
_c_(96246, _n_(96244, "print", lambda: print), _n_(96245, "sr_data", lambda: sr_data))
_l_(96247)
_c_(96249, _n_(96248, "print", lambda: print), '\nCheck for inequality of the said series & dataframe:')
_l_(96250)
_c_(96256, _n_(96251, "print", lambda: print), _c_(96255, _a_(96253, _n_(96252, "df_data", lambda: df_data), "ne"), _n_(96254, "sr_data", lambda: sr_data), axis=0))
_l_(96257)