# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71422564/3d-volume-slicing-typeerror-only-integer-scalar-arrays-can-be-converted-to-a-s
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
ini=_n_(390166, "p", lambda: p)[0,0]
_l_(390167)
fin=_n_(390168, "p", lambda: p)[0,:-1]
_l_(390169)
aux=_n_(390170, "img", lambda: img)[:,:,_c_(390174, _a_(390172, _n_(390171, "ini", lambda: ini), "astype"), _n_(390173, "int", lambda: int)):_c_(390178, _a_(390176, _n_(390175, "fin", lambda: fin), "astype"), _n_(390177, "int", lambda: int))]
_l_(390179)