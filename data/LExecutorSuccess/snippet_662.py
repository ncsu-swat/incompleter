# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1233448/no-multiline-lambda-in-python-why-not
#%%
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x = 1
_l_(1544907)
y = 2
_l_(1544908)

q = _c_(1544918, _n_(1544909, "list", lambda: list), _c_(1544917, _n_(1544910, "map", lambda: map), lambda t: (
    tx := _n_(1544911, "t", lambda: t)*_n_(1544912, "x", lambda: x),
    ty := _n_(1544913, "t", lambda: t)*_n_(1544914, "y", lambda: y),
    _n_(1544915, "tx", lambda: tx)+_n_(1544916, "ty", lambda: ty)
)[-1], [1, 2, 3]))
_l_(1544919)

_c_(1544922, _n_(1544920, "print", lambda: print), _n_(1544921, "q", lambda: q))
_l_(1544923)

