# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/209513/convert-hex-string-to-integer-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
a = _c_(1540082, _n_(1540081, "int", lambda: int), '0x100', 16)
_l_(1540083)
_c_(1540086, _n_(1540084, "print", lambda: print), _n_(1540085, "a", lambda: a))   #256
_l_(1540087)   #256
_c_(1540090, _n_(1540088, "print", lambda: print), '%x' % _n_(1540089, "a", lambda: a)) #100
_l_(1540091) #100
b = _n_(1540092, "a", lambda: a)
_l_(1540093)
_c_(1540096, _n_(1540094, "print", lambda: print), _n_(1540095, "b", lambda: b)) #256
_l_(1540097) #256
c = '%x' % _n_(1540098, "a", lambda: a)
_l_(1540099)
_c_(1540102, _n_(1540100, "print", lambda: print), _n_(1540101, "c", lambda: c)) #100
_l_(1540103) #100

