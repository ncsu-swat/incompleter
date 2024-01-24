# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52242859/file-e-python-lib-re-py-line-229-in-finditer-return-compilepattern-flags
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from skimage.feature import greycomatrix
    _l_(441541)

except ImportError:
    pass
try:
    import numpy as np
    _l_(441543)

except ImportError:
    pass

image=_c_(441548, _a_(441545, _n_(441544, "np", lambda: np), "array"), [[1,1,5,6,8],
                [0,0,5,7,1],
                [4,0,0,1,2],
                [8,5,1,2,5]],dtype=_a_(441547, _n_(441546, "np", lambda: np), "uint8"))
_l_(441549)
#levels=256   image   this test is 9
result=_c_(441558, _n_(441550, "greycomatrix", lambda: greycomatrix), _n_(441551, "image", lambda: image),[1],[0,_a_(441553, _n_(441552, "np", lambda: np), "pi")/4,_a_(441555, _n_(441554, "np", lambda: np), "pi")/2,3*_a_(441557, _n_(441556, "np", lambda: np), "pi")/4],levels=9)
_l_(441559)
_c_(441562, _n_(441560, "print", lambda: print), _n_(441561, "result", lambda: result)[:, :, 0, 0])
_l_(441563)