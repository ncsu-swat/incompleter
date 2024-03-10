# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54496411/python-errortypeerror-findall-missing-1-required-positional-argument-stri
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(426229)

except ImportError:
    pass
#import csv

text = _c_(426231, _n_(426230, "open", lambda: open), r'C:\Users\Vincent\Documents\python\theSortingHat\100000DirtyNames.txt') #open text file
_l_(426232) #open text file
for line in _n_(426233, "text", lambda: text):
    _l_(426244)

    #return list of names in that line
    x = _c_(426236, _a_(426235, _n_(426234, "re", lambda: re), "findall"), '^([a-zA-Z]-?$')
    _l_(426237)
    #if an actual name is found
    if _n_(426238, "x", lambda: x) != 0:
        _l_(426243)

        _c_(426241, _n_(426239, "print", lambda: print), _n_(426240, "x", lambda: x))
        _l_(426242)