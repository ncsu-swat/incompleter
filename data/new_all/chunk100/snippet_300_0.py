# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import chain
    _l_(25565)

except ImportError:
    pass

def sum_of_digits(nums):
    _l_(25578)

    aux = _c_(25576, _n_(25566, "sum", lambda: sum), (_c_(25569, _n_(25567, "int", lambda: int), _n_(25568, "y", lambda: y)) for y in _c_(25575, _n_(25570, "chain", lambda: chain), *[_c_(25573, _n_(25571, "str", lambda: str), _n_(25572, "x", lambda: x)) for x in _n_(25574, "nums", lambda: nums)])))
    _l_(25577)
    return aux
_c_(25580, _n_(25579, "print", lambda: print), 'Original tuple: ')
_l_(25581)
_c_(25584, _n_(25582, "print", lambda: print), _n_(25583, "nums", lambda: nums))
_l_(25585)
_c_(25587, _n_(25586, "print", lambda: print), 'Sum of digits of each number of the said list of integers:')
_l_(25588)
_c_(25593, _n_(25589, "print", lambda: print), _c_(25592, _n_(25590, "sum_of_digits", lambda: sum_of_digits), _n_(25591, "nums", lambda: nums)))
_l_(25594)
nums = [10, 20, 4, 5, 70]
_l_(25595)
_c_(25597, _n_(25596, "print", lambda: print), '\nOriginal tuple: ')
_l_(25598)
_c_(25601, _n_(25599, "print", lambda: print), _n_(25600, "nums", lambda: nums))
_l_(25602)
_c_(25604, _n_(25603, "print", lambda: print), 'Sum of digits of each number of the said list of integers:')
_l_(25605)
_c_(25610, _n_(25606, "print", lambda: print), _c_(25609, _n_(25607, "sum_of_digits", lambda: sum_of_digits), _n_(25608, "nums", lambda: nums)))
_l_(25611)