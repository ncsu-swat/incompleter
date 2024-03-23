# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections as ct
    _l_(83828)

except ImportError:
    pass

def merge_dictionaries(color1, color2):
    _l_(83839)

    merged_dict = _c_(83835, _n_(83829, "dict", lambda: dict), _c_(83834, _a_(83831, _n_(83830, "ct", lambda: ct), "ChainMap"), {}, _n_(83832, "color1", lambda: color1), _n_(83833, "color2", lambda: color2)))
    _l_(83836)
    aux = _n_(83837, "merged_dict", lambda: merged_dict)
    _l_(83838)
    return aux
color1 = {'R': 'Red', 'B': 'Black', 'P': 'Pink'}
_l_(83840)
color2 = {'G': 'Green', 'W': 'White'}
_l_(83841)
_c_(83843, _n_(83842, "print", lambda: print), 'Original dictionaries:')
_l_(83844)
_c_(83848, _n_(83845, "print", lambda: print), _n_(83846, "color1", lambda: color1), ' ', _n_(83847, "color2", lambda: color2))
_l_(83849)
_c_(83851, _n_(83850, "print", lambda: print), '\nMerged dictionary:')
_l_(83852)
_c_(83858, _n_(83853, "print", lambda: print), _c_(83857, _n_(83854, "merge_dictionaries", lambda: merge_dictionaries), _n_(83855, "color1", lambda: color1), _n_(83856, "color2", lambda: color2)))
_l_(83859)

def merge_dictionaries(color1, color2, color3):
    _l_(83862)

    aux = _n_(83860, "merged_dict", lambda: merged_dict)
    _l_(83861)
    return aux
color1 = {'R': 'Red', 'B': 'Black', 'P': 'Pink'}
_l_(83863)
color2 = {'G': 'Green', 'W': 'White'}
_l_(83864)
color3 = {'O': 'Orange', 'W': 'White', 'B': 'Black'}
_l_(83865)
_c_(83867, _n_(83866, "print", lambda: print), '\nOriginal dictionaries:')
_l_(83868)
_c_(83873, _n_(83869, "print", lambda: print), _n_(83870, "color1", lambda: color1), ' ', _n_(83871, "color2", lambda: color2), _n_(83872, "color3", lambda: color3))
_l_(83874)
_c_(83876, _n_(83875, "print", lambda: print), '\nMerged dictionary:')
_l_(83877)
_c_(83884, _n_(83878, "print", lambda: print), _c_(83883, _n_(83879, "merge_dictionaries", lambda: merge_dictionaries), _n_(83880, "color1", lambda: color1), _n_(83881, "color2", lambda: color2), _n_(83882, "color3", lambda: color3)))
_l_(83885)