# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50716931/unittest-mock-and-multiple-inheritance-typeerror-metaclass-conflict
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from class_a import A
    _l_(400686)

except ImportError:
    pass

class B:
    _l_(400688)

    pass
    _l_(400687)

class C(_n_(400689, "A", lambda: A), _n_(400690, "B", lambda: B)):
    _l_(400692)

    pass
    _l_(400691)