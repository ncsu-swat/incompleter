# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/33533148/how-do-i-type-hint-a-method-with-the-type-of-the-enclosing-class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class MyClass:
    _l_(1540851)

    @_n_(1540846, "classmethod", lambda: classmethod)
    def make_new(cls) -> __qualname__:
        _l_(1540850)

        aux = _c_(1540848, _n_(1540847, "cls", lambda: cls))
        _l_(1540849)
        return aux

