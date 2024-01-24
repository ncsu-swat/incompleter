# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59509507/formating-issue-with-list-of-integers-typeerror-not-all-arguments-converted-du
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sort_array(source_array):
    _l_(649973)

    result = _n_(649951, "source_array", lambda: source_array)[:]
    _l_(649952)
    odd = []
    _l_(649953)
    for i in _n_(649954, "result", lambda: result) :
        _l_(649970)

        if _n_(649955, "i", lambda: i) % 2 == 0 or _n_(649956, "i", lambda: i) == 0:
            _l_(649969)

            _c_(649959, _a_(649958, _n_(649957, "odd", lambda: odd), "append"), 'even_number')
            _l_(649960)
        else:
            _c_(649964, _a_(649962, _n_(649961, "odd", lambda: odd), "append"), _n_(649963, "i", lambda: i))
            _l_(649965)
            _n_(649966, "result", lambda: result)[_n_(649967, "i", lambda: i)] = 'odd'
            _l_(649968)
    aux = _n_(649971, "source_array", lambda: source_array)
    _l_(649972)

     # this is not a complete implementation we need to sort odd then replace it 
     # string 'even_number' kind off merge
    return aux
#checking the out put below
_c_(649977, _n_(649974, "print", lambda: print), _c_(649976, _n_(649975, "sort_array", lambda: sort_array), [5, 3, 2, 8, 1, 4]))
_l_(649978)
_c_(649982, _n_(649979, "print", lambda: print), _c_(649981, _n_(649980, "sort_array", lambda: sort_array), [5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4])
_l_(649983)