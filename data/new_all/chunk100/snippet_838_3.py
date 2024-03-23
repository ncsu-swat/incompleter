# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections as ct
    _l_(83701)

except ImportError:
    pass

def merge_dictionaries(color1, color2):
    _l_(83712)

    merged_dict = _c_(83708, _n_(83702, "dict", lambda: dict), _c_(83707, _a_(83704, _n_(83703, "ct", lambda: ct), "ChainMap"), {}, _n_(83705, "color1", lambda: color1), _n_(83706, "color2", lambda: color2)))
    _l_(83709)
    aux = _n_(83710, "merged_dict", lambda: merged_dict)
    _l_(83711)
    return aux
color2 = {'G': 'Green', 'W': 'White'}
_l_(83713)
_c_(83715, _n_(83714, "print", lambda: print), 'Original dictionaries:')
_l_(83716)
_c_(83720, _n_(83717, "print", lambda: print), _n_(83718, "color1", lambda: color1), ' ', _n_(83719, "color2", lambda: color2))
_l_(83721)
_c_(83723, _n_(83722, "print", lambda: print), '\nMerged dictionary:')
_l_(83724)
_c_(83730, _n_(83725, "print", lambda: print), _c_(83729, _n_(83726, "merge_dictionaries", lambda: merge_dictionaries), _n_(83727, "color1", lambda: color1), _n_(83728, "color2", lambda: color2)))
_l_(83731)

def merge_dictionaries(color1, color2, color3):
    _l_(83743)

    merged_dict = _c_(83739, _n_(83732, "dict", lambda: dict), _c_(83738, _a_(83734, _n_(83733, "ct", lambda: ct), "ChainMap"), {}, _n_(83735, "color1", lambda: color1), _n_(83736, "color2", lambda: color2), _n_(83737, "color3", lambda: color3)))
    _l_(83740)
    aux = _n_(83741, "merged_dict", lambda: merged_dict)
    _l_(83742)
    return aux
color1 = {'R': 'Red', 'B': 'Black', 'P': 'Pink'}
_l_(83744)
color2 = {'G': 'Green', 'W': 'White'}
_l_(83745)
color3 = {'O': 'Orange', 'W': 'White', 'B': 'Black'}
_l_(83746)
_c_(83748, _n_(83747, "print", lambda: print), '\nOriginal dictionaries:')
_l_(83749)
_c_(83754, _n_(83750, "print", lambda: print), _n_(83751, "color1", lambda: color1), ' ', _n_(83752, "color2", lambda: color2), _n_(83753, "color3", lambda: color3))
_l_(83755)
_c_(83757, _n_(83756, "print", lambda: print), '\nMerged dictionary:')
_l_(83758)
_c_(83765, _n_(83759, "print", lambda: print), _c_(83764, _n_(83760, "merge_dictionaries", lambda: merge_dictionaries), _n_(83761, "color1", lambda: color1), _n_(83762, "color2", lambda: color2), _n_(83763, "color3", lambda: color3)))
_l_(83766)