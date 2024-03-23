# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(71224)

except ImportError:
    pass
word_counts = _c_(71227, _n_(71225, "Counter", lambda: Counter), _n_(71226, "words", lambda: words))
_l_(71228)
top_four = _c_(71231, _a_(71230, _n_(71229, "word_counts", lambda: word_counts), "most_common"), 4)
_l_(71232)
_c_(71235, _n_(71233, "print", lambda: print), _n_(71234, "top_four", lambda: top_four))
_l_(71236)