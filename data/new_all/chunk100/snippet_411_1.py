# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(40204)

except ImportError:
    pass
try:
    import numpy as np
    _l_(40206)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(40207)
sales_tuples = _c_(40212, _n_(40208, "list", lambda: list), _c_(40211, _n_(40209, "zip", lambda: zip), *_n_(40210, "sales_arrays", lambda: sales_arrays)))
_l_(40213)
sales_index = _c_(40218, _a_(40216, _a_(40215, _n_(40214, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(40217, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(40219)
_c_(40222, _n_(40220, "print", lambda: print), _n_(40221, "sales_tuples", lambda: sales_tuples))
_l_(40223)
_c_(40225, _n_(40224, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(40226)
_c_(40229, _n_(40227, "print", lambda: print), _n_(40228, "df", lambda: df))
_l_(40230)
_c_(40232, _n_(40231, "print", lambda: print), '\nExtract a single row from the said dataframe:')
_l_(40233)
_c_(40237, _n_(40234, "print", lambda: print), _a_(40236, _n_(40235, "df", lambda: df), "loc")['sale2', 'city2'])
_l_(40238)
_c_(40240, _n_(40239, "print", lambda: print), '\nExtract a single row from the said dataframe:')
_l_(40241)
_c_(40245, _n_(40242, "print", lambda: print), _a_(40244, _n_(40243, "df", lambda: df), "loc")['sale2', 'city2'])
_l_(40246)
_c_(40248, _n_(40247, "print", lambda: print), '\nExtract number of rows from the said dataframe:')
_l_(40249)
_c_(40253, _n_(40250, "print", lambda: print), _a_(40252, _n_(40251, "df", lambda: df), "loc")['sale1'])
_l_(40254)
_c_(40256, _n_(40255, "print", lambda: print), '\nExtract number of rows from the said dataframe:')
_l_(40257)
_c_(40261, _n_(40258, "print", lambda: print), _a_(40260, _n_(40259, "df", lambda: df), "loc")['sale3'])
_l_(40262)
_c_(40264, _n_(40263, "print", lambda: print), '\nExtract a single value from the said dataframe:')
_l_(40265)
_c_(40269, _n_(40266, "print", lambda: print), _a_(40268, _n_(40267, "df", lambda: df), "loc")[('sale1', 'city2'), 1])
_l_(40270)
_c_(40272, _n_(40271, "print", lambda: print), '\nExtract a single value from the said dataframe:')
_l_(40273)
_c_(40277, _n_(40274, "print", lambda: print), _a_(40276, _n_(40275, "df", lambda: df), "loc")[('sale4', 'city1'), 4])
_l_(40278)