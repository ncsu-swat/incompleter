# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55551721/getting-typeerror-of-tuple-even-though-the-object-is-of-type-numpy-nparray
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
labels=_c_(668928, _a_(668925, _n_(668924, "np", lambda: np), "ones"), _n_(668926, "length", lambda: length),dtype=_n_(668927, "int", lambda: int))
_l_(668929)
_c_(668934, _n_(668930, "print", lambda: print), _c_(668933, _n_(668931, "type", lambda: type), _n_(668932, "labels", lambda: labels)))
_l_(668935)
_n_(668936, "labels", lambda: labels)[:43]=0
_l_(668937)
_n_(668938, "labels", lambda: labels)[43:263]=1
_l_(668939)
_n_(668940, "labels", lambda: labels)[263:]=2
_l_(668941)
_c_(668946, _n_(668942, "print", lambda: print), _c_(668945, _a_(668944, _n_(668943, "labels", lambda: labels), "shape")))#produces error
_l_(668947)#produces error