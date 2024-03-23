# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(68247)

except ImportError:
    pass
_c_(68250, _a_(68249, _n_(68248, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(68251)
_c_(68253, _n_(68252, "print", lambda: print), 'Original DataFrame:')
_l_(68254)
_c_(68257, _n_(68255, "print", lambda: print), _n_(68256, "student_data", lambda: student_data))
_l_(68258)
_c_(68260, _n_(68259, "print", lambda: print), '\nSplit the said data on school_code wise:')
_l_(68261)
grouped_single = _c_(68264, _a_(68263, _n_(68262, "student_data", lambda: student_data), "groupby"), ['school_code'])
_l_(68265)
_c_(68267, _n_(68266, "print", lambda: print), 'Size of the grouped data - single column')
_l_(68268)
_c_(68273, _n_(68269, "print", lambda: print), _c_(68272, _a_(68271, _n_(68270, "grouped_single", lambda: grouped_single), "size")))
_l_(68274)
_c_(68276, _n_(68275, "print", lambda: print), '\nSplit the said data on school_code and class wise:')
_l_(68277)
grouped_mul = _c_(68280, _a_(68279, _n_(68278, "student_data", lambda: student_data), "groupby"), ['school_code', 'class'])
_l_(68281)
_c_(68283, _n_(68282, "print", lambda: print), 'Size of the grouped data - multiple columns:')
_l_(68284)
_c_(68289, _n_(68285, "print", lambda: print), _c_(68288, _a_(68287, _n_(68286, "grouped_mul", lambda: grouped_mul), "size")))
_l_(68290)