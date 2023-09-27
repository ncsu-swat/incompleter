# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5442910/how-to-use-multiprocessing-pool-map-with-multiple-arguments
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import multiprocessing as mp
    _l_(1540911)

except ImportError:
    pass

def foo(q, h, w):
    _l_(1540923)

    _c_(1540916, _a_(1540913, _n_(1540912, "q", lambda: q), "put"), _n_(1540914, "h", lambda: h) + ' ' + _n_(1540915, "w", lambda: w))
    _l_(1540917)
    _c_(1540921, _n_(1540918, "print", lambda: print), _n_(1540919, "h", lambda: h) + ' ' + _n_(1540920, "w", lambda: w))
    _l_(1540922)

if _n_(1540924, "__name__", lambda: __name__) == '__main__':
    _l_(1540953)

    ctx = _c_(1540927, _a_(1540926, _n_(1540925, "mp", lambda: mp), "get_context"), 'spawn')
    _l_(1540928)
    q = _c_(1540931, _a_(1540930, _n_(1540929, "ctx", lambda: ctx), "Queue"))
    _l_(1540932)
    p = _c_(1540937, _a_(1540934, _n_(1540933, "ctx", lambda: ctx), "Process"), target=_n_(1540935, "foo", lambda: foo), args=(_n_(1540936, "q", lambda: q),'hello', 'world'))
    _l_(1540938)
    _c_(1540941, _a_(1540940, _n_(1540939, "p", lambda: p), "start"))
    _l_(1540942)
    _c_(1540947, _n_(1540943, "print", lambda: print), _c_(1540946, _a_(1540945, _n_(1540944, "q", lambda: q), "get")))
    _l_(1540948)
    _c_(1540951, _a_(1540950, _n_(1540949, "p", lambda: p), "join"))
    _l_(1540952)

_c_(1540961, _a_(1540955, _n_(1540954, "pool", lambda: pool), "map"), _c_(1540959, _n_(1540956, "harvester", lambda: harvester), _n_(1540957, "text", lambda: text), _n_(1540958, "case", lambda: case)), _n_(1540960, "case", lambda: case), 1)
_l_(1540962)

_c_(1540970, _a_(1540964, _n_(1540963, "pool", lambda: pool), "apply_async"), _c_(1540968, _n_(1540965, "harvester", lambda: harvester), _n_(1540966, "text", lambda: text), _n_(1540967, "case", lambda: case)), _n_(1540969, "case", lambda: case), 1)
_l_(1540971)

