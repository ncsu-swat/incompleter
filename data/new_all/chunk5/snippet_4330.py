# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59509507/formating-issue-with-list-of-integers-typeerror-not-all-arguments-converted-du
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sort_array(source_array):
    _l_(702774)

    result = _n_(702752, "source_array", lambda: source_array)[:]
    _l_(702753)
    odd = []
    _l_(702754)
    for i in _n_(702755, "result", lambda: result) :
        _l_(702771)

        if _n_(702756, "i", lambda: i) % 2 == 0 or _n_(702757, "i", lambda: i) == 0:
            _l_(702770)

            _c_(702760, _a_(702759, _n_(702758, "odd", lambda: odd), "append"), 'even_number')
            _l_(702761)
        else:
            _c_(702765, _a_(702763, _n_(702762, "odd", lambda: odd), "append"), _n_(702764, "i", lambda: i))
            _l_(702766)
            _n_(702767, "result", lambda: result)[_n_(702768, "i", lambda: i)] = 'odd'
            _l_(702769)
    aux = _n_(702772, "source_array", lambda: source_array)
    _l_(702773)

     # this is not a complete implementation we need to sort odd then replace it 
     # string 'even_number' kind off merge
    return aux
#checking the out put below
_c_(702778, _n_(702775, "print", lambda: print), _c_(702777, _n_(702776, "sort_array", lambda: sort_array), [5, 3, 2, 8, 1, 4]))
_l_(702779)
_c_(702783, _n_(702780, "print", lambda: print), _c_(702782, _n_(702781, "sort_array", lambda: sort_array), [5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4])
_l_(702784)