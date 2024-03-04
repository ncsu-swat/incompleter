# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9884132/what-are-iterator-iterable-and-iteration
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x=[1,2,3,4]
_l_(63671)

y=_c_(63674, _n_(63672, "iter", lambda: iter), _n_(63673, "x", lambda: x))
_l_(63675)

y=[1,2,3,4]
_l_(63676)

_c_(63679, _a_(63678, _n_(63677, "y", lambda: y), "next"))
_l_(63680)
1
_l_(63681)
_c_(63684, _a_(63683, _n_(63682, "y", lambda: y), "next"))
_l_(63685)
2
_l_(63686)
_c_(63689, _a_(63688, _n_(63687, "y", lambda: y), "next"))
_l_(63690)
3
_l_(63691)
_c_(63694, _a_(63693, _n_(63692, "y", lambda: y), "next"))
_l_(63695)
4
_l_(63696)
_c_(63699, _a_(63698, _n_(63697, "y", lambda: y), "next"))
_l_(63700)
_n_(63701, "StopIteration", lambda: StopIteration)
_l_(63702)

