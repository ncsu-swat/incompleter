# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections as ct
    _l_(83567)

except ImportError:
    pass

def merge_dictionaries(color1, color2):
    _l_(83578)

    merged_dict = _c_(83574, _n_(83568, "dict", lambda: dict), _c_(83573, _a_(83570, _n_(83569, "ct", lambda: ct), "ChainMap"), {}, _n_(83571, "color1", lambda: color1), _n_(83572, "color2", lambda: color2)))
    _l_(83575)
    aux = _n_(83576, "merged_dict", lambda: merged_dict)
    _l_(83577)
    return aux
color1 = {'R': 'Red', 'B': 'Black', 'P': 'Pink'}
_l_(83579)
color2 = {'G': 'Green', 'W': 'White'}
_l_(83580)
_c_(83582, _n_(83581, "print", lambda: print), 'Original dictionaries:')
_l_(83583)
_c_(83587, _n_(83584, "print", lambda: print), _n_(83585, "color1", lambda: color1), ' ', _n_(83586, "color2", lambda: color2))
_l_(83588)
_c_(83590, _n_(83589, "print", lambda: print), '\nMerged dictionary:')
_l_(83591)
_c_(83597, _n_(83592, "print", lambda: print), _c_(83596, _n_(83593, "merge_dictionaries", lambda: merge_dictionaries), _n_(83594, "color1", lambda: color1), _n_(83595, "color2", lambda: color2)))
_l_(83598)

def merge_dictionaries(color1, color2, color3):
    _l_(83610)

    merged_dict = _c_(83606, _n_(83599, "dict", lambda: dict), _c_(83605, _a_(83601, _n_(83600, "ct", lambda: ct), "ChainMap"), {}, _n_(83602, "color1", lambda: color1), _n_(83603, "color2", lambda: color2), _n_(83604, "color3", lambda: color3)))
    _l_(83607)
    aux = _n_(83608, "merged_dict", lambda: merged_dict)
    _l_(83609)
    return aux
color1 = {'R': 'Red', 'B': 'Black', 'P': 'Pink'}
_l_(83611)
color3 = {'O': 'Orange', 'W': 'White', 'B': 'Black'}
_l_(83612)
_c_(83614, _n_(83613, "print", lambda: print), '\nOriginal dictionaries:')
_l_(83615)
_c_(83620, _n_(83616, "print", lambda: print), _n_(83617, "color1", lambda: color1), ' ', _n_(83618, "color2", lambda: color2), _n_(83619, "color3", lambda: color3))
_l_(83621)
_c_(83623, _n_(83622, "print", lambda: print), '\nMerged dictionary:')
_l_(83624)
_c_(83631, _n_(83625, "print", lambda: print), _c_(83630, _n_(83626, "merge_dictionaries", lambda: merge_dictionaries), _n_(83627, "color1", lambda: color1), _n_(83628, "color2", lambda: color2), _n_(83629, "color3", lambda: color3)))
_l_(83632)