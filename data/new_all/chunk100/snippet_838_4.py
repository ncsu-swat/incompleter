# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections as ct
    _l_(83768)

except ImportError:
    pass

def merge_dictionaries(color1, color2):
    _l_(83771)

    aux = _n_(83769, "merged_dict", lambda: merged_dict)
    _l_(83770)
    return aux
color1 = {'R': 'Red', 'B': 'Black', 'P': 'Pink'}
_l_(83772)
color2 = {'G': 'Green', 'W': 'White'}
_l_(83773)
_c_(83775, _n_(83774, "print", lambda: print), 'Original dictionaries:')
_l_(83776)
_c_(83780, _n_(83777, "print", lambda: print), _n_(83778, "color1", lambda: color1), ' ', _n_(83779, "color2", lambda: color2))
_l_(83781)
_c_(83783, _n_(83782, "print", lambda: print), '\nMerged dictionary:')
_l_(83784)
_c_(83790, _n_(83785, "print", lambda: print), _c_(83789, _n_(83786, "merge_dictionaries", lambda: merge_dictionaries), _n_(83787, "color1", lambda: color1), _n_(83788, "color2", lambda: color2)))
_l_(83791)

def merge_dictionaries(color1, color2, color3):
    _l_(83803)

    merged_dict = _c_(83799, _n_(83792, "dict", lambda: dict), _c_(83798, _a_(83794, _n_(83793, "ct", lambda: ct), "ChainMap"), {}, _n_(83795, "color1", lambda: color1), _n_(83796, "color2", lambda: color2), _n_(83797, "color3", lambda: color3)))
    _l_(83800)
    aux = _n_(83801, "merged_dict", lambda: merged_dict)
    _l_(83802)
    return aux
color1 = {'R': 'Red', 'B': 'Black', 'P': 'Pink'}
_l_(83804)
color2 = {'G': 'Green', 'W': 'White'}
_l_(83805)
color3 = {'O': 'Orange', 'W': 'White', 'B': 'Black'}
_l_(83806)
_c_(83808, _n_(83807, "print", lambda: print), '\nOriginal dictionaries:')
_l_(83809)
_c_(83814, _n_(83810, "print", lambda: print), _n_(83811, "color1", lambda: color1), ' ', _n_(83812, "color2", lambda: color2), _n_(83813, "color3", lambda: color3))
_l_(83815)
_c_(83817, _n_(83816, "print", lambda: print), '\nMerged dictionary:')
_l_(83818)
_c_(83825, _n_(83819, "print", lambda: print), _c_(83824, _n_(83820, "merge_dictionaries", lambda: merge_dictionaries), _n_(83821, "color1", lambda: color1), _n_(83822, "color2", lambda: color2), _n_(83823, "color3", lambda: color3)))
_l_(83826)