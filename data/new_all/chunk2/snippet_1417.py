# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61275826/python-trying-to-randomly-select-the-value-from-list-within-a-list-results-in-th
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(425246)

except ImportError:
    pass
try:
    import string
    _l_(425248)

except ImportError:
    pass

def passwordGenerator():
    _l_(425300)

    lowerchars      =   _c_(425252, _n_(425249, "list", lambda: list), _a_(425251, _n_(425250, "string", lambda: string), "ascii_lowercase"))
    _l_(425253)
    upperchars      =   _c_(425257, _n_(425254, "list", lambda: list), _a_(425256, _n_(425255, "string", lambda: string), "ascii_uppercase"))
    _l_(425258)
    speciachars     =   ['&','!','_','@']
    _l_(425259)
    numericchars    =   _c_(425263, _n_(425260, "list", lambda: list), _c_(425262, _n_(425261, "range", lambda: range), 0,9))
    _l_(425264)
    otherrandom     =   _c_(425272, _n_(425265, "list", lambda: list), _a_(425267, _n_(425266, "string", lambda: string), "ascii_lowercase"), _a_(425269, _n_(425268, "string", lambda: string), "ascii_uppercase"), _c_(425271, _n_(425270, "range", lambda: range), 0,9), ['&','!','_','@'])
    _l_(425273)
    #otherrandom     =   list(list(string.ascii_lowercase), list(string.ascii_uppercase) list(range(0,9)), ['&','!','_','@'])
    _c_(425279, _n_(425274, "print", lambda: print), _c_(425278, _a_(425276, _n_(425275, "random", lambda: random), "choice"), _n_(425277, "otherrandom", lambda: otherrandom)))
    _l_(425280)
    #print(random.choice(random.choice(otherrandom)))
    password        = _c_(425284, _a_(425282, _n_(425281, "random", lambda: random), "choice"), _n_(425283, "lowerchars", lambda: lowerchars)) + _c_(425288, _a_(425286, _n_(425285, "random", lambda: random), "choice"), _n_(425287, "upperchars", lambda: upperchars)) + _c_(425292, _a_(425290, _n_(425289, "random", lambda: random), "choice"), _n_(425291, "speciachars", lambda: speciachars)) + _c_(425298, _n_(425293, "str", lambda: str), _c_(425297, _a_(425295, _n_(425294, "random", lambda: random), "choice"), _n_(425296, "numericchars", lambda: numericchars)))
    _l_(425299)

_c_(425302, _n_(425301, "passwordGenerator", lambda: passwordGenerator))
_l_(425303)