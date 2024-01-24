# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/33423431/python-3-5-0-typeerror-cant-multiply-sequence-by-non-int-of-type-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(621542)

except ImportError:
    pass

f= _c_(621544, _n_(621543, "open", lambda: open), 'file.txt','r')
_l_(621545)
namesList = []
_l_(621546)

for line in _n_(621547, "f", lambda: f):
    _l_(621555)

    _c_(621553, _a_(621549, _n_(621548, "namesList", lambda: namesList), "append"), _c_(621552, _a_(621551, _n_(621550, "line", lambda: line), "strip")))
    _l_(621554)

_c_(621565, _n_(621556, "print", lambda: print), 'There are %d names in list and we will choose %.0f from the list.' % (_c_(621559, _n_(621557, "len", lambda: len), _n_(621558, "namesList", lambda: namesList)), _c_(621564, _n_(621560, "float", lambda: float), _c_(621563, _n_(621561, "len", lambda: len), _n_(621562, "namesList", lambda: namesList)))*0.25))
_l_(621566)

_c_(621575, _n_(621567, "print", lambda: print), 'Names choosed was %s' % _c_(621574, _a_(621569, _n_(621568, "random", lambda: random), "sample"), _n_(621570, "namesList", lambda: namesList), _c_(621573, _n_(621571, "len", lambda: len), _n_(621572, "namesList", lambda: namesList))*0.25))
_l_(621576)

_c_(621579, _a_(621578, _n_(621577, "f", lambda: f), "close"))
_l_(621580)