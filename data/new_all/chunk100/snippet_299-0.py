# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(109160)

except ImportError:
    pass
_c_(109163, _a_(109162, _n_(109161, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(109164)
_c_(109166, _n_(109165, "print", lambda: print), 'Original DataFrame:')
_l_(109167)
_c_(109170, _n_(109168, "print", lambda: print), _n_(109169, "student_data", lambda: student_data))
_l_(109171)
_c_(109173, _n_(109172, "print", lambda: print), '\nSplit the said data on school_code wise:')
_l_(109174)
grouped = _c_(109177, _a_(109176, _n_(109175, "student_data", lambda: student_data), "groupby"), ['school_code'])
_l_(109178)
_c_(109180, _n_(109179, "print", lambda: print), "Call school code 's001':")
_l_(109181)
_c_(109186, _n_(109182, "print", lambda: print), _c_(109185, _a_(109184, _n_(109183, "grouped", lambda: grouped), "get_group"), 's001'))
_l_(109187)
_c_(109189, _n_(109188, "print", lambda: print), "\nCall school code 's004':")
_l_(109190)
_c_(109195, _n_(109191, "print", lambda: print), _c_(109194, _a_(109193, _n_(109192, "grouped", lambda: grouped), "get_group"), 's004'))
_l_(109196)