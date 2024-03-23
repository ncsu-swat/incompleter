# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import difflib
    _l_(31685)

except ImportError:
    pass

def string_similarity(str1, str2):
    _l_(31700)

    result = _c_(31694, _a_(31687, _n_(31686, "difflib", lambda: difflib), "SequenceMatcher"), a=_c_(31690, _a_(31689, _n_(31688, "str1", lambda: str1), "lower")), b=_c_(31693, _a_(31692, _n_(31691, "str2", lambda: str2), "lower")))
    _l_(31695)
    aux = _c_(31698, _a_(31697, _n_(31696, "result", lambda: result), "ratio"))
    _l_(31699)
    return aux
str1 = 'Python Exercises'
_l_(31701)
str2 = 'Python Exercises'
_l_(31702)
_c_(31704, _n_(31703, "print", lambda: print), 'Original string:')
_l_(31705)
_c_(31708, _n_(31706, "print", lambda: print), _n_(31707, "str1", lambda: str1))
_l_(31709)
_c_(31712, _n_(31710, "print", lambda: print), _n_(31711, "str2", lambda: str2))
_l_(31713)
_c_(31715, _n_(31714, "print", lambda: print), 'Similarity between two said strings:')
_l_(31716)
_c_(31722, _n_(31717, "print", lambda: print), _c_(31721, _n_(31718, "string_similarity", lambda: string_similarity), _n_(31719, "str1", lambda: str1), _n_(31720, "str2", lambda: str2)))
_l_(31723)
str1 = 'Python Exercises'
_l_(31724)
str2 = 'Python Exercise'
_l_(31725)
_c_(31727, _n_(31726, "print", lambda: print), '\nOriginal string:')
_l_(31728)
_c_(31731, _n_(31729, "print", lambda: print), _n_(31730, "str1", lambda: str1))
_l_(31732)
_c_(31735, _n_(31733, "print", lambda: print), _n_(31734, "str2", lambda: str2))
_l_(31736)
_c_(31738, _n_(31737, "print", lambda: print), 'Similarity between two said strings:')
_l_(31739)
_c_(31745, _n_(31740, "print", lambda: print), _c_(31744, _n_(31741, "string_similarity", lambda: string_similarity), _n_(31742, "str1", lambda: str1), _n_(31743, "str2", lambda: str2)))
_l_(31746)
str2 = 'Python Ex.'
_l_(31747)
_c_(31749, _n_(31748, "print", lambda: print), '\nOriginal string:')
_l_(31750)
_c_(31753, _n_(31751, "print", lambda: print), _n_(31752, "str1", lambda: str1))
_l_(31754)
_c_(31757, _n_(31755, "print", lambda: print), _n_(31756, "str2", lambda: str2))
_l_(31758)
_c_(31760, _n_(31759, "print", lambda: print), 'Similarity between two said strings:')
_l_(31761)
_c_(31767, _n_(31762, "print", lambda: print), _c_(31766, _n_(31763, "string_similarity", lambda: string_similarity), _n_(31764, "str1", lambda: str1), _n_(31765, "str2", lambda: str2)))
_l_(31768)
str1 = 'Python Exercises'
_l_(31769)
str2 = 'Python'
_l_(31770)
_c_(31772, _n_(31771, "print", lambda: print), '\nOriginal string:')
_l_(31773)
_c_(31776, _n_(31774, "print", lambda: print), _n_(31775, "str1", lambda: str1))
_l_(31777)
_c_(31780, _n_(31778, "print", lambda: print), _n_(31779, "str2", lambda: str2))
_l_(31781)
_c_(31783, _n_(31782, "print", lambda: print), 'Similarity between two said strings:')
_l_(31784)
_c_(31790, _n_(31785, "print", lambda: print), _c_(31789, _n_(31786, "string_similarity", lambda: string_similarity), _n_(31787, "str1", lambda: str1), _n_(31788, "str2", lambda: str2)))
_l_(31791)
str1 = 'Python Exercises'
_l_(31792)
str1 = 'Java Exercises'
_l_(31793)
_c_(31795, _n_(31794, "print", lambda: print), '\nOriginal string:')
_l_(31796)
_c_(31799, _n_(31797, "print", lambda: print), _n_(31798, "str1", lambda: str1))
_l_(31800)
_c_(31803, _n_(31801, "print", lambda: print), _n_(31802, "str2", lambda: str2))
_l_(31804)
_c_(31806, _n_(31805, "print", lambda: print), 'Similarity between two said strings:')
_l_(31807)
_c_(31813, _n_(31808, "print", lambda: print), _c_(31812, _n_(31809, "string_similarity", lambda: string_similarity), _n_(31810, "str1", lambda: str1), _n_(31811, "str2", lambda: str2)))
_l_(31814)