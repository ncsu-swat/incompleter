# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import copy
    _l_(107466)

except ImportError:
    pass
nums_x = {'a': 1, 'b': 2, 'cc': {'c': 3}}
_l_(107467)
_c_(107470, _n_(107468, "print", lambda: print), 'Original dictionary: ', _n_(107469, "nums_x", lambda: nums_x))
_l_(107471)
nums_y = _c_(107475, _a_(107473, _n_(107472, "copy", lambda: copy), "deepcopy"), _n_(107474, "nums_x", lambda: nums_x))
_l_(107476)
_c_(107478, _n_(107477, "print", lambda: print), '\nDeep copy of the said list:')
_l_(107479)
_c_(107482, _n_(107480, "print", lambda: print), _n_(107481, "nums_y", lambda: nums_y))
_l_(107483)
_c_(107485, _n_(107484, "print", lambda: print), '\nChange the value of an element of the original dictionary:')
_l_(107486)
_n_(107487, "nums_x", lambda: nums_x)['cc']['c'] = 10
_l_(107488)
_c_(107491, _n_(107489, "print", lambda: print), _n_(107490, "nums_x", lambda: nums_x))
_l_(107492)
_c_(107494, _n_(107493, "print", lambda: print), '\nSecond dictionary (Deep copy):')
_l_(107495)
_c_(107498, _n_(107496, "print", lambda: print), _n_(107497, "nums_y", lambda: nums_y))
_l_(107499)
nums_copy = _c_(107503, _a_(107501, _n_(107500, "copy", lambda: copy), "deepcopy"), _n_(107502, "nums", lambda: nums))
_l_(107504)
_c_(107506, _n_(107505, "print", lambda: print), '\nOriginal dictionary :')
_l_(107507)
_c_(107510, _n_(107508, "print", lambda: print), _n_(107509, "nums", lambda: nums))
_l_(107511)
_c_(107513, _n_(107512, "print", lambda: print), '\nDeep copy of the said list:')
_l_(107514)
_c_(107517, _n_(107515, "print", lambda: print), _n_(107516, "nums_copy", lambda: nums_copy))
_l_(107518)
_c_(107520, _n_(107519, "print", lambda: print), '\nChange the value of an element of the original dictionary:')
_l_(107521)
_n_(107522, "nums", lambda: nums)['zz']['z'] = 10
_l_(107523)
_c_(107525, _n_(107524, "print", lambda: print), '\nFirst dictionary:')
_l_(107526)
_c_(107529, _n_(107527, "print", lambda: print), _n_(107528, "nums", lambda: nums))
_l_(107530)
_c_(107532, _n_(107531, "print", lambda: print), '\nSecond dictionary (Deep copy):')
_l_(107533)
_c_(107536, _n_(107534, "print", lambda: print), _n_(107535, "nums_copy", lambda: nums_copy))
_l_(107537)