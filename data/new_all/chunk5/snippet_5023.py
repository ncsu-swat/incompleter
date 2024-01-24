# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57345721/how-to-fix-attributeerror-on-using-pyinstaller-on-a-project-with-tensorflow-an
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tensorflow import keras
    _l_(692157)

except ImportError:
    pass
_c_(692161, _n_(692158, "print", lambda: print), _a_(692160, _n_(692159, "keras", lambda: keras), "__file__"))
_l_(692162)