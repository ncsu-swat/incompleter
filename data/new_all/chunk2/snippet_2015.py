# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69770023/python-colour-attributeerror-module-colour-has-no-attribute-ccs-illuminants
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
rgb = _c_(425573, _a_(425572, _n_(425571, "np", lambda: np), "array"), [100, 80, 20]) / 255
_l_(425574)
D50 = _a_(425576, _n_(425575, "colour", lambda: colour), "CCS_ILLUMINANTS")['CIE 1931 2 Degree Standard Observer']['D50']
_l_(425577)
xyz = _c_(425582, _a_(425579, _n_(425578, "colour", lambda: colour), "sRGB_to_XYZ"), _n_(425580, "rgb", lambda: rgb), illuminant=_n_(425581, "D50", lambda: D50))
_l_(425583)
_c_(425590, _n_(425584, "print", lambda: print), _c_(425589, _a_(425586, _n_(425585, "colour", lambda: colour), "XYZ_to_Lab"), _n_(425587, "xyz", lambda: xyz), illuminant=_n_(425588, "D50", lambda: D50)))
_l_(425591)