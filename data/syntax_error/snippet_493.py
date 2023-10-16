# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/452104/is-it-worth-using-pythons-re-compile
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def match(pattern, string, flags=0):
    _l_(1543932)

    aux = _c_(1543930, _a_(1543928, _c_(1543927, _n_(1543924, "_compile", lambda: _compile), _n_(1543925, "pattern", lambda: pattern), _n_(1543926, "flags", lambda: flags)), "match"), _n_(1543929, "string", lambda: string))
    _l_(1543931)
    return aux

def _compile(*key):
    _l_(1543961)


    # Does cache check at top of function
    cachekey = (_c_(1543935, _n_(1543933, "type", lambda: type), _n_(1543934, "key", lambda: key)[0]),) + _n_(1543936, "key", lambda: key)
    _l_(1543937)
    p = _c_(1543941, _a_(1543939, _n_(1543938, "_cache", lambda: _cache), "get"), _n_(1543940, "cachekey", lambda: cachekey))
    _l_(1543942)
    if _n_(1543943, "p", lambda: p) is not None:
        _l_(1543945)

return _n_(1543944, "p", lambda: p)
    # ...
    # Does actual compilation on cache miss
    # ...

    # Caches compiled regex
    if _c_(1543948, _n_(1543946, "len", lambda: len), _n_(1543947, "_cache", lambda: _cache)) >= _n_(1543949, "_MAXCACHE", lambda: _MAXCACHE):
        _l_(1543954)

        _c_(1543952, _a_(1543951, _n_(1543950, "_cache", lambda: _cache), "clear"))
        _l_(1543953)
    _n_(1543955, "_cache", lambda: _cache)[_n_(1543956, "cachekey", lambda: cachekey)] = _n_(1543957, "p", lambda: p)
    _l_(1543958)
    aux = _n_(1543959, "p", lambda: p)
    _l_(1543960)
    return aux

