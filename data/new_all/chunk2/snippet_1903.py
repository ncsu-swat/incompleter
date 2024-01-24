# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40829486/extracting-the-longest-subsequence-from-a-list-cant-figure-out-the-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def subSequence(sequence):
    _l_(435069)


    newSequence = [0]
    _l_(434995)
    longest = [0]
    _l_(434996)

    for x in _c_(435001, _n_(434997, "range", lambda: range), 0,_c_(435000, _n_(434998, "len", lambda: len), _n_(434999, "sequence", lambda: sequence))):
        _l_(435066)

        _c_(435006, _n_(435002, "print", lambda: print), "x is " +_c_(435005, _n_(435003, "str", lambda: str), _n_(435004, "x", lambda: x))+"\n")
        _l_(435007)
        if _n_(435008, "sequence", lambda: sequence)[_n_(435009, "x", lambda: x)] == _n_(435010, "sequence", lambda: sequence)[0]:
            _l_(435065)

            _c_(435015, _a_(435012, _n_(435011, "newSequence", lambda: newSequence), "append"), _n_(435013, "sequence", lambda: sequence)[_n_(435014, "x", lambda: x)])
            _l_(435016)

        elif _n_(435017, "sequence", lambda: sequence)[_n_(435018, "x", lambda: x)] > _n_(435019, "sequence", lambda: sequence)[_n_(435020, "x", lambda: x)-1]:
            _l_(435064)

            _c_(435026, _n_(435021, "print", lambda: print), "sequence[x] = " +_c_(435025, _n_(435022, "str", lambda: str), _n_(435023, "sequence", lambda: sequence)[_n_(435024, "x", lambda: x)]))
            _l_(435027)
            _c_(435033, _n_(435028, "print", lambda: print), "sequence[x-1] = " +_c_(435032, _n_(435029, "str", lambda: str), _n_(435030, "sequence", lambda: sequence)[_n_(435031, "x", lambda: x)-1]))
            _l_(435034)
            _c_(435039, _a_(435036, _n_(435035, "newSequence", lambda: newSequence), "append"), _n_(435037, "sequence", lambda: sequence)[_n_(435038, "x", lambda: x)])
            _l_(435040)

        else:
            if _n_(435041, "longest", lambda: longest) <= _n_(435042, "newSequence", lambda: newSequence):
                _l_(435063)

                del longest[:]
                _l_(435043)
                _c_(435047, _a_(435045, _n_(435044, "longest", lambda: longest), "append"), _n_(435046, "newSequence", lambda: newSequence)[:])
                _l_(435048)
                _c_(435053, _n_(435049, "print", lambda: print), "longest = "+_c_(435052, _n_(435050, "str", lambda: str), _n_(435051, "longest", lambda: longest)))
                _l_(435054)
                del newSequence[:]
                _l_(435055)
                _c_(435060, _a_(435057, _n_(435056, "newSequence", lambda: newSequence), "append"), _n_(435058, "sequence", lambda: sequence)[_n_(435059, "x", lambda: x)])
                _l_(435061)
            else:
                del newSequence[:]
                _l_(435062)
    aux = _n_(435067, "newSequence", lambda: newSequence)
    _l_(435068)

    return aux

mySequence = [1,2,3,2,5,6,7,2]
_l_(435070)
_c_(435075, _n_(435071, "print", lambda: print), _c_(435074, _n_(435072, "subSequence", lambda: subSequence), _n_(435073, "mySequence", lambda: mySequence)))
_l_(435076)