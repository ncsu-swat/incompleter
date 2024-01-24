# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53327338/numpy-busday-count-for-days-difference-gives-typeerror-dtypem8us-to-dtyp
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(522735)

except ImportError:
    pass
try:
    import numpy as np
    _l_(522737)

except ImportError:
    pass
try:
    import datetime
    _l_(522739)

except ImportError:
    pass
try:
    from datetime import date
    _l_(522741)

except ImportError:
    pass
try:
    from datetime import datetime, timedelta
    _l_(522743)

except ImportError:
    pass
try:
    from dateutil.relativedelta import relativedelta
    _l_(522745)

except ImportError:
    pass
try:
    import xlrd
    _l_(522747)

except ImportError:
    pass
try:
    import workdays
    _l_(522749)

except ImportError:
    pass
try:
    import defusedxml
    _l_(522751)

except ImportError:
    pass
try:
    from xlrd import open_workbook
    _l_(522753)

except ImportError:
    pass
_c_(522756, _a_(522755, _n_(522754, "defusedxml", lambda: defusedxml), "defuse_stdlib"))
_l_(522757)


def secure_open_workbook(**kwargs):
    _l_(522768)

    try:
        _l_(522767)

        aux = _c_(522760, _n_(522758, "open_workbook", lambda: open_workbook), **_n_(522759, "kwargs", lambda: kwargs))
        _l_(522761)
        return aux
    except _n_(522762, "EntitiesForbidden", lambda: EntitiesForbidden):
        _l_(522766)

        raise _c_(522764, _n_(522763, "ValueError", lambda: ValueError), 'Please use a xlsx file without XEE')
        _l_(522765)


#loading Raw Data
releases = _c_(522771, _a_(522770, _n_(522769, "pd", lambda: pd), "read_excel"), r'C:\Desktop\Releases.xlsx',
                     sheet_name = 'Releases',
                     header = 0
                     )
_l_(522772)
_a_(522774, _n_(522773, "releases", lambda: releases), "loc")[_c_(522777, _a_(522776, _n_(522775, "releases", lambda: releases)['REASSIGN_DATE'], "isnull")),'REASSIGN_DATE']=_n_(522778, "releases", lambda: releases)['SETUP_DATE']
_l_(522779)
_n_(522780, "releases", lambda: releases)['REASSIGN_DATE']=_c_(522784, _a_(522782, _n_(522781, "pd", lambda: pd), "to_datetime"), _n_(522783, "releases", lambda: releases)['REASSIGN_DATE'])
_l_(522785)
_n_(522786, "releases", lambda: releases)['RELEASED_DATE']=_c_(522790, _a_(522788, _n_(522787, "pd", lambda: pd), "to_datetime"), _n_(522789, "releases", lambda: releases)['RELEASED_DATE'])
_l_(522791)
_n_(522792, "releases", lambda: releases)['RELEASED_DAYS']=_c_(522802, _a_(522794, _n_(522793, "releases", lambda: releases), "apply"), lambda x: 
_c_(522801, _a_(522796, _n_(522795, "np", lambda: np), "busday_count"), _a_(522798, _n_(522797, "x", lambda: x), "REASSIGN_DATE"),_a_(522800, _n_(522799, "x", lambda: x), "RELEASED_DATE")),axis =1)
_l_(522803)

releases_2=_c_(522806, _a_(522805, _n_(522804, "releases", lambda: releases), "drop"), ['SETUPDATE','RELEASEDDATE','REASSIGNDATE'],axis=1)
_l_(522807)