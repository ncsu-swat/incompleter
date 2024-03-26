# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(103027)

except ImportError:
    pass
_c_(103030, _a_(103029, _n_(103028, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(103031)
_c_(103034, _a_(103033, _n_(103032, "pd", lambda: pd), "set_option"), 'display.max_columns', None)
_l_(103035)
df = _c_(103038, _a_(103037, _n_(103036, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_Of_Birth ': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'age': [12, 12, 13, 13, 14, 12], 'height': [173, 192, 186, 167, 151, 159], 'weight': [35, 32, 33, 30, 31, 32], 'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
_l_(103039)
_c_(103041, _n_(103040, "print", lambda: print), 'Original DataFrame:')
_l_(103042)
_c_(103045, _n_(103043, "print", lambda: print), _n_(103044, "df", lambda: df))
_l_(103046)
for gg, dd in _c_(103049, _a_(103048, _n_(103047, "df", lambda: df), "groupby"), ['school_code', 'class']):
    _l_(103082)

    group = _c_(103054, _n_(103050, "dict", lambda: dict), _c_(103053, _n_(103051, "zip", lambda: zip), ['school_code', 'class'], _n_(103052, "gg", lambda: gg)))
    _l_(103055)
    ocolumns_list = _c_(103057, _n_(103056, "list", lambda: list))
    _l_(103058)
    for _, data in _c_(103061, _a_(103060, _n_(103059, "dd", lambda: dd), "iterrows")):
        _l_(103073)

        data = _c_(103064, _a_(103063, _n_(103062, "data", lambda: data), "drop"), labels=['school_code', 'class'])
        _l_(103065)
        _c_(103071, _a_(103067, _n_(103066, "ocolumns_list", lambda: ocolumns_list), "append"), _c_(103070, _a_(103069, _n_(103068, "data", lambda: data), "to_dict")))
        _l_(103072)
    _n_(103074, "group", lambda: group)['other_columns'] = _n_(103075, "ocolumns_list", lambda: ocolumns_list)
    _l_(103076)
    _c_(103080, _a_(103078, _n_(103077, "dict_data_list", lambda: dict_data_list), "append"), _n_(103079, "group", lambda: group))
    _l_(103081)
_c_(103085, _n_(103083, "print", lambda: print), _n_(103084, "dict_data_list", lambda: dict_data_list))
_l_(103086)