# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62034809/python3-7-metaclassing-from-tuple-base-class-receiving-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from typing import Tuple
    _l_(565949)

except ImportError:
    pass

class StructMeta(_n_(565950, "Tuple", lambda: Tuple)):
    _l_(565952)

    pass
    _l_(565951)

class Struct(metaclass=_n_(565953, "StructMeta", lambda: StructMeta)):
    _l_(565955)

    pass
    _l_(565954)

_c_(565960, _n_(565956, "print", lambda: print), _c_(565959, _n_(565957, "type", lambda: type), _n_(565958, "Struct", lambda: Struct)))
_l_(565961)