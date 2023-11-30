# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def maybeMakeNumber(s):
    _l_(1541571)

    """Returns a string 's' into a integer if possible, a float if needed or
    returns it as is."""

    # handle None, "", 0
    if not _n_(1541549, "s", lambda: s):
        _l_(1541552)

        aux = _n_(1541550, "s", lambda: s)
        _l_(1541551)
        return aux
    try:
        _l_(1541570)

        f = _c_(1541555, _n_(1541553, "float", lambda: float), _n_(1541554, "s", lambda: s))
        _l_(1541556)
        i = _c_(1541559, _n_(1541557, "int", lambda: int), _n_(1541558, "f", lambda: f))
        _l_(1541560)
        aux = _n_(1541561, "i", lambda: i) if _n_(1541562, "f", lambda: f) == _n_(1541563, "i", lambda: i) else _n_(1541564, "f", lambda: f)
        _l_(1541565)
        return aux
    except _n_(1541566, "ValueError", lambda: ValueError):
        _l_(1541569)

        aux = _n_(1541567, "s", lambda: s)
        _l_(1541568)
        return aux

data = ["unkind", "data", "42", 98, "47.11", "of mixed", "types"]
_l_(1541572)

converted = _c_(1541578, _n_(1541573, "list", lambda: list), _c_(1541577, _n_(1541574, "map", lambda: map), _n_(1541575, "maybeMakeNumber", lambda: maybeMakeNumber), _n_(1541576, "data", lambda: data)))
_l_(1541579)
_c_(1541582, _n_(1541580, "print", lambda: print), _n_(1541581, "converted", lambda: converted))
_l_(1541583)

['unkind', 'data', 42, 98, 47.11, 'of mixed', 'types']
_l_(1541584)
try:
    from collections.abc import Iterable, Mapping
    _l_(1541586)

except ImportError:
    pass

def convertEr(iterab):
    _l_(1541616)

    """Tries to convert an iterable to list of floats, ints or the original thing
    from the iterable. Converts any iterable (tuple,set, ...) to itself in output.
    Does not work for Mappings  - you would need to check abc.Mapping and handle 
    things like {1:42, "1":84} when converting them - so they come out as is."""

    if _c_(1541590, _n_(1541587, "isinstance", lambda: isinstance), _n_(1541588, "iterab", lambda: iterab), _n_(1541589, "str", lambda: str)):
        _l_(1541595)

        aux = _c_(1541593, _n_(1541591, "maybeMakeNumber", lambda: maybeMakeNumber), _n_(1541592, "iterab", lambda: iterab))
        _l_(1541594)
        return aux

    if _c_(1541599, _n_(1541596, "isinstance", lambda: isinstance), _n_(1541597, "iterab", lambda: iterab), _n_(1541598, "Mapping", lambda: Mapping)):
        _l_(1541602)

        aux = _n_(1541600, "iterab", lambda: iterab)
        _l_(1541601)
        return aux

    if _c_(1541606, _n_(1541603, "isinstance", lambda: isinstance), _n_(1541604, "iterab", lambda: iterab), _n_(1541605, "Iterable", lambda: Iterable)):
        _l_(1541615)

        aux = _c_(1541613, _a_(1541608, _n_(1541607, "iterab", lambda: iterab), "__class__"), (_c_(1541611, _n_(1541609, "convertEr", lambda: convertEr), _n_(1541610, "p", lambda: p)) for p in _n_(1541612, "iterab", lambda: iterab)))
        _l_(1541614)
        return aux


data = ["unkind", {1: 3,"1":42}, "data", "42", 98, "47.11", "of mixed", 
        ("0", "8", {"15", "things"}, "3.141"), "types"]
_l_(1541617)

converted = _c_(1541620, _n_(1541618, "convertEr", lambda: convertEr), _n_(1541619, "data", lambda: data))
_l_(1541621)
_c_(1541624, _n_(1541622, "print", lambda: print), _n_(1541623, "converted", lambda: converted))
_l_(1541625)

['unkind', {1: 3, '1': 42}, 'data', 42, 98, 47.11, 'of mixed', 
 (0, 8, {'things', 15}, 3.141), 'types'] # sets are unordered, hence diffrent order
_l_(1541626) # sets are unordered, hence diffrent order

