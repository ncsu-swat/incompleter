# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51439242/python-3-7-got-an-unexpected-typeerror-from-a-user-defined-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
xs = {'x': 1, 'y': 2, 'z': 0}
_l_(452986)
ys = {'a': 3, 'b': 4, 'c': 5}
_l_(452987)
def print_vector(x, y, z):
    _l_(452994)

    _c_(452992, _n_(452988, "print", lambda: print), f'<{_n_(452989, "x", lambda: x)}, {_n_(452990, "y", lambda: y)}, {_n_(452991, "z", lambda: z)}>')
    _l_(452993)

_c_(452997, _n_(452995, 'print_vector', lambda: print_vector), **_n_(452996, 'xs', lambda: xs)) # <1, 2, 0>
_l_(452998) # <1, 2, 0>
_c_(453001, _n_(452999, 'print_vector', lambda: print_vector), **_n_(453000, 'ys', lambda: ys)) # TypeError: print_vector() got an unexpected keyword argument 'a'
_l_(453002) # TypeError: print_vector() got an unexpected keyword argument 'a'