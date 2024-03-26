# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(115177)

except ImportError:
    pass
try:
    import numpy as np
    _l_(115179)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(115180)
sales_tuples = _c_(115185, _n_(115181, "list", lambda: list), _c_(115184, _n_(115182, "zip", lambda: zip), *_n_(115183, "sales_arrays", lambda: sales_arrays)))
_l_(115186)
_c_(115189, _n_(115187, "print", lambda: print), _n_(115188, "sales_tuples", lambda: sales_tuples))
_l_(115190)
_c_(115192, _n_(115191, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(115193)
df = _c_(115201, _a_(115195, _n_(115194, "pd", lambda: pd), "DataFrame"), _c_(115199, _a_(115198, _a_(115197, _n_(115196, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(115200, "sales_index", lambda: sales_index))
_l_(115202)
_c_(115205, _n_(115203, "print", lambda: print), _n_(115204, "df", lambda: df))
_l_(115206)
_c_(115208, _n_(115207, "print", lambda: print), '\nExtract a single row from the said dataframe:')
_l_(115209)
_c_(115213, _n_(115210, "print", lambda: print), _a_(115212, _n_(115211, "df", lambda: df), "loc")['sale2', 'city2'])
_l_(115214)
_c_(115216, _n_(115215, "print", lambda: print), '\nExtract a single row from the said dataframe:')
_l_(115217)
_c_(115221, _n_(115218, "print", lambda: print), _a_(115220, _n_(115219, "df", lambda: df), "loc")['sale2', 'city2'])
_l_(115222)
_c_(115224, _n_(115223, "print", lambda: print), '\nExtract number of rows from the said dataframe:')
_l_(115225)
_c_(115229, _n_(115226, "print", lambda: print), _a_(115228, _n_(115227, "df", lambda: df), "loc")['sale1'])
_l_(115230)
_c_(115232, _n_(115231, "print", lambda: print), '\nExtract number of rows from the said dataframe:')
_l_(115233)
_c_(115237, _n_(115234, "print", lambda: print), _a_(115236, _n_(115235, "df", lambda: df), "loc")['sale3'])
_l_(115238)
_c_(115240, _n_(115239, "print", lambda: print), '\nExtract a single value from the said dataframe:')
_l_(115241)
_c_(115245, _n_(115242, "print", lambda: print), _a_(115244, _n_(115243, "df", lambda: df), "loc")[('sale1', 'city2'), 1])
_l_(115246)
_c_(115248, _n_(115247, "print", lambda: print), '\nExtract a single value from the said dataframe:')
_l_(115249)
_c_(115253, _n_(115250, "print", lambda: print), _a_(115252, _n_(115251, "df", lambda: df), "loc")[('sale4', 'city1'), 4])
_l_(115254)