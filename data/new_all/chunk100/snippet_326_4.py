# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import difflib
    _l_(31947)

except ImportError:
    pass

def string_similarity(str1, str2):
    _l_(31962)

    result = _c_(31956, _a_(31949, _n_(31948, "difflib", lambda: difflib), "SequenceMatcher"), a=_c_(31952, _a_(31951, _n_(31950, "str1", lambda: str1), "lower")), b=_c_(31955, _a_(31954, _n_(31953, "str2", lambda: str2), "lower")))
    _l_(31957)
    aux = _c_(31960, _a_(31959, _n_(31958, "result", lambda: result), "ratio"))
    _l_(31961)
    return aux
str1 = 'Python Exercises'
_l_(31963)
str2 = 'Python Exercises'
_l_(31964)
_c_(31966, _n_(31965, "print", lambda: print), 'Original string:')
_l_(31967)
_c_(31970, _n_(31968, "print", lambda: print), _n_(31969, "str1", lambda: str1))
_l_(31971)
_c_(31974, _n_(31972, "print", lambda: print), _n_(31973, "str2", lambda: str2))
_l_(31975)
_c_(31977, _n_(31976, "print", lambda: print), 'Similarity between two said strings:')
_l_(31978)
_c_(31984, _n_(31979, "print", lambda: print), _c_(31983, _n_(31980, "string_similarity", lambda: string_similarity), _n_(31981, "str1", lambda: str1), _n_(31982, "str2", lambda: str2)))
_l_(31985)
str1 = 'Python Exercises'
_l_(31986)
str2 = 'Python Exercise'
_l_(31987)
_c_(31989, _n_(31988, "print", lambda: print), '\nOriginal string:')
_l_(31990)
_c_(31993, _n_(31991, "print", lambda: print), _n_(31992, "str1", lambda: str1))
_l_(31994)
_c_(31997, _n_(31995, "print", lambda: print), _n_(31996, "str2", lambda: str2))
_l_(31998)
_c_(32000, _n_(31999, "print", lambda: print), 'Similarity between two said strings:')
_l_(32001)
_c_(32007, _n_(32002, "print", lambda: print), _c_(32006, _n_(32003, "string_similarity", lambda: string_similarity), _n_(32004, "str1", lambda: str1), _n_(32005, "str2", lambda: str2)))
_l_(32008)
str1 = 'Python Exercises'
_l_(32009)
str2 = 'Python Ex.'
_l_(32010)
_c_(32012, _n_(32011, "print", lambda: print), '\nOriginal string:')
_l_(32013)
_c_(32016, _n_(32014, "print", lambda: print), _n_(32015, "str1", lambda: str1))
_l_(32017)
_c_(32020, _n_(32018, "print", lambda: print), _n_(32019, "str2", lambda: str2))
_l_(32021)
_c_(32023, _n_(32022, "print", lambda: print), 'Similarity between two said strings:')
_l_(32024)
_c_(32030, _n_(32025, "print", lambda: print), _c_(32029, _n_(32026, "string_similarity", lambda: string_similarity), _n_(32027, "str1", lambda: str1), _n_(32028, "str2", lambda: str2)))
_l_(32031)
str1 = 'Python Exercises'
_l_(32032)
str2 = 'Python'
_l_(32033)
_c_(32035, _n_(32034, "print", lambda: print), '\nOriginal string:')
_l_(32036)
_c_(32039, _n_(32037, "print", lambda: print), _n_(32038, "str1", lambda: str1))
_l_(32040)
_c_(32043, _n_(32041, "print", lambda: print), _n_(32042, "str2", lambda: str2))
_l_(32044)
_c_(32046, _n_(32045, "print", lambda: print), 'Similarity between two said strings:')
_l_(32047)
_c_(32053, _n_(32048, "print", lambda: print), _c_(32052, _n_(32049, "string_similarity", lambda: string_similarity), _n_(32050, "str1", lambda: str1), _n_(32051, "str2", lambda: str2)))
_l_(32054)
str1 = 'Java Exercises'
_l_(32055)
_c_(32057, _n_(32056, "print", lambda: print), '\nOriginal string:')
_l_(32058)
_c_(32061, _n_(32059, "print", lambda: print), _n_(32060, "str1", lambda: str1))
_l_(32062)
_c_(32065, _n_(32063, "print", lambda: print), _n_(32064, "str2", lambda: str2))
_l_(32066)
_c_(32068, _n_(32067, "print", lambda: print), 'Similarity between two said strings:')
_l_(32069)
_c_(32075, _n_(32070, "print", lambda: print), _c_(32074, _n_(32071, "string_similarity", lambda: string_similarity), _n_(32072, "str1", lambda: str1), _n_(32073, "str2", lambda: str2)))
_l_(32076)