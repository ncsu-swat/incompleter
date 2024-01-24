# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64486390/nameerror-when-trying-to-import-variables-from-another-python-file
# myfile1.py

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x = 5
_l_(572191)
y = 2
_l_(572192)
try:
    from myfile1 import *
    _l_(572194)

except ImportError:
    pass

_c_(572198, _n_(572195, "print", lambda: print), _a_(572197, _n_(572196, "myfile1", lambda: myfile1), "x"))
_l_(572199)
_c_(572203, _n_(572200, "print", lambda: print), _a_(572202, _n_(572201, "myfile1", lambda: myfile1), "y"))
_l_(572204)