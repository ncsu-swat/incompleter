# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import difflib
    _l_(31292)

except ImportError:
    pass

def string_similarity(str1, str2):
    _l_(31307)

    result = _c_(31301, _a_(31294, _n_(31293, "difflib", lambda: difflib), "SequenceMatcher"), a=_c_(31297, _a_(31296, _n_(31295, "str1", lambda: str1), "lower")), b=_c_(31300, _a_(31299, _n_(31298, "str2", lambda: str2), "lower")))
    _l_(31302)
    aux = _c_(31305, _a_(31304, _n_(31303, "result", lambda: result), "ratio"))
    _l_(31306)
    return aux
str2 = 'Python Exercises'
_l_(31308)
_c_(31310, _n_(31309, "print", lambda: print), 'Original string:')
_l_(31311)
_c_(31314, _n_(31312, "print", lambda: print), _n_(31313, "str1", lambda: str1))
_l_(31315)
_c_(31318, _n_(31316, "print", lambda: print), _n_(31317, "str2", lambda: str2))
_l_(31319)
_c_(31321, _n_(31320, "print", lambda: print), 'Similarity between two said strings:')
_l_(31322)
_c_(31328, _n_(31323, "print", lambda: print), _c_(31327, _n_(31324, "string_similarity", lambda: string_similarity), _n_(31325, "str1", lambda: str1), _n_(31326, "str2", lambda: str2)))
_l_(31329)
str1 = 'Python Exercises'
_l_(31330)
str2 = 'Python Exercise'
_l_(31331)
_c_(31333, _n_(31332, "print", lambda: print), '\nOriginal string:')
_l_(31334)
_c_(31337, _n_(31335, "print", lambda: print), _n_(31336, "str1", lambda: str1))
_l_(31338)
_c_(31341, _n_(31339, "print", lambda: print), _n_(31340, "str2", lambda: str2))
_l_(31342)
_c_(31344, _n_(31343, "print", lambda: print), 'Similarity between two said strings:')
_l_(31345)
_c_(31351, _n_(31346, "print", lambda: print), _c_(31350, _n_(31347, "string_similarity", lambda: string_similarity), _n_(31348, "str1", lambda: str1), _n_(31349, "str2", lambda: str2)))
_l_(31352)
str1 = 'Python Exercises'
_l_(31353)
str2 = 'Python Ex.'
_l_(31354)
_c_(31356, _n_(31355, "print", lambda: print), '\nOriginal string:')
_l_(31357)
_c_(31360, _n_(31358, "print", lambda: print), _n_(31359, "str1", lambda: str1))
_l_(31361)
_c_(31364, _n_(31362, "print", lambda: print), _n_(31363, "str2", lambda: str2))
_l_(31365)
_c_(31367, _n_(31366, "print", lambda: print), 'Similarity between two said strings:')
_l_(31368)
_c_(31374, _n_(31369, "print", lambda: print), _c_(31373, _n_(31370, "string_similarity", lambda: string_similarity), _n_(31371, "str1", lambda: str1), _n_(31372, "str2", lambda: str2)))
_l_(31375)
str1 = 'Python Exercises'
_l_(31376)
str2 = 'Python'
_l_(31377)
_c_(31379, _n_(31378, "print", lambda: print), '\nOriginal string:')
_l_(31380)
_c_(31383, _n_(31381, "print", lambda: print), _n_(31382, "str1", lambda: str1))
_l_(31384)
_c_(31387, _n_(31385, "print", lambda: print), _n_(31386, "str2", lambda: str2))
_l_(31388)
_c_(31390, _n_(31389, "print", lambda: print), 'Similarity between two said strings:')
_l_(31391)
_c_(31397, _n_(31392, "print", lambda: print), _c_(31396, _n_(31393, "string_similarity", lambda: string_similarity), _n_(31394, "str1", lambda: str1), _n_(31395, "str2", lambda: str2)))
_l_(31398)
str1 = 'Python Exercises'
_l_(31399)
str1 = 'Java Exercises'
_l_(31400)
_c_(31402, _n_(31401, "print", lambda: print), '\nOriginal string:')
_l_(31403)
_c_(31406, _n_(31404, "print", lambda: print), _n_(31405, "str1", lambda: str1))
_l_(31407)
_c_(31410, _n_(31408, "print", lambda: print), _n_(31409, "str2", lambda: str2))
_l_(31411)
_c_(31413, _n_(31412, "print", lambda: print), 'Similarity between two said strings:')
_l_(31414)
_c_(31420, _n_(31415, "print", lambda: print), _c_(31419, _n_(31416, "string_similarity", lambda: string_similarity), _n_(31417, "str1", lambda: str1), _n_(31418, "str2", lambda: str2)))
_l_(31421)