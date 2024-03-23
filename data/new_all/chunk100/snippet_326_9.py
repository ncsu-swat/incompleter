# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import difflib
    _l_(32593)

except ImportError:
    pass

def string_similarity(str1, str2):
    _l_(32608)

    result = _c_(32602, _a_(32595, _n_(32594, "difflib", lambda: difflib), "SequenceMatcher"), a=_c_(32598, _a_(32597, _n_(32596, "str1", lambda: str1), "lower")), b=_c_(32601, _a_(32600, _n_(32599, "str2", lambda: str2), "lower")))
    _l_(32603)
    aux = _c_(32606, _a_(32605, _n_(32604, "result", lambda: result), "ratio"))
    _l_(32607)
    return aux
str1 = 'Python Exercises'
_l_(32609)
str2 = 'Python Exercises'
_l_(32610)
_c_(32612, _n_(32611, "print", lambda: print), 'Original string:')
_l_(32613)
_c_(32616, _n_(32614, "print", lambda: print), _n_(32615, "str1", lambda: str1))
_l_(32617)
_c_(32620, _n_(32618, "print", lambda: print), _n_(32619, "str2", lambda: str2))
_l_(32621)
_c_(32623, _n_(32622, "print", lambda: print), 'Similarity between two said strings:')
_l_(32624)
_c_(32630, _n_(32625, "print", lambda: print), _c_(32629, _n_(32626, "string_similarity", lambda: string_similarity), _n_(32627, "str1", lambda: str1), _n_(32628, "str2", lambda: str2)))
_l_(32631)
str1 = 'Python Exercises'
_l_(32632)
str2 = 'Python Exercise'
_l_(32633)
_c_(32635, _n_(32634, "print", lambda: print), '\nOriginal string:')
_l_(32636)
_c_(32639, _n_(32637, "print", lambda: print), _n_(32638, "str1", lambda: str1))
_l_(32640)
_c_(32643, _n_(32641, "print", lambda: print), _n_(32642, "str2", lambda: str2))
_l_(32644)
_c_(32646, _n_(32645, "print", lambda: print), 'Similarity between two said strings:')
_l_(32647)
_c_(32653, _n_(32648, "print", lambda: print), _c_(32652, _n_(32649, "string_similarity", lambda: string_similarity), _n_(32650, "str1", lambda: str1), _n_(32651, "str2", lambda: str2)))
_l_(32654)
str1 = 'Python Exercises'
_l_(32655)
str2 = 'Python Ex.'
_l_(32656)
_c_(32658, _n_(32657, "print", lambda: print), '\nOriginal string:')
_l_(32659)
_c_(32662, _n_(32660, "print", lambda: print), _n_(32661, "str1", lambda: str1))
_l_(32663)
_c_(32666, _n_(32664, "print", lambda: print), _n_(32665, "str2", lambda: str2))
_l_(32667)
_c_(32669, _n_(32668, "print", lambda: print), 'Similarity between two said strings:')
_l_(32670)
_c_(32676, _n_(32671, "print", lambda: print), _c_(32675, _n_(32672, "string_similarity", lambda: string_similarity), _n_(32673, "str1", lambda: str1), _n_(32674, "str2", lambda: str2)))
_l_(32677)
str2 = 'Python'
_l_(32678)
_c_(32680, _n_(32679, "print", lambda: print), '\nOriginal string:')
_l_(32681)
_c_(32684, _n_(32682, "print", lambda: print), _n_(32683, "str1", lambda: str1))
_l_(32685)
_c_(32688, _n_(32686, "print", lambda: print), _n_(32687, "str2", lambda: str2))
_l_(32689)
_c_(32691, _n_(32690, "print", lambda: print), 'Similarity between two said strings:')
_l_(32692)
_c_(32698, _n_(32693, "print", lambda: print), _c_(32697, _n_(32694, "string_similarity", lambda: string_similarity), _n_(32695, "str1", lambda: str1), _n_(32696, "str2", lambda: str2)))
_l_(32699)
str1 = 'Python Exercises'
_l_(32700)
str1 = 'Java Exercises'
_l_(32701)
_c_(32703, _n_(32702, "print", lambda: print), '\nOriginal string:')
_l_(32704)
_c_(32707, _n_(32705, "print", lambda: print), _n_(32706, "str1", lambda: str1))
_l_(32708)
_c_(32711, _n_(32709, "print", lambda: print), _n_(32710, "str2", lambda: str2))
_l_(32712)
_c_(32714, _n_(32713, "print", lambda: print), 'Similarity between two said strings:')
_l_(32715)
_c_(32721, _n_(32716, "print", lambda: print), _c_(32720, _n_(32717, "string_similarity", lambda: string_similarity), _n_(32718, "str1", lambda: str1), _n_(32719, "str2", lambda: str2)))
_l_(32722)