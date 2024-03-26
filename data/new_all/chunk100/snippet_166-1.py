# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(103088)

except ImportError:
    pass
_c_(103091, _a_(103090, _n_(103089, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(103092)
_c_(103095, _a_(103094, _n_(103093, "pd", lambda: pd), "set_option"), 'display.max_columns', None)
_l_(103096)
_c_(103098, _n_(103097, "print", lambda: print), 'Original DataFrame:')
_l_(103099)
_c_(103102, _n_(103100, "print", lambda: print), _n_(103101, "df", lambda: df))
_l_(103103)
dict_data_list = _c_(103105, _n_(103104, "list", lambda: list))
_l_(103106)
for gg, dd in _c_(103109, _a_(103108, _n_(103107, "df", lambda: df), "groupby"), ['school_code', 'class']):
    _l_(103142)

    group = _c_(103114, _n_(103110, "dict", lambda: dict), _c_(103113, _n_(103111, "zip", lambda: zip), ['school_code', 'class'], _n_(103112, "gg", lambda: gg)))
    _l_(103115)
    ocolumns_list = _c_(103117, _n_(103116, "list", lambda: list))
    _l_(103118)
    for _, data in _c_(103121, _a_(103120, _n_(103119, "dd", lambda: dd), "iterrows")):
        _l_(103133)

        data = _c_(103124, _a_(103123, _n_(103122, "data", lambda: data), "drop"), labels=['school_code', 'class'])
        _l_(103125)
        _c_(103131, _a_(103127, _n_(103126, "ocolumns_list", lambda: ocolumns_list), "append"), _c_(103130, _a_(103129, _n_(103128, "data", lambda: data), "to_dict")))
        _l_(103132)
    _n_(103134, "group", lambda: group)['other_columns'] = _n_(103135, "ocolumns_list", lambda: ocolumns_list)
    _l_(103136)
    _c_(103140, _a_(103138, _n_(103137, "dict_data_list", lambda: dict_data_list), "append"), _n_(103139, "group", lambda: group))
    _l_(103141)
_c_(103145, _n_(103143, "print", lambda: print), _n_(103144, "dict_data_list", lambda: dict_data_list))
_l_(103146)