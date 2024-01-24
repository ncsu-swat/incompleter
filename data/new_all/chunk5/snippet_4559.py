# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55551721/getting-typeerror-of-tuple-even-though-the-object-is-of-type-numpy-nparray
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
labels=_c_(656139, _a_(656136, _n_(656135, "np", lambda: np), "ones"), _n_(656137, "length", lambda: length),dtype=_n_(656138, "int", lambda: int))
_l_(656140)
_c_(656145, _n_(656141, "print", lambda: print), _c_(656144, _n_(656142, "type", lambda: type), _n_(656143, "labels", lambda: labels)))
_l_(656146)
_n_(656147, "labels", lambda: labels)[:43]=0
_l_(656148)
_n_(656149, "labels", lambda: labels)[43:263]=1
_l_(656150)
_n_(656151, "labels", lambda: labels)[263:]=2
_l_(656152)
_c_(656157, _n_(656153, "print", lambda: print), _c_(656156, _a_(656155, _n_(656154, "labels", lambda: labels), "shape")))#produces error
_l_(656158)#produces error