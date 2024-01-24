# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/18282148/why-does-my-code-produce-typeerror-nonetype-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def merge( s1, s2):
    _l_(399030)

    if _c_(398994, _n_(398992, "len", lambda: len), _n_(398993, "s1", lambda: s1)) == 0:
        _l_(398997)

        aux = _n_(398995, "s2", lambda: s2)[:]
        _l_(398996)
        return aux
    if _c_(399000, _n_(398998, "len", lambda: len), _n_(398999, "s2", lambda: s2)) == 0:
        _l_(399003)

        aux = _n_(399001, "s1", lambda: s1)[:]
        _l_(399002)
        return aux
    minElm = []
    _l_(399004)
    if _n_(399005, "s1", lambda: s1)[0] <= _n_(399006, "s2", lambda: s2)[0]:
        _l_(399021)

        _c_(399012, _a_(399008, _n_(399007, "minElm", lambda: minElm), "append"), _c_(399011, _a_(399010, _n_(399009, "s1", lambda: s1), "pop"), 0) )
        _l_(399013)
    else:
        _c_(399019, _a_(399015, _n_(399014, "minElm", lambda: minElm), "append"), _c_(399018, _a_(399017, _n_(399016, "s2", lambda: s2), "pop"), 0) )
        _l_(399020)
    aux = _c_(399028, _a_(399023, _n_(399022, "minElm", lambda: minElm), "extend"), _c_(399027, _n_(399024, "merge", lambda: merge), _n_(399025, "s1", lambda: s1)[:], _n_(399026, "s2", lambda: s2)[:] ))
    _l_(399029)
    return aux

list1 = [1,3,5,7,9]
_l_(399031)
list2 = [2,4,6,8]
_l_(399032)

merged = _c_(399036, _n_(399033, "merge", lambda: merge), _n_(399034, "list1", lambda: list1)[:], _n_(399035, "list2", lambda: list2)[:] )
_l_(399037)
_c_(399040, _n_(399038, "print", lambda: print), _n_(399039, "merged", lambda: merged))
_l_(399041)