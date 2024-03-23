# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(40125)

except ImportError:
    pass
try:
    import numpy as np
    _l_(40127)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(40128)
sales_index = _c_(40133, _a_(40131, _a_(40130, _n_(40129, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(40132, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(40134)
_c_(40137, _n_(40135, "print", lambda: print), _n_(40136, "sales_tuples", lambda: sales_tuples))
_l_(40138)
_c_(40140, _n_(40139, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(40141)
df = _c_(40149, _a_(40143, _n_(40142, "pd", lambda: pd), "DataFrame"), _c_(40147, _a_(40146, _a_(40145, _n_(40144, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(40148, "sales_index", lambda: sales_index))
_l_(40150)
_c_(40153, _n_(40151, "print", lambda: print), _n_(40152, "df", lambda: df))
_l_(40154)
_c_(40156, _n_(40155, "print", lambda: print), '\nExtract a single row from the said dataframe:')
_l_(40157)
_c_(40161, _n_(40158, "print", lambda: print), _a_(40160, _n_(40159, "df", lambda: df), "loc")['sale2', 'city2'])
_l_(40162)
_c_(40164, _n_(40163, "print", lambda: print), '\nExtract a single row from the said dataframe:')
_l_(40165)
_c_(40169, _n_(40166, "print", lambda: print), _a_(40168, _n_(40167, "df", lambda: df), "loc")['sale2', 'city2'])
_l_(40170)
_c_(40172, _n_(40171, "print", lambda: print), '\nExtract number of rows from the said dataframe:')
_l_(40173)
_c_(40177, _n_(40174, "print", lambda: print), _a_(40176, _n_(40175, "df", lambda: df), "loc")['sale1'])
_l_(40178)
_c_(40180, _n_(40179, "print", lambda: print), '\nExtract number of rows from the said dataframe:')
_l_(40181)
_c_(40185, _n_(40182, "print", lambda: print), _a_(40184, _n_(40183, "df", lambda: df), "loc")['sale3'])
_l_(40186)
_c_(40188, _n_(40187, "print", lambda: print), '\nExtract a single value from the said dataframe:')
_l_(40189)
_c_(40193, _n_(40190, "print", lambda: print), _a_(40192, _n_(40191, "df", lambda: df), "loc")[('sale1', 'city2'), 1])
_l_(40194)
_c_(40196, _n_(40195, "print", lambda: print), '\nExtract a single value from the said dataframe:')
_l_(40197)
_c_(40201, _n_(40198, "print", lambda: print), _a_(40200, _n_(40199, "df", lambda: df), "loc")[('sale4', 'city1'), 4])
_l_(40202)