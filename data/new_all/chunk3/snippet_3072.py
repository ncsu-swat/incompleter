# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49332661/typeerror-nonetype-selection-sort-on-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(551807)

except ImportError:
    pass

def find_smallest(arr):
    _l_(551828)

    """Return the index of the smallest value in an array"""
    smallest = _n_(551808, "arr", lambda: arr)[0]
    _l_(551809)
    smallest_index = 0
    _l_(551810)

    for i in _c_(551815, _n_(551811, "range", lambda: range), 1, _c_(551814, _n_(551812, "len", lambda: len), _n_(551813, "arr", lambda: arr))):
        _l_(551827)

        if _n_(551816, "arr", lambda: arr)[_n_(551817, "i", lambda: i)] < _n_(551818, "smallest", lambda: smallest):
            _l_(551824)

            smallest = _n_(551819, "arr", lambda: arr)[_n_(551820, "i", lambda: i)]
            _l_(551821)
            smallest_index = _n_(551822, "i", lambda: i)
            _l_(551823)
        aux = _n_(551825, "smallest_index", lambda: smallest_index)
        _l_(551826)
        return aux

def selection_sort(arr):
    _l_(551850)

    """sort an array by storing smallest value to new array 1 by 1"""
    new_array = []
    _l_(551829)
    for i in _c_(551834, _n_(551830, "range", lambda: range), _c_(551833, _n_(551831, "len", lambda: len), _n_(551832, "arr", lambda: arr))):
        _l_(551847)

        smallest = _c_(551837, _n_(551835, "find_smallest", lambda: find_smallest), _n_(551836, "arr", lambda: arr))
        _l_(551838)
        _c_(551845, _a_(551840, _n_(551839, "new_array", lambda: new_array), "append"), _c_(551844, _a_(551842, _n_(551841, "arr", lambda: arr), "pop"), _n_(551843, "smallest", lambda: smallest)))
        _l_(551846)
    aux = _n_(551848, "new_array", lambda: new_array)
    _l_(551849)
    return aux


my_array = []
_l_(551851)
for i in _c_(551853, _n_(551852, "range", lambda: range), 0, 11):
    _l_(551866)

    _c_(551859, _a_(551855, _n_(551854, "my_array", lambda: my_array), "append"), _c_(551858, _a_(551857, _n_(551856, "random", lambda: random), "randint"), 1, 101))
    _l_(551860)
    _c_(551864, _n_(551861, "print", lambda: print), _n_(551862, "my_array", lambda: my_array)[_n_(551863, "i", lambda: i)])
    _l_(551865)

sorted_array = _c_(551869, _n_(551867, "selection_sort", lambda: selection_sort), _n_(551868, "my_array", lambda: my_array))
_l_(551870)
for i in _c_(551875, _n_(551871, "range", lambda: range), _c_(551874, _n_(551872, "len", lambda: len), _n_(551873, "sorted_array", lambda: sorted_array))):
    _l_(551881)

    _c_(551879, _n_(551876, "print", lambda: print), _n_(551877, "sorted_array", lambda: sorted_array)[_n_(551878, "i", lambda: i)])
    _l_(551880)