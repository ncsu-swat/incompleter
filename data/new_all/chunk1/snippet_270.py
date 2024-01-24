# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52140811/overwriting-class-raises-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Derived(_n_(381151, "Base", lambda: Base)):
    _l_(381157)

    @_n_(381152, "classmethod", lambda: classmethod)
    def cast(cls, obj: Base):
        _l_(381156)

        _n_(381153, "obj", lambda: obj).__class__ = _n_(381154, "cls", lambda: cls)
        _l_(381155)