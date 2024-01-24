# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53748877/python-3-for-loop-typeerror-int-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(522405)

except ImportError:
    pass
try:
    import math
    _l_(522407)

except ImportError:
    pass
try:
    from PIL import Image
    _l_(522409)

except ImportError:
    pass
try:
    from PIL import ImageDraw
    _l_(522411)

except ImportError:
    pass

im = _c_(522416, _a_(522415, _c_(522414, _a_(522413, _n_(522412, "Image", lambda: Image), "open"), 'harita2.png'), "convert"), "RGB")
_l_(522417)
npimage = _c_(522421, _a_(522419, _n_(522418, "np", lambda: np), "array"), _n_(522420, "im", lambda: im))
_l_(522422)
g1= _c_(522427, _a_(522424, _n_(522423, "np", lambda: np), "array"), [93,95,95],dtype=_a_(522426, _n_(522425, "np", lambda: np), "uint8"))
_l_(522428)
g2= _c_(522433, _a_(522430, _n_(522429, "np", lambda: np), "array"), [54,55,55],dtype=_a_(522432, _n_(522431, "np", lambda: np), "uint8"))
_l_(522434)
g3= _c_(522439, _a_(522436, _n_(522435, "np", lambda: np), "array"), [84,86,86],dtype=_a_(522438, _n_(522437, "np", lambda: np), "uint8"))
_l_(522440)
s= _c_(522445, _a_(522442, _n_(522441, "np", lambda: np), "array"), [0,0,0],dtype=_a_(522444, _n_(522443, "np", lambda: np), "uint8"))
_l_(522446)
#print(g1)
x1,y1=_c_(522454, _a_(522448, _n_(522447, "np", lambda: np), "where"), _c_(522453, _a_(522450, _n_(522449, "np", lambda: np), "all"), (_n_(522451, "npimage", lambda: npimage)==_n_(522452, "g1", lambda: g1)),axis=-1))
_l_(522455)
_c_(522458, _n_(522456, "print", lambda: print), _n_(522457, "x1", lambda: x1))
_l_(522459)
tt = _a_(522461, _n_(522460, "x1", lambda: x1), "size")
_l_(522462)
tt = _c_(522465, _n_(522463, "int", lambda: int), _n_(522464, "tt", lambda: tt))
_l_(522466)
_c_(522469, _n_(522467, "print", lambda: print), _n_(522468, "tt", lambda: tt))
_l_(522470)
_c_(522473, _n_(522471, "print", lambda: print), _n_(522472, "x1", lambda: x1)[15])
_l_(522474)
_c_(522477, _n_(522475, "print", lambda: print), _n_(522476, "y1", lambda: y1)[15])   
_l_(522478)   

for vvv in _n_(522479, "tt", lambda: tt):
    _l_(522494)

    idraw = _c_(522483, _a_(522481, _n_(522480, "ImageDraw", lambda: ImageDraw), "Draw"), _n_(522482, "im", lambda: im))
    _l_(522484)
    _c_(522492, _a_(522486, _n_(522485, "idraw", lambda: idraw), "point"), (_n_(522487, "x1", lambda: x1)[_n_(522488, "vvv", lambda: vvv)],_n_(522489, "y1", lambda: y1)[_n_(522490, "vvv", lambda: vvv)]),_n_(522491, "s", lambda: s))
    _l_(522493)

_c_(522497, _a_(522496, _n_(522495, "im", lambda: im), "save"), 'boyatest.png')
_l_(522498)