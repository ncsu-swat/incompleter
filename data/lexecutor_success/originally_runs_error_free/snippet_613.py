# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3257919/what-is-the-difference-between-is-none-and-none
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
p = [1]
_l_(1543903)
q = [1]
_l_(1543904)
_n_(1543905, "p", lambda: p) is _n_(1543906, "q", lambda: q) # False because they are not the same actual object
_l_(1543907) # False because they are not the same actual object
_n_(1543908, "p", lambda: p) == _n_(1543909, "q", lambda: q) # True because they are equivalent
_l_(1543910) # True because they are equivalent

p = None
_l_(1543911)
q = None
_l_(1543912)
_n_(1543913, "p", lambda: p) is _n_(1543914, "q", lambda: q) # True because they are both pointing to the same "None"
_l_(1543915) # True because they are both pointing to the same "None"

