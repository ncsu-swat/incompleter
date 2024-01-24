# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59220623/my-cached-function-throws-typeerror-decorated-with-lru-cache
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(574231, _a_(574230, _n_(574229, "functools", lambda: functools), "lru_cache"), maxsize=None)
def flat_map(map_: _n_(574232, "Dict", lambda: Dict)[_n_(574233, "str", lambda: str), _n_(574234, "List", lambda: List)[_n_(574235, "str", lambda: str)]], start: _n_(574236, "str", lambda: str)) -> _n_(574237, "Dict", lambda: Dict)[_n_(574238, "str", lambda: str), _n_(574239, "List", lambda: List)[_n_(574240, "str", lambda: str)]]:
    _l_(574258)

    if _n_(574241, "start", lambda: start) not in _n_(574242, "map_", lambda: map_):
        _l_(574244)

        aux = []
        _l_(574243)
        return aux
    stars = _n_(574245, "map_", lambda: map_)[_n_(574246, "start", lambda: start)] + [_n_(574247, "s", lambda: s) for star in _n_(574248, "map_", lambda: map_)[_n_(574249, "start", lambda: start)] for s in _c_(574252, _n_(574250, "flat_map", lambda: flat_map), _n_(574251, "star", lambda: star))]
    _l_(574253)
    aux = {_n_(574254, "star", lambda: star): _n_(574255, "stars", lambda: stars) for star in _n_(574256, "starmap", lambda: starmap)}
    _l_(574257)
    return aux