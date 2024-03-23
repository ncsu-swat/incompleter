# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections as ct
    _l_(83634)

except ImportError:
    pass

def merge_dictionaries(color1, color2):
    _l_(83645)

    merged_dict = _c_(83641, _n_(83635, "dict", lambda: dict), _c_(83640, _a_(83637, _n_(83636, "ct", lambda: ct), "ChainMap"), {}, _n_(83638, "color1", lambda: color1), _n_(83639, "color2", lambda: color2)))
    _l_(83642)
    aux = _n_(83643, "merged_dict", lambda: merged_dict)
    _l_(83644)
    return aux
color1 = {'R': 'Red', 'B': 'Black', 'P': 'Pink'}
_l_(83646)
_c_(83648, _n_(83647, "print", lambda: print), 'Original dictionaries:')
_l_(83649)
_c_(83653, _n_(83650, "print", lambda: print), _n_(83651, "color1", lambda: color1), ' ', _n_(83652, "color2", lambda: color2))
_l_(83654)
_c_(83656, _n_(83655, "print", lambda: print), '\nMerged dictionary:')
_l_(83657)
_c_(83663, _n_(83658, "print", lambda: print), _c_(83662, _n_(83659, "merge_dictionaries", lambda: merge_dictionaries), _n_(83660, "color1", lambda: color1), _n_(83661, "color2", lambda: color2)))
_l_(83664)

def merge_dictionaries(color1, color2, color3):
    _l_(83676)

    merged_dict = _c_(83672, _n_(83665, "dict", lambda: dict), _c_(83671, _a_(83667, _n_(83666, "ct", lambda: ct), "ChainMap"), {}, _n_(83668, "color1", lambda: color1), _n_(83669, "color2", lambda: color2), _n_(83670, "color3", lambda: color3)))
    _l_(83673)
    aux = _n_(83674, "merged_dict", lambda: merged_dict)
    _l_(83675)
    return aux
color1 = {'R': 'Red', 'B': 'Black', 'P': 'Pink'}
_l_(83677)
color2 = {'G': 'Green', 'W': 'White'}
_l_(83678)
color3 = {'O': 'Orange', 'W': 'White', 'B': 'Black'}
_l_(83679)
_c_(83681, _n_(83680, "print", lambda: print), '\nOriginal dictionaries:')
_l_(83682)
_c_(83687, _n_(83683, "print", lambda: print), _n_(83684, "color1", lambda: color1), ' ', _n_(83685, "color2", lambda: color2), _n_(83686, "color3", lambda: color3))
_l_(83688)
_c_(83690, _n_(83689, "print", lambda: print), '\nMerged dictionary:')
_l_(83691)
_c_(83698, _n_(83692, "print", lambda: print), _c_(83697, _n_(83693, "merge_dictionaries", lambda: merge_dictionaries), _n_(83694, "color1", lambda: color1), _n_(83695, "color2", lambda: color2), _n_(83696, "color3", lambda: color3)))
_l_(83699)