# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import difflib
    _l_(31816)

except ImportError:
    pass

def string_similarity(str1, str2):
    _l_(31831)

    result = _c_(31825, _a_(31818, _n_(31817, "difflib", lambda: difflib), "SequenceMatcher"), a=_c_(31821, _a_(31820, _n_(31819, "str1", lambda: str1), "lower")), b=_c_(31824, _a_(31823, _n_(31822, "str2", lambda: str2), "lower")))
    _l_(31826)
    aux = _c_(31829, _a_(31828, _n_(31827, "result", lambda: result), "ratio"))
    _l_(31830)
    return aux
str1 = 'Python Exercises'
_l_(31832)
str2 = 'Python Exercises'
_l_(31833)
_c_(31835, _n_(31834, "print", lambda: print), 'Original string:')
_l_(31836)
_c_(31839, _n_(31837, "print", lambda: print), _n_(31838, "str1", lambda: str1))
_l_(31840)
_c_(31843, _n_(31841, "print", lambda: print), _n_(31842, "str2", lambda: str2))
_l_(31844)
_c_(31846, _n_(31845, "print", lambda: print), 'Similarity between two said strings:')
_l_(31847)
_c_(31853, _n_(31848, "print", lambda: print), _c_(31852, _n_(31849, "string_similarity", lambda: string_similarity), _n_(31850, "str1", lambda: str1), _n_(31851, "str2", lambda: str2)))
_l_(31854)
str1 = 'Python Exercises'
_l_(31855)
_c_(31857, _n_(31856, "print", lambda: print), '\nOriginal string:')
_l_(31858)
_c_(31861, _n_(31859, "print", lambda: print), _n_(31860, "str1", lambda: str1))
_l_(31862)
_c_(31865, _n_(31863, "print", lambda: print), _n_(31864, "str2", lambda: str2))
_l_(31866)
_c_(31868, _n_(31867, "print", lambda: print), 'Similarity between two said strings:')
_l_(31869)
_c_(31875, _n_(31870, "print", lambda: print), _c_(31874, _n_(31871, "string_similarity", lambda: string_similarity), _n_(31872, "str1", lambda: str1), _n_(31873, "str2", lambda: str2)))
_l_(31876)
str1 = 'Python Exercises'
_l_(31877)
str2 = 'Python Ex.'
_l_(31878)
_c_(31880, _n_(31879, "print", lambda: print), '\nOriginal string:')
_l_(31881)
_c_(31884, _n_(31882, "print", lambda: print), _n_(31883, "str1", lambda: str1))
_l_(31885)
_c_(31888, _n_(31886, "print", lambda: print), _n_(31887, "str2", lambda: str2))
_l_(31889)
_c_(31891, _n_(31890, "print", lambda: print), 'Similarity between two said strings:')
_l_(31892)
_c_(31898, _n_(31893, "print", lambda: print), _c_(31897, _n_(31894, "string_similarity", lambda: string_similarity), _n_(31895, "str1", lambda: str1), _n_(31896, "str2", lambda: str2)))
_l_(31899)
str1 = 'Python Exercises'
_l_(31900)
str2 = 'Python'
_l_(31901)
_c_(31903, _n_(31902, "print", lambda: print), '\nOriginal string:')
_l_(31904)
_c_(31907, _n_(31905, "print", lambda: print), _n_(31906, "str1", lambda: str1))
_l_(31908)
_c_(31911, _n_(31909, "print", lambda: print), _n_(31910, "str2", lambda: str2))
_l_(31912)
_c_(31914, _n_(31913, "print", lambda: print), 'Similarity between two said strings:')
_l_(31915)
_c_(31921, _n_(31916, "print", lambda: print), _c_(31920, _n_(31917, "string_similarity", lambda: string_similarity), _n_(31918, "str1", lambda: str1), _n_(31919, "str2", lambda: str2)))
_l_(31922)
str1 = 'Python Exercises'
_l_(31923)
str1 = 'Java Exercises'
_l_(31924)
_c_(31926, _n_(31925, "print", lambda: print), '\nOriginal string:')
_l_(31927)
_c_(31930, _n_(31928, "print", lambda: print), _n_(31929, "str1", lambda: str1))
_l_(31931)
_c_(31934, _n_(31932, "print", lambda: print), _n_(31933, "str2", lambda: str2))
_l_(31935)
_c_(31937, _n_(31936, "print", lambda: print), 'Similarity between two said strings:')
_l_(31938)
_c_(31944, _n_(31939, "print", lambda: print), _c_(31943, _n_(31940, "string_similarity", lambda: string_similarity), _n_(31941, "str1", lambda: str1), _n_(31942, "str2", lambda: str2)))
_l_(31945)