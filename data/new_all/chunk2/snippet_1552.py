# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/31771559/finding-most-frequent-number-in-a-list-typeerror-unhashable-type-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
   from collections import Counter
   _l_(430980)

except ImportError:
   pass
def opportunity(a,h):
   _l_(431001)

   ar = []
   _l_(430981)
   _c_(430991, _a_(430983, _n_(430982, "ar", lambda: ar), "append"), [_n_(430984, "row", lambda: row)[_n_(430985, "h", lambda: h)] for row in _n_(430986, "a", lambda: a) if _c_(430989, _n_(430987, "len", lambda: len), _n_(430988, "row", lambda: row))>_n_(430990, "h", lambda: h)] )
   _l_(430992)
   b = _c_(430995, _n_(430993, "Counter", lambda: Counter), _n_(430994, "ar", lambda: ar))
   _l_(430996)
   aux = _c_(430999, _a_(430998, _n_(430997, "b", lambda: b), "most_common"), 1)
   _l_(431000)
   return aux

next = _c_(431005, _n_(431002, "opportunity", lambda: opportunity), _n_(431003, "take", lambda: take), _n_(431004, "head", lambda: head))
_l_(431006)