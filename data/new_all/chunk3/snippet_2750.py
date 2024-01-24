# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64486390/nameerror-when-trying-to-import-variables-from-another-python-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import myfile1
    _l_(548741)

except ImportError:
    pass
try:
    from myfile1 import x, y
    _l_(548743)

except ImportError:
    pass