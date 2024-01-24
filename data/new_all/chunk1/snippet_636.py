# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/32880712/grouping-anagrams-using-ordereddictionary-typeerror-issue
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(384428)

except ImportError:
    pass
try:
    from collections import *
    _l_(384430)

except ImportError:
    pass
def findAnagrams(string):
    _l_(384451)

    anagramDict = _c_(384433, _n_(384431, "OrderedDict", lambda: OrderedDict), _n_(384432, "list", lambda: list))
    _l_(384434)
    for word in _n_(384435, "string", lambda: string):
        _l_(384448)

        key = _c_(384440, _a_(384436, '', "join"), _c_(384439, _n_(384437, "sorted", lambda: sorted), _n_(384438, "word", lambda: word)))
        _l_(384441)
        _c_(384446, _a_(384444, _n_(384442, "anagramDict", lambda: anagramDict)[_n_(384443, "key", lambda: key)], "append"), _n_(384445, "word", lambda: word))
        _l_(384447)
    aux = _n_(384449, "anagramDict", lambda: anagramDict)
    _l_(384450)
    return aux

def main():
    _l_(384487)

    for string in _a_(384453, _n_(384452, "sys", lambda: sys), "stdin"):
        _l_(384486)

        stringList = _c_(384456, _a_(384455, _n_(384454, "string", lambda: string), "split"))
        _l_(384457)
        if _c_(384460, _n_(384458, "len", lambda: len), _n_(384459, "stringList", lambda: stringList)) == 0:
            _l_(384462)

            break
            _l_(384461)
        anagramDict = _c_(384465, _n_(384463, "findAnagrams", lambda: findAnagrams), _n_(384464, "stringList", lambda: stringList))
        _l_(384466)
        for key,anagrams in _c_(384469, _a_(384468, _n_(384467, "anagramDict", lambda: anagramDict), "items")):
            _l_(384482)

            if _c_(384472, _n_(384470, "len", lambda: len), _n_(384471, "anagrams", lambda: anagrams)) >=1:
                _l_(384481)

                _c_(384479, _n_(384473, "print", lambda: print), _c_(384478, _a_(384474, ' ', "join"), _c_(384477, _n_(384475, "sorted", lambda: sorted), _n_(384476, "anagrams", lambda: anagrams))))
                _l_(384480)
        _c_(384484, _n_(384483, "print", lambda: print))
        _l_(384485)
_c_(384489, _n_(384488, "main", lambda: main))
_l_(384490)