# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69770023/python-colour-attributeerror-module-colour-has-no-attribute-ccs-illuminants
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
rgb = _c_(437203, _a_(437202, _n_(437201, "np", lambda: np), "array"), [100, 80, 20]) / 255
_l_(437204)
xyz = _c_(437208, _a_(437206, _n_(437205, "colour", lambda: colour), "sRGB_to_XYZ"), _n_(437207, "rgb", lambda: rgb))
_l_(437209)
lab = _c_(437213, _a_(437211, _n_(437210, "colour", lambda: colour), "XYZ_to_Lab"), _n_(437212, "xyz", lambda: xyz))
_l_(437214)
_c_(437217, _n_(437215, "print", lambda: print), _n_(437216, "lab", lambda: lab)) # 35, 4, 36
_l_(437218) # 35, 4, 36