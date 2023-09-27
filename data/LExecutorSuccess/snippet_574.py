# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
mystring = 'Hello World, this should work!'
_l_(1541183)
find_all = lambda c,s: [_n_(1541184, "x", lambda: x) for x in _c_(1541193, _n_(1541185, "range", lambda: range), _c_(1541189, _a_(1541187, _n_(1541186, "c", lambda: c), "find"), _n_(1541188, "s", lambda: s)), _c_(1541192, _n_(1541190, "len", lambda: len), _n_(1541191, "c", lambda: c))) if _n_(1541194, "c", lambda: c)[_n_(1541195, "x", lambda: x)] == _n_(1541196, "s", lambda: s)]
_l_(1541197)

# s represents the search string
# c represents the character string

_c_(1541200, _n_(1541198, "find_all", lambda: find_all), _n_(1541199, "mystring", lambda: mystring),'o')    # will return all positions of 'o'
_l_(1541201)    # will return all positions of 'o'

[4, 7, 20, 26] 
_l_(1541202) 


