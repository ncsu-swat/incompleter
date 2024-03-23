# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections as ct
    _l_(83887)

except ImportError:
    pass

def merge_dictionaries(color1, color2):
    _l_(83898)

    merged_dict = _c_(83894, _n_(83888, "dict", lambda: dict), _c_(83893, _a_(83890, _n_(83889, "ct", lambda: ct), "ChainMap"), {}, _n_(83891, "color1", lambda: color1), _n_(83892, "color2", lambda: color2)))
    _l_(83895)
    aux = _n_(83896, "merged_dict", lambda: merged_dict)
    _l_(83897)
    return aux
color1 = {'R': 'Red', 'B': 'Black', 'P': 'Pink'}
_l_(83899)
color2 = {'G': 'Green', 'W': 'White'}
_l_(83900)
_c_(83902, _n_(83901, "print", lambda: print), 'Original dictionaries:')
_l_(83903)
_c_(83907, _n_(83904, "print", lambda: print), _n_(83905, "color1", lambda: color1), ' ', _n_(83906, "color2", lambda: color2))
_l_(83908)
_c_(83910, _n_(83909, "print", lambda: print), '\nMerged dictionary:')
_l_(83911)
_c_(83917, _n_(83912, "print", lambda: print), _c_(83916, _n_(83913, "merge_dictionaries", lambda: merge_dictionaries), _n_(83914, "color1", lambda: color1), _n_(83915, "color2", lambda: color2)))
_l_(83918)

def merge_dictionaries(color1, color2, color3):
    _l_(83930)

    merged_dict = _c_(83926, _n_(83919, "dict", lambda: dict), _c_(83925, _a_(83921, _n_(83920, "ct", lambda: ct), "ChainMap"), {}, _n_(83922, "color1", lambda: color1), _n_(83923, "color2", lambda: color2), _n_(83924, "color3", lambda: color3)))
    _l_(83927)
    aux = _n_(83928, "merged_dict", lambda: merged_dict)
    _l_(83929)
    return aux
color1 = {'R': 'Red', 'B': 'Black', 'P': 'Pink'}
_l_(83931)
color2 = {'G': 'Green', 'W': 'White'}
_l_(83932)
_c_(83934, _n_(83933, "print", lambda: print), '\nOriginal dictionaries:')
_l_(83935)
_c_(83940, _n_(83936, "print", lambda: print), _n_(83937, "color1", lambda: color1), ' ', _n_(83938, "color2", lambda: color2), _n_(83939, "color3", lambda: color3))
_l_(83941)
_c_(83943, _n_(83942, "print", lambda: print), '\nMerged dictionary:')
_l_(83944)
_c_(83951, _n_(83945, "print", lambda: print), _c_(83950, _n_(83946, "merge_dictionaries", lambda: merge_dictionaries), _n_(83947, "color1", lambda: color1), _n_(83948, "color2", lambda: color2), _n_(83949, "color3", lambda: color3)))
_l_(83952)