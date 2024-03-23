# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(33676)

except ImportError:
    pass
try:
    import os
    _l_(33678)

except ImportError:
    pass
_c_(33680, _n_(33679, "print", lambda: print), 'Select a random element from a list:')
_l_(33681)
elements = [1, 2, 3, 4, 5]
_l_(33682)
_c_(33688, _n_(33683, "print", lambda: print), _c_(33687, _a_(33685, _n_(33684, "random", lambda: random), "choice"), _n_(33686, "elements", lambda: elements)))
_l_(33689)
_c_(33695, _n_(33690, "print", lambda: print), _c_(33694, _a_(33692, _n_(33691, "random", lambda: random), "choice"), _n_(33693, "elements", lambda: elements)))
_l_(33696)
_c_(33702, _n_(33697, "print", lambda: print), _c_(33701, _a_(33699, _n_(33698, "random", lambda: random), "choice"), _n_(33700, "elements", lambda: elements)))
_l_(33703)
_c_(33705, _n_(33704, "print", lambda: print), '\nSelect a random element from a set:')
_l_(33706)
elements = _c_(33708, _n_(33707, "set", lambda: set), [1, 2, 3, 4, 5])
_l_(33709)
_c_(33717, _n_(33710, "print", lambda: print), _c_(33716, _a_(33712, _n_(33711, "random", lambda: random), "choice"), _c_(33715, _n_(33713, "tuple", lambda: tuple), _n_(33714, "elements", lambda: elements))))
_l_(33718)
_c_(33726, _n_(33719, "print", lambda: print), _c_(33725, _a_(33721, _n_(33720, "random", lambda: random), "choice"), _c_(33724, _n_(33722, "tuple", lambda: tuple), _n_(33723, "elements", lambda: elements))))
_l_(33727)
_c_(33735, _n_(33728, "print", lambda: print), _c_(33734, _a_(33730, _n_(33729, "random", lambda: random), "choice"), _c_(33733, _n_(33731, "tuple", lambda: tuple), _n_(33732, "elements", lambda: elements))))
_l_(33736)
_c_(33738, _n_(33737, "print", lambda: print), '\nSelect a random value from a dictionary:')
_l_(33739)
key = _c_(33745, _a_(33741, _n_(33740, "random", lambda: random), "choice"), _c_(33744, _n_(33742, "list", lambda: list), _n_(33743, "d", lambda: d)))
_l_(33746)
_c_(33750, _n_(33747, "print", lambda: print), _n_(33748, "d", lambda: d)[_n_(33749, "key", lambda: key)])
_l_(33751)
key = _c_(33757, _a_(33753, _n_(33752, "random", lambda: random), "choice"), _c_(33756, _n_(33754, "list", lambda: list), _n_(33755, "d", lambda: d)))
_l_(33758)
_c_(33762, _n_(33759, "print", lambda: print), _n_(33760, "d", lambda: d)[_n_(33761, "key", lambda: key)])
_l_(33763)
key = _c_(33769, _a_(33765, _n_(33764, "random", lambda: random), "choice"), _c_(33768, _n_(33766, "list", lambda: list), _n_(33767, "d", lambda: d)))
_l_(33770)
_c_(33774, _n_(33771, "print", lambda: print), _n_(33772, "d", lambda: d)[_n_(33773, "key", lambda: key)])
_l_(33775)
_c_(33777, _n_(33776, "print", lambda: print), '\nSelect a random file from a directory.:')
_l_(33778)
_c_(33786, _n_(33779, "print", lambda: print), _c_(33785, _a_(33781, _n_(33780, "random", lambda: random), "choice"), _c_(33784, _a_(33783, _n_(33782, "os", lambda: os), "listdir"), '/')))
_l_(33787)