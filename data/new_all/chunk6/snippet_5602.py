# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65448638/typeerror-unsupported-operand-types-for-nonetype-and-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def quicksort(array):
    _l_(369465)

    if _c_(369442, _n_(369440, "len", lambda: len), _n_(369441, "array", lambda: array)) < 2:
        _l_(369464)

        aux = "" 
        _l_(369443) 
        return aux 
    else:
        pivot = _n_(369444, "array", lambda: array)[0] #Recursive case
        _l_(369445) #Recursive case
        less = [_n_(369446, "i", lambda: i) for i in _n_(369447, "array", lambda: array)[1:] if _n_(369448, "i", lambda: i) <= _n_(369449, "pivot", lambda: pivot)] 
        _l_(369450) 
        greater = [_n_(369451, "i", lambda: i) for i in _n_(369452, "array", lambda: array)[1:] if _n_(369453, "i", lambda: i) > _n_(369454, "pivot", lambda: pivot)] 
        _l_(369455) 
        aux = _c_(369458, _n_(369456, "quicksort", lambda: quicksort), _n_(369457, "less", lambda: less)) + [_n_(369459, "pivot", lambda: pivot)] + _c_(369462, _n_(369460, "quicksort", lambda: quicksort), _n_(369461, "greater", lambda: greater))
        _l_(369463)
        return aux
_c_(369469, _n_(369466, "print", lambda: print), _c_(369468, _n_(369467, "quicksort", lambda: quicksort), [10, 5, 2, 3]))
_l_(369470)