# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(11468)

except ImportError:
    pass
_c_(11471, _a_(11470, _n_(11469, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(11472)
_c_(11475, _a_(11474, _n_(11473, "pd", lambda: pd), "set_option"), 'display.max_columns', None)
_l_(11476)
df = _c_(11479, _a_(11478, _n_(11477, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_Of_Birth ': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'age': [12, 12, 13, 13, 14, 12], 'height': [173, 192, 186, 167, 151, 159], 'weight': [35, 32, 33, 30, 31, 32], 'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
_l_(11480)
_c_(11482, _n_(11481, "print", lambda: print), 'Original DataFrame:')
_l_(11483)
_c_(11486, _n_(11484, "print", lambda: print), _n_(11485, "df", lambda: df))
_l_(11487)
dict_data_list = _c_(11489, _n_(11488, "list", lambda: list))
_l_(11490)
for (gg, dd) in _c_(11493, _a_(11492, _n_(11491, "df", lambda: df), "groupby"), ['school_code', 'class']):
    _l_(11523)

    group = _c_(11498, _n_(11494, "dict", lambda: dict), _c_(11497, _n_(11495, "zip", lambda: zip), ['school_code', 'class'], _n_(11496, "gg", lambda: gg)))
    _l_(11499)
    for (_, data) in _c_(11502, _a_(11501, _n_(11500, "dd", lambda: dd), "iterrows")):
        _l_(11514)

        data = _c_(11505, _a_(11504, _n_(11503, "data", lambda: data), "drop"), labels=['school_code', 'class'])
        _l_(11506)
        _c_(11512, _a_(11508, _n_(11507, "ocolumns_list", lambda: ocolumns_list), "append"), _c_(11511, _a_(11510, _n_(11509, "data", lambda: data), "to_dict")))
        _l_(11513)
    _n_(11515, "group", lambda: group)['other_columns'] = _n_(11516, "ocolumns_list", lambda: ocolumns_list)
    _l_(11517)
    _c_(11521, _a_(11519, _n_(11518, "dict_data_list", lambda: dict_data_list), "append"), _n_(11520, "group", lambda: group))
    _l_(11522)
_c_(11526, _n_(11524, "print", lambda: print), _n_(11525, "dict_data_list", lambda: dict_data_list))
_l_(11527)