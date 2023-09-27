# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(1540528, _a_(1540527, _c_(1540526, _a_(1540525, "+7", "lstrip"), "-+"), "isdigit"))
_l_(1540529)
True
_l_(1540530)
_c_(1540534, _a_(1540533, _c_(1540532, _a_(1540531, "-7", "lstrip"), "-+"), "isdigit"))
_l_(1540535)
True
_l_(1540536)
_c_(1540540, _a_(1540539, _c_(1540538, _a_(1540537, "7", "lstrip"), "-+"), "isdigit"))
_l_(1540541)
True
_l_(1540542)
_c_(1540546, _a_(1540545, _c_(1540544, _a_(1540543, "13.4", "lstrip"), "-+"), "isdigit"))
_l_(1540547)
False
_l_(1540548)

def is_int(val):
   _l_(1540555)

   aux = _c_(1540553, _a_(1540552, _c_(1540551, _a_(1540550, _n_(1540549, "val", lambda: val), "lstrip"), "-+"), "isdigit"))
   _l_(1540554)
   return aux

