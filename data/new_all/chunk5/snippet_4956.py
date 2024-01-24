# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65448638/typeerror-unsupported-operand-types-for-nonetype-and-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def quicksort(array):
    _l_(659698)

    if _c_(659675, _n_(659673, "len", lambda: len), _n_(659674, "array", lambda: array)) < 2:
        _l_(659697)

        aux = "" 
        _l_(659676) 
        return aux 
    else:
        pivot = _n_(659677, "array", lambda: array)[0] #Recursive case
        _l_(659678) #Recursive case
        less = [_n_(659679, "i", lambda: i) for i in _n_(659680, "array", lambda: array)[1:] if _n_(659681, "i", lambda: i) <= _n_(659682, "pivot", lambda: pivot)] 
        _l_(659683) 
        greater = [_n_(659684, "i", lambda: i) for i in _n_(659685, "array", lambda: array)[1:] if _n_(659686, "i", lambda: i) > _n_(659687, "pivot", lambda: pivot)] 
        _l_(659688) 
        aux = _c_(659691, _n_(659689, "quicksort", lambda: quicksort), _n_(659690, "less", lambda: less)) + [_n_(659692, "pivot", lambda: pivot)] + _c_(659695, _n_(659693, "quicksort", lambda: quicksort), _n_(659694, "greater", lambda: greater))
        _l_(659696)
        return aux
_c_(659702, _n_(659699, "print", lambda: print), _c_(659701, _n_(659700, "quicksort", lambda: quicksort), [10, 5, 2, 3]))
_l_(659703)