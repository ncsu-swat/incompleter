# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3013449/list-comprehension-vs-lambda-filter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
[_n_(61942, "x", lambda: x) for x in _n_(61943, "X", lambda: X) if _c_(61946, _n_(61944, "P", lambda: P), _n_(61945, "x", lambda: x))]
_l_(61947)

[_c_(61950, _n_(61948, "f", lambda: f), _n_(61949, "x", lambda: x)) for x in _n_(61951, "X", lambda: X) if _c_(61956, _n_(61952, "P", lambda: P), _c_(61955, _n_(61953, "f", lambda: f), _n_(61954, "x", lambda: x)))]
_l_(61957)

primes_cubed = [_n_(61958, "x", lambda: x)*_n_(61959, "x", lambda: x)*_n_(61960, "x", lambda: x) for x in _c_(61962, _n_(61961, "range", lambda: range), 1000) if _c_(61965, _n_(61963, "prime", lambda: prime), _n_(61964, "x", lambda: x))]
_l_(61966)

prime_cubes = [_n_(61967, "x", lambda: x)*_n_(61968, "x", lambda: x)*_n_(61969, "x", lambda: x) for x in _c_(61971, _n_(61970, "range", lambda: range), 1000) if _c_(61976, _n_(61972, "prime", lambda: prime), _n_(61973, "x", lambda: x)*_n_(61974, "x", lambda: x)*_n_(61975, "x", lambda: x))]
_l_(61977)

prime_cubes = _c_(61985, _n_(61978, "filter", lambda: filter), _n_(61979, "prime", lambda: prime), [_n_(61980, "x", lambda: x)*_n_(61981, "x", lambda: x)*_n_(61982, "x", lambda: x) for x in _c_(61984, _n_(61983, "range", lambda: range), 1000)])
_l_(61986)

