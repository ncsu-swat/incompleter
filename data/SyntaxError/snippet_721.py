# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/13646245/is-it-possible-to-make-abstract-classes
# decorators.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def abstract(f):
    _l_(1544523)

    def _decorator(*_):
        _l_(1544520)

        raise _c_(1544518, _n_(1544515, "NotImplementedError", lambda: NotImplementedError), f"Method '{_a_(1544517, _n_(1544516, 'f', lambda: f), '__name__')}' is abstract")
        _l_(1544519)
    aux = _n_(1544521, "_decorator", lambda: _decorator)
    _l_(1544522)
    return aux


# yourclass.py
class Vehicle:
    _l_(1544532)

    def add_energy():
        _l_(1544527)

        _c_(1544525, _n_(1544524, "print", lambda: print), "Energy added!")
        _l_(1544526)

    @_n_(1544528, "abstract", lambda: abstract)
    def get_make():
        _l_(1544529)

...
    @_n_(1544530, "abstract", lambda: abstract)
    def get_model():
        _l_(1544531)

...
