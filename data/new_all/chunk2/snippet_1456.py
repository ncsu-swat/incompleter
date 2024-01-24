# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56210112/error-using-exp-in-sympy-typeerror-and-attribute-error-is-displayed
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import math
    _l_(421138)

except ImportError:
    pass
try:
    import sympy as sym
    _l_(421140)

except ImportError:
    pass
try:
    from sympy import symbols, diff, exp, log, power
    _l_(421142)

except ImportError:
    pass
try:
    from sympy import *
    _l_(421144)

except ImportError:
    pass

data = [3, 33, 146, 227, 342, 351, 353, 444, 556, 571, 709, 759, 836, 860, 968, 1056, 1726, 1846, 1872, 1986, 2311, 2366, 2608, 2676, 3098, 3278, 3288, 4434, 5034, 5049, 5085, 5089, 5089, 5097, 5324, 5389,5565, 5623, 6080, 6380, 6477, 6740, 7192, 7447, 7644, 7837, 7843, 7922, 8738, 10089, 10237, 10258, 10491, 10625, 10982, 11175, 11411, 11442, 11811, 12559, 12559, 12791, 13121, 13486, 14708, 15251, 15261, 15277, 15806, 16185, 16229, 16358, 17168, 17458, 17758, 18287, 18568, 18728, 19556, 20567, 21012, 21308, 23063, 24127, 25910, 26770, 27753, 28460, 28493, 29361, 30085, 32408, 35338, 36799, 37642, 37654, 37915, 39715, 40580, 42015, 42045, 42188, 42296, 42296, 45406, 46653, 47596, 48296, 49171, 49416, 50145, 52042, 52489, 52875, 53321, 53443, 54433, 55381, 56463, 56485, 56560, 57042, 62551, 62651, 62661, 63732, 64103, 64893, 71043, 74364, 75409, 76057, 81542, 82702, 84566, 88682]
_l_(421145)
n = _c_(421148, _n_(421146, "len", lambda: len), _n_(421147, "data", lambda: data))
_l_(421149)
tn = _n_(421150, "data", lambda: data)[_n_(421151, "n", lambda: n)-1]
_l_(421152)


b, c = _c_(421155, _a_(421154, _n_(421153, "sym", lambda: sym), "symbols"), 'b c', real=True)
_l_(421156)

f = -(-_n_(421157, "n", lambda: n) +_c_(421177, _n_(421158, "sum", lambda: sum), _c_(421176, _a_(421160, _n_(421159, "np", lambda: np), "log"), _n_(421161, "b", lambda: b)*_n_(421162, "c", lambda: c)*_c_(421167, _a_(421164, _n_(421163, "np", lambda: np), "power"), _n_(421165, "data", lambda: data),(_n_(421166, "c", lambda: c)-1))*_c_(421175, _n_(421168, "exp", lambda: exp), -_n_(421169, "b", lambda: b)*_c_(421174, _a_(421171, _n_(421170, "np", lambda: np), "power"), _n_(421172, "data", lambda: data),_n_(421173, "c", lambda: c))))))
_l_(421178)

_c_(421182, _n_(421179, "diff", lambda: diff), _n_(421180, "f", lambda: f),_n_(421181, "b", lambda: b))
_l_(421183)
_c_(421187, _n_(421184, "diff", lambda: diff), _n_(421185, "f", lambda: f),_n_(421186, "c", lambda: c))
_l_(421188)