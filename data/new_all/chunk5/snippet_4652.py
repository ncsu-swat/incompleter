# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53383631/nameerror-for-variable-that-i-wont-have-value-for-until-runtime
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def get_desc_info():
    _l_(693215)

    row_num = _c_(693209, _n_(693208, "get_row_num", lambda: get_row_num))
    _l_(693210)
    aux = f"Row Num: {_n_(693211, 'row_num', lambda: row_num)} - Wait Time: {_n_(693212, 'wait_time', lambda: wait_time)} - Total Inserts: {_n_(693213, 'num_inserts', lambda: num_inserts)}"
    _l_(693214)
    return aux

test_value: f"{_c_(693218, _a_(693217, _n_(693216, 'utils', lambda: utils), 'get_desc_info'))}"
_l_(693219)