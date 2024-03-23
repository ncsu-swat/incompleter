# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(11529)

except ImportError:
    pass
_c_(11532, _a_(11531, _n_(11530, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(11533)
_c_(11536, _a_(11535, _n_(11534, "pd", lambda: pd), "set_option"), 'display.max_columns', None)
_l_(11537)
_c_(11539, _n_(11538, "print", lambda: print), 'Original DataFrame:')
_l_(11540)
_c_(11543, _n_(11541, "print", lambda: print), _n_(11542, "df", lambda: df))
_l_(11544)
dict_data_list = _c_(11546, _n_(11545, "list", lambda: list))
_l_(11547)
for (gg, dd) in _c_(11550, _a_(11549, _n_(11548, "df", lambda: df), "groupby"), ['school_code', 'class']):
    _l_(11583)

    group = _c_(11555, _n_(11551, "dict", lambda: dict), _c_(11554, _n_(11552, "zip", lambda: zip), ['school_code', 'class'], _n_(11553, "gg", lambda: gg)))
    _l_(11556)
    ocolumns_list = _c_(11558, _n_(11557, "list", lambda: list))
    _l_(11559)
    for (_, data) in _c_(11562, _a_(11561, _n_(11560, "dd", lambda: dd), "iterrows")):
        _l_(11574)

        data = _c_(11565, _a_(11564, _n_(11563, "data", lambda: data), "drop"), labels=['school_code', 'class'])
        _l_(11566)
        _c_(11572, _a_(11568, _n_(11567, "ocolumns_list", lambda: ocolumns_list), "append"), _c_(11571, _a_(11570, _n_(11569, "data", lambda: data), "to_dict")))
        _l_(11573)
    _n_(11575, "group", lambda: group)['other_columns'] = _n_(11576, "ocolumns_list", lambda: ocolumns_list)
    _l_(11577)
    _c_(11581, _a_(11579, _n_(11578, "dict_data_list", lambda: dict_data_list), "append"), _n_(11580, "group", lambda: group))
    _l_(11582)
_c_(11586, _n_(11584, "print", lambda: print), _n_(11585, "dict_data_list", lambda: dict_data_list))
_l_(11587)