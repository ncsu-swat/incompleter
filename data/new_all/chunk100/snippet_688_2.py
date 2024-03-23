# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
words = ['red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes', 'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange', 'white', 'black', 'pink', 'green', 'green', 'pink', 'green', 'pink', 'white', 'orange', 'orange', 'red']
_l_(71237)
try:
    from collections import Counter
    _l_(71239)

except ImportError:
    pass
word_counts = _c_(71242, _n_(71240, "Counter", lambda: Counter), _n_(71241, "words", lambda: words))
_l_(71243)
_c_(71246, _n_(71244, "print", lambda: print), _n_(71245, "top_four", lambda: top_four))
_l_(71247)