# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63065061/why-do-i-get-attributeerror-when-i-run-this-code
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(700758)

except ImportError:
    pass
try:
    import re
    _l_(700760)

except ImportError:
    pass
  

s = _c_(700762, _n_(700761, "open", lambda: open), 'filename.txt', 'r')
_l_(700763)
words = _c_(700769, _a_(700765, _n_(700764, "re", lambda: re), "findall"), '\w+', _c_(700768, _a_(700767, _n_(700766, "s", lambda: s), "lower")))
_l_(700770)
c = _c_(700773, _n_(700771, "Counter", lambda: Counter), _n_(700772, "words", lambda: words))
_l_(700774)

for word, freq in _c_(700777, _a_(700776, _n_(700775, "c", lambda: c), "most_common"), 10):
    _l_(700783)

    _c_(700781, _n_(700778, "print", lambda: print), _n_(700779, "word", lambda: word), ':' , _n_(700780, "freq", lambda: freq))
    _l_(700782)