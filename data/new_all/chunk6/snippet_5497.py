# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37398907/for-x-in-l-for-each-item-at-this-level-typeerror-int-object-is-not-iterabl
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sumtree(L):
    _l_(375029)

    tot = 0
    _l_(375013)
    for x in _n_(375014, "L", lambda: L):
        _l_(375026)

        if not _c_(375018, _n_(375015, "isinstance", lambda: isinstance), _n_(375016, "x", lambda: x),_n_(375017, "list", lambda: list)):
            _l_(375021)

            tot += _n_(375019, "x", lambda: x)  # Add numbers directly
            _l_(375020)  # Add numbers directly
    else:
       tot += _c_(375024, _n_(375022, "sumtree", lambda: sumtree), _n_(375023, "x", lambda: x))  # Recur for sublists
       _l_(375025)  # Recur for sublists
    aux = _n_(375027, "tot", lambda: tot)
    _l_(375028)
    return aux

l1 = [1, 2, 3, 4, [23, 33, [22, 22], 12, [12, 11]]]
_l_(375030)
_c_(375035, _n_(375031, "print", lambda: print), _c_(375034, _n_(375032, "sumtree", lambda: sumtree), _n_(375033, "l1", lambda: l1)))
_l_(375036)