# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
words = ['red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes', 'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange', 'white', 'black', 'pink', 'green', 'green', 'pink', 'green', 'pink', 'white', 'orange', 'orange', 'red']
_l_(71212)
try:
    from collections import Counter
    _l_(71214)

except ImportError:
    pass
top_four = _c_(71217, _a_(71216, _n_(71215, "word_counts", lambda: word_counts), "most_common"), 4)
_l_(71218)
_c_(71221, _n_(71219, "print", lambda: print), _n_(71220, "top_four", lambda: top_four))
_l_(71222)