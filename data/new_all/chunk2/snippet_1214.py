# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/29618165/why-is-the-order-of-types-in-python-2-fixed-and-an-unorderable-typeerror-in-pyt
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(458329, "object", lambda: object) > _n_(458330, "type", lambda: type) > _n_(458331, "tuple", lambda: tuple) > (_n_(458332, "bytes", lambda: bytes) or _n_(458333, "str", lambda: str)) > _n_(458334, "frozenset", lambda: frozenset) > _n_(458335, "set", lambda: set) > _n_(458336, "dict", lambda: dict) \
       > _n_(458337, "long", lambda: long) > _n_(458338, "list", lambda: list) > _n_(458339, "int", lambda: int) > _n_(458340, "float", lambda: float) > _n_(458341, "complex", lambda: complex) > _n_(458342, "bytearray", lambda: bytearray) > None
_l_(458343)

True
_l_(458344)