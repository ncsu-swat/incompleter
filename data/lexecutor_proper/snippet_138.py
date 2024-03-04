# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/192109/is-there-a-built-in-function-to-print-all-the-current-properties-and-values-of-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pprint import pprint
    _l_(61798)

except ImportError:
    pass
_c_(61803, _n_(61799, "pprint", lambda: pprint), _c_(61802, _n_(61800, "vars", lambda: vars), _n_(61801, "your_object", lambda: your_object)))
_l_(61804)

