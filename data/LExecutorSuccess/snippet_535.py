# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9475241/split-string-every-nth-character
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
s='1234567890'
_l_(1543263)
_c_(1543272, _n_(1543264, "print", lambda: print), [_n_(1543265, "s", lambda: s)[_n_(1543266, "idx", lambda: idx):_n_(1543267, "idx", lambda: idx)+2] for idx,val in _c_(1543270, _n_(1543268, "enumerate", lambda: enumerate), _n_(1543269, "s", lambda: s)) if _n_(1543271, "idx", lambda: idx)%2 == 0])
_l_(1543273)

['12', '34', '56', '78', '90']
_l_(1543274)

