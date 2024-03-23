# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(11589)

except ImportError:
    pass
_c_(11592, _a_(11591, _n_(11590, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(11593)
_c_(11596, _a_(11595, _n_(11594, "pd", lambda: pd), "set_option"), 'display.max_columns', None)
_l_(11597)
df = _c_(11600, _a_(11599, _n_(11598, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_Of_Birth ': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'age': [12, 12, 13, 13, 14, 12], 'height': [173, 192, 186, 167, 151, 159], 'weight': [35, 32, 33, 30, 31, 32], 'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
_l_(11601)
_c_(11603, _n_(11602, "print", lambda: print), 'Original DataFrame:')
_l_(11604)
_c_(11607, _n_(11605, "print", lambda: print), _n_(11606, "df", lambda: df))
_l_(11608)
for (gg, dd) in _c_(11611, _a_(11610, _n_(11609, "df", lambda: df), "groupby"), ['school_code', 'class']):
    _l_(11644)

    group = _c_(11616, _n_(11612, "dict", lambda: dict), _c_(11615, _n_(11613, "zip", lambda: zip), ['school_code', 'class'], _n_(11614, "gg", lambda: gg)))
    _l_(11617)
    ocolumns_list = _c_(11619, _n_(11618, "list", lambda: list))
    _l_(11620)
    for (_, data) in _c_(11623, _a_(11622, _n_(11621, "dd", lambda: dd), "iterrows")):
        _l_(11635)

        data = _c_(11626, _a_(11625, _n_(11624, "data", lambda: data), "drop"), labels=['school_code', 'class'])
        _l_(11627)
        _c_(11633, _a_(11629, _n_(11628, "ocolumns_list", lambda: ocolumns_list), "append"), _c_(11632, _a_(11631, _n_(11630, "data", lambda: data), "to_dict")))
        _l_(11634)
    _n_(11636, "group", lambda: group)['other_columns'] = _n_(11637, "ocolumns_list", lambda: ocolumns_list)
    _l_(11638)
    _c_(11642, _a_(11640, _n_(11639, "dict_data_list", lambda: dict_data_list), "append"), _n_(11641, "group", lambda: group))
    _l_(11643)
_c_(11647, _n_(11645, "print", lambda: print), _n_(11646, "dict_data_list", lambda: dict_data_list))
_l_(11648)