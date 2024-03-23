# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(11650)

except ImportError:
    pass
_c_(11653, _a_(11652, _n_(11651, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(11654)
_c_(11657, _a_(11656, _n_(11655, "pd", lambda: pd), "set_option"), 'display.max_columns', None)
_l_(11658)
df = _c_(11661, _a_(11660, _n_(11659, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_Of_Birth ': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'age': [12, 12, 13, 13, 14, 12], 'height': [173, 192, 186, 167, 151, 159], 'weight': [35, 32, 33, 30, 31, 32], 'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
_l_(11662)
_c_(11664, _n_(11663, "print", lambda: print), 'Original DataFrame:')
_l_(11665)
_c_(11668, _n_(11666, "print", lambda: print), _n_(11667, "df", lambda: df))
_l_(11669)
dict_data_list = _c_(11671, _n_(11670, "list", lambda: list))
_l_(11672)
for (gg, dd) in _c_(11675, _a_(11674, _n_(11673, "df", lambda: df), "groupby"), ['school_code', 'class']):
    _l_(11704)

    group = _c_(11680, _n_(11676, "dict", lambda: dict), _c_(11679, _n_(11677, "zip", lambda: zip), ['school_code', 'class'], _n_(11678, "gg", lambda: gg)))
    _l_(11681)
    ocolumns_list = _c_(11683, _n_(11682, "list", lambda: list))
    _l_(11684)
    for (_, data) in _c_(11687, _a_(11686, _n_(11685, "dd", lambda: dd), "iterrows")):
        _l_(11695)

        _c_(11693, _a_(11689, _n_(11688, "ocolumns_list", lambda: ocolumns_list), "append"), _c_(11692, _a_(11691, _n_(11690, "data", lambda: data), "to_dict")))
        _l_(11694)
    _n_(11696, "group", lambda: group)['other_columns'] = _n_(11697, "ocolumns_list", lambda: ocolumns_list)
    _l_(11698)
    _c_(11702, _a_(11700, _n_(11699, "dict_data_list", lambda: dict_data_list), "append"), _n_(11701, "group", lambda: group))
    _l_(11703)
_c_(11707, _n_(11705, "print", lambda: print), _n_(11706, "dict_data_list", lambda: dict_data_list))
_l_(11708)