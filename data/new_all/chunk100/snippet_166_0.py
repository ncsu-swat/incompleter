# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(11410)

except ImportError:
    pass
_c_(11413, _a_(11412, _n_(11411, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(11414)
_c_(11417, _a_(11416, _n_(11415, "pd", lambda: pd), "set_option"), 'display.max_columns', None)
_l_(11418)
df = _c_(11421, _a_(11420, _n_(11419, "pd", lambda: pd), "DataFrame"), {'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'date_Of_Birth ': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'], 'age': [12, 12, 13, 13, 14, 12], 'height': [173, 192, 186, 167, 151, 159], 'weight': [35, 32, 33, 30, 31, 32], 'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
_l_(11422)
_c_(11424, _n_(11423, "print", lambda: print), 'Original DataFrame:')
_l_(11425)
_c_(11428, _n_(11426, "print", lambda: print), _n_(11427, "df", lambda: df))
_l_(11429)
dict_data_list = _c_(11431, _n_(11430, "list", lambda: list))
_l_(11432)
for (gg, dd) in _c_(11435, _a_(11434, _n_(11433, "df", lambda: df), "groupby"), ['school_code', 'class']):
    _l_(11462)

    ocolumns_list = _c_(11437, _n_(11436, "list", lambda: list))
    _l_(11438)
    for (_, data) in _c_(11441, _a_(11440, _n_(11439, "dd", lambda: dd), "iterrows")):
        _l_(11453)

        data = _c_(11444, _a_(11443, _n_(11442, "data", lambda: data), "drop"), labels=['school_code', 'class'])
        _l_(11445)
        _c_(11451, _a_(11447, _n_(11446, "ocolumns_list", lambda: ocolumns_list), "append"), _c_(11450, _a_(11449, _n_(11448, "data", lambda: data), "to_dict")))
        _l_(11452)
    _n_(11454, "group", lambda: group)['other_columns'] = _n_(11455, "ocolumns_list", lambda: ocolumns_list)
    _l_(11456)
    _c_(11460, _a_(11458, _n_(11457, "dict_data_list", lambda: dict_data_list), "append"), _n_(11459, "group", lambda: group))
    _l_(11461)
_c_(11465, _n_(11463, "print", lambda: print), _n_(11464, "dict_data_list", lambda: dict_data_list))
_l_(11466)