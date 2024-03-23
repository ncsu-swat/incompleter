# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import difflib
    _l_(31554)

except ImportError:
    pass

def string_similarity(str1, str2):
    _l_(31569)

    result = _c_(31563, _a_(31556, _n_(31555, "difflib", lambda: difflib), "SequenceMatcher"), a=_c_(31559, _a_(31558, _n_(31557, "str1", lambda: str1), "lower")), b=_c_(31562, _a_(31561, _n_(31560, "str2", lambda: str2), "lower")))
    _l_(31564)
    aux = _c_(31567, _a_(31566, _n_(31565, "result", lambda: result), "ratio"))
    _l_(31568)
    return aux
str1 = 'Python Exercises'
_l_(31570)
str2 = 'Python Exercises'
_l_(31571)
_c_(31573, _n_(31572, "print", lambda: print), 'Original string:')
_l_(31574)
_c_(31577, _n_(31575, "print", lambda: print), _n_(31576, "str1", lambda: str1))
_l_(31578)
_c_(31581, _n_(31579, "print", lambda: print), _n_(31580, "str2", lambda: str2))
_l_(31582)
_c_(31584, _n_(31583, "print", lambda: print), 'Similarity between two said strings:')
_l_(31585)
_c_(31591, _n_(31586, "print", lambda: print), _c_(31590, _n_(31587, "string_similarity", lambda: string_similarity), _n_(31588, "str1", lambda: str1), _n_(31589, "str2", lambda: str2)))
_l_(31592)
str1 = 'Python Exercises'
_l_(31593)
str2 = 'Python Exercise'
_l_(31594)
_c_(31596, _n_(31595, "print", lambda: print), '\nOriginal string:')
_l_(31597)
_c_(31600, _n_(31598, "print", lambda: print), _n_(31599, "str1", lambda: str1))
_l_(31601)
_c_(31604, _n_(31602, "print", lambda: print), _n_(31603, "str2", lambda: str2))
_l_(31605)
_c_(31607, _n_(31606, "print", lambda: print), 'Similarity between two said strings:')
_l_(31608)
_c_(31614, _n_(31609, "print", lambda: print), _c_(31613, _n_(31610, "string_similarity", lambda: string_similarity), _n_(31611, "str1", lambda: str1), _n_(31612, "str2", lambda: str2)))
_l_(31615)
str1 = 'Python Exercises'
_l_(31616)
_c_(31618, _n_(31617, "print", lambda: print), '\nOriginal string:')
_l_(31619)
_c_(31622, _n_(31620, "print", lambda: print), _n_(31621, "str1", lambda: str1))
_l_(31623)
_c_(31626, _n_(31624, "print", lambda: print), _n_(31625, "str2", lambda: str2))
_l_(31627)
_c_(31629, _n_(31628, "print", lambda: print), 'Similarity between two said strings:')
_l_(31630)
_c_(31636, _n_(31631, "print", lambda: print), _c_(31635, _n_(31632, "string_similarity", lambda: string_similarity), _n_(31633, "str1", lambda: str1), _n_(31634, "str2", lambda: str2)))
_l_(31637)
str1 = 'Python Exercises'
_l_(31638)
str2 = 'Python'
_l_(31639)
_c_(31641, _n_(31640, "print", lambda: print), '\nOriginal string:')
_l_(31642)
_c_(31645, _n_(31643, "print", lambda: print), _n_(31644, "str1", lambda: str1))
_l_(31646)
_c_(31649, _n_(31647, "print", lambda: print), _n_(31648, "str2", lambda: str2))
_l_(31650)
_c_(31652, _n_(31651, "print", lambda: print), 'Similarity between two said strings:')
_l_(31653)
_c_(31659, _n_(31654, "print", lambda: print), _c_(31658, _n_(31655, "string_similarity", lambda: string_similarity), _n_(31656, "str1", lambda: str1), _n_(31657, "str2", lambda: str2)))
_l_(31660)
str1 = 'Python Exercises'
_l_(31661)
str1 = 'Java Exercises'
_l_(31662)
_c_(31664, _n_(31663, "print", lambda: print), '\nOriginal string:')
_l_(31665)
_c_(31668, _n_(31666, "print", lambda: print), _n_(31667, "str1", lambda: str1))
_l_(31669)
_c_(31672, _n_(31670, "print", lambda: print), _n_(31671, "str2", lambda: str2))
_l_(31673)
_c_(31675, _n_(31674, "print", lambda: print), 'Similarity between two said strings:')
_l_(31676)
_c_(31682, _n_(31677, "print", lambda: print), _c_(31681, _n_(31678, "string_similarity", lambda: string_similarity), _n_(31679, "str1", lambda: str1), _n_(31680, "str2", lambda: str2)))
_l_(31683)