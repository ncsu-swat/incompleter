# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43671634/python-3-typeerror-string-indices-must-be-integers-conditional-statement
#function that accepts a string and calculates the number of upper case and lower case

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def case_count(str):
    _l_(474887)

    total_cap_cases = 0
    _l_(474863)
    total_low_cases = 0
    _l_(474864)
    for words in _n_(474865, "str", lambda: str):
        _l_(474878)

        if _c_(474869, _a_(474868, _n_(474866, "str", lambda: str)[_n_(474867, "words", lambda: words)], "isupper")):
            _l_(474877)

            total_cap_cases += 1
            _l_(474870)
        elif _c_(474873, _a_(474872, _n_(474871, "words", lambda: words), "islower")):
            _l_(474876)

            total_low_cases += 1
            _l_(474874)
        else:
            pass
            _l_(474875)

    _c_(474881, _n_(474879, "print", lambda: print), _n_(474880, "total_cap_cases", lambda: total_cap_cases))
    _l_(474882)
    _c_(474885, _n_(474883, "print", lambda: print), _n_(474884, "total_low_cases", lambda: total_low_cases))
    _l_(474886)


str = "How Many upper and LOWER case lettters are in THIS senTence?"
_l_(474888)
_c_(474891, _n_(474889, "case_count", lambda: case_count), _n_(474890, "str", lambda: str))
_l_(474892)