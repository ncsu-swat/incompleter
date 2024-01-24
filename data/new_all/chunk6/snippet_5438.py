# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51439242/python-3-7-got-an-unexpected-typeerror-from-a-user-defined-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
xs = {'x': 1, 'y': 2, 'z': 0}
_l_(347904)
ys = {'a': 3, 'b': 4, 'c': 5}
_l_(347905)
def print_vector(x, y, z):
    _l_(347912)

    _c_(347910, _n_(347906, "print", lambda: print), f'<{_n_(347907, "x", lambda: x)}, {_n_(347908, "y", lambda: y)}, {_n_(347909, "z", lambda: z)}>')
    _l_(347911)

_c_(347915, _n_(347913, 'print_vector', lambda: print_vector), **_n_(347914, 'xs', lambda: xs)) # <1, 2, 0>
_l_(347916) # <1, 2, 0>
_c_(347919, _n_(347917, 'print_vector', lambda: print_vector), **_n_(347918, 'ys', lambda: ys)) # TypeError: print_vector() got an unexpected keyword argument 'a'
_l_(347920) # TypeError: print_vector() got an unexpected keyword argument 'a'