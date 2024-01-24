# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51439242/python-3-7-got-an-unexpected-typeerror-from-a-user-defined-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
xs = {'x': 1, 'y': 2, 'z': 0}
_l_(374949)
ys = {'a': 3, 'b': 4, 'c': 5}
_l_(374950)
def print_vector(x, y, z):
    _l_(374957)

    _c_(374955, _n_(374951, "print", lambda: print), f'<{_n_(374952, "x", lambda: x)}, {_n_(374953, "y", lambda: y)}, {_n_(374954, "z", lambda: z)}>')
    _l_(374956)

_c_(374960, _n_(374958, 'print_vector', lambda: print_vector), **_n_(374959, 'xs', lambda: xs)) # <1, 2, 0>
_l_(374961) # <1, 2, 0>
_c_(374964, _n_(374962, 'print_vector', lambda: print_vector), **_n_(374963, 'ys', lambda: ys)) # TypeError: print_vector() got an unexpected keyword argument 'a'
_l_(374965) # TypeError: print_vector() got an unexpected keyword argument 'a'