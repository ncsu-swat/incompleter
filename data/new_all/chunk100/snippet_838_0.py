# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections as ct
    _l_(83500)

except ImportError:
    pass

def merge_dictionaries(color1, color2):
    _l_(83511)

    merged_dict = _c_(83507, _n_(83501, "dict", lambda: dict), _c_(83506, _a_(83503, _n_(83502, "ct", lambda: ct), "ChainMap"), {}, _n_(83504, "color1", lambda: color1), _n_(83505, "color2", lambda: color2)))
    _l_(83508)
    aux = _n_(83509, "merged_dict", lambda: merged_dict)
    _l_(83510)
    return aux
color1 = {'R': 'Red', 'B': 'Black', 'P': 'Pink'}
_l_(83512)
color2 = {'G': 'Green', 'W': 'White'}
_l_(83513)
_c_(83515, _n_(83514, "print", lambda: print), 'Original dictionaries:')
_l_(83516)
_c_(83520, _n_(83517, "print", lambda: print), _n_(83518, "color1", lambda: color1), ' ', _n_(83519, "color2", lambda: color2))
_l_(83521)
_c_(83523, _n_(83522, "print", lambda: print), '\nMerged dictionary:')
_l_(83524)
_c_(83530, _n_(83525, "print", lambda: print), _c_(83529, _n_(83526, "merge_dictionaries", lambda: merge_dictionaries), _n_(83527, "color1", lambda: color1), _n_(83528, "color2", lambda: color2)))
_l_(83531)

def merge_dictionaries(color1, color2, color3):
    _l_(83543)

    merged_dict = _c_(83539, _n_(83532, "dict", lambda: dict), _c_(83538, _a_(83534, _n_(83533, "ct", lambda: ct), "ChainMap"), {}, _n_(83535, "color1", lambda: color1), _n_(83536, "color2", lambda: color2), _n_(83537, "color3", lambda: color3)))
    _l_(83540)
    aux = _n_(83541, "merged_dict", lambda: merged_dict)
    _l_(83542)
    return aux
color2 = {'G': 'Green', 'W': 'White'}
_l_(83544)
color3 = {'O': 'Orange', 'W': 'White', 'B': 'Black'}
_l_(83545)
_c_(83547, _n_(83546, "print", lambda: print), '\nOriginal dictionaries:')
_l_(83548)
_c_(83553, _n_(83549, "print", lambda: print), _n_(83550, "color1", lambda: color1), ' ', _n_(83551, "color2", lambda: color2), _n_(83552, "color3", lambda: color3))
_l_(83554)
_c_(83556, _n_(83555, "print", lambda: print), '\nMerged dictionary:')
_l_(83557)
_c_(83564, _n_(83558, "print", lambda: print), _c_(83563, _n_(83559, "merge_dictionaries", lambda: merge_dictionaries), _n_(83560, "color1", lambda: color1), _n_(83561, "color2", lambda: color2), _n_(83562, "color3", lambda: color3)))
_l_(83565)