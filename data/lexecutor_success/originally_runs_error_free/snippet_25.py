# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1024847/how-can-i-add-new-keys-to-a-dictionary
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x = {1:2}
_l_(1547443)
_c_(1547446, _n_(1547444, "print", lambda: print), _n_(1547445, "x", lambda: x))
_l_(1547447)
{1: 2}
_l_(1547448)

d = {3:4, 5:6, 7:8}
_l_(1547449)
_c_(1547453, _a_(1547451, _n_(1547450, "x", lambda: x), "update"), _n_(1547452, "d", lambda: d))
_l_(1547454)
_c_(1547457, _n_(1547455, "print", lambda: print), _n_(1547456, "x", lambda: x))
_l_(1547458)
{1: 2, 3: 4, 5: 6, 7: 8}
_l_(1547459)

