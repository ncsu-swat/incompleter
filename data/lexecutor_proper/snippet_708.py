# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9786102/how-do-i-parallelize-a-simple-python-loop
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tqdm.contrib.concurrent import thread_map, process_map
    _l_(64413)

except ImportError:
    pass


def calc_stuff(num, multiplier):
    _l_(64424)

    try:
        import time
        _l_(64415)

    except ImportError:
        pass

    _c_(64418, _a_(64417, _n_(64416, "time", lambda: time), "sleep"), 1)
    _l_(64419)
    aux = _n_(64420, "num", lambda: num), _n_(64421, "num", lambda: num) * _n_(64422, "multiplier", lambda: multiplier)
    _l_(64423)

    return aux


if _n_(64425, "__name__", lambda: __name__) == "__main__":
    _l_(64445)


    # let's parallelize this for loop:
    # results = [calc_stuff(i, 2) for i in range(64)]

    loop_idx = _c_(64427, _n_(64426, "range", lambda: range), 64)
    _l_(64428)
    multiplier = [2] * _c_(64431, _n_(64429, "len", lambda: len), _n_(64430, "loop_idx", lambda: loop_idx))
    _l_(64432)

    # either with threading:
    results_threading = _c_(64437, _n_(64433, "thread_map", lambda: thread_map), _n_(64434, "calc_stuff", lambda: calc_stuff), _n_(64435, "loop_idx", lambda: loop_idx), _n_(64436, "multiplier", lambda: multiplier))
    _l_(64438)

    # or with multi-processing:
    results_processes = _c_(64443, _n_(64439, "process_map", lambda: process_map), _n_(64440, "calc_stuff", lambda: calc_stuff), _n_(64441, "loop_idx", lambda: loop_idx), _n_(64442, "multiplier", lambda: multiplier))
    _l_(64444)

