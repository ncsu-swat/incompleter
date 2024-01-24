# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71376220/typeerror-cannot-unpack-non-iterable-float-object-in-centered-average-algorithm
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def calc_centered_average(numbers):
    _l_(543094)

    sorted_list = _c_(543085, _n_(543083, "sorted", lambda: sorted), _n_(543084, "numbers", lambda: numbers))
    _l_(543086)
    aux = _c_(543089, _n_(543087, "sum", lambda: sum), _n_(543088, "sorted_list", lambda: sorted_list)[1:-1])/(_c_(543092, _n_(543090, "len", lambda: len), _n_(543091, "numbers", lambda: numbers))-2)
    _l_(543093)
    return aux


numbers = [1, 4, 5, 6, 100]
_l_(543095)
sublist, cavg = _c_(543098, _n_(543096, "calc_centered_average", lambda: calc_centered_average), _n_(543097, "numbers", lambda: numbers))
_l_(543099)
_c_(543104, _n_(543100, "print", lambda: print), f"The centered average of {_n_(543101, 'numbers', lambda: numbers)} is {_n_(543102, 'cavg', lambda: cavg)} (based on {_n_(543103, 'sublist', lambda: sublist)}).")
_l_(543105)