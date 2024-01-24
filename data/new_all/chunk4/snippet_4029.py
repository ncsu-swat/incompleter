# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63854512/how-to-fix-error-typeerror-a-bytes-like-object-is-required-not-str
#-*- coding: utf-8 -*-
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sha3
    _l_(625909)

except ImportError:
    pass
try:
    import pyopencl as cl
    _l_(625911)

except ImportError:
    pass
try:
    import Keccak
    _l_(625913)

except ImportError:
    pass
try:
    import time
    _l_(625915)

except ImportError:
    pass
#Initialize OpenCL
platforms = _c_(625918, _a_(625917, _n_(625916, "cl", lambda: cl), "get_platforms"))
_l_(625919)
devices = _c_(625922, _a_(625921, _n_(625920, "platforms", lambda: platforms)[0], "get_devices"))
_l_(625923)
context = _c_(625927, _a_(625925, _n_(625924, "cl", lambda: cl), "Context"), _n_(625926, "devices", lambda: devices)[:2])
_l_(625928)
queue = _c_(625937, _a_(625930, _n_(625929, "cl", lambda: cl), "CommandQueue"), _n_(625931, "context", lambda: context), _a_(625933, _n_(625932, "context", lambda: context), "devices")[0],
                        properties=_a_(625936, _a_(625935, _n_(625934, "cl", lambda: cl), "command_queue_properties"), "PROFILING_ENABLE"))
_l_(625938)
program = _c_(625948, _a_(625947, _c_(625946, _a_(625940, _n_(625939, "cl", lambda: cl), "Program"), _n_(625941, "context", lambda: context), _c_(625945, _a_(625944, _c_(625943, _n_(625942, "open", lambda: open), 'sha3.cl'), "read"))), "build"), options='')
_l_(625949)

#Parameters for SHA 512
r = 576
_l_(625950)
c = 1024
_l_(625951)
n = 512
_l_(625952)

inputlist = []
_l_(625953)
_c_(625956, _a_(625955, _n_(625954, "inputlist", lambda: inputlist), "append"), "a" * 1000)
_l_(625957)


start = _c_(625960, _a_(625959, _n_(625958, "time", lambda: time), "time"))
_l_(625961)
result = _c_(625971, _a_(625963, _n_(625962, "sha3", lambda: sha3), "Keccak"), _n_(625964, "inputlist", lambda: inputlist), _n_(625965, "n", lambda: n), _n_(625966, "r", lambda: r),_n_(625967, "c", lambda: c), _n_(625968, "program", lambda: program), _n_(625969, "context", lambda: context), _n_(625970, "queue", lambda: queue))
_l_(625972)
_c_(625974, _n_(625973, "print", lambda: print), "Hashing Result is")
_l_(625975)
_c_(625978, _n_(625976, "print", lambda: print), _n_(625977, "result", lambda: result))
_l_(625979)
_c_(625987, _n_(625980, "print", lambda: print), "Time taken is: " + _c_(625986, _n_(625981, "str", lambda: str), _c_(625984, _a_(625983, _n_(625982, "time", lambda: time), "time")) - _n_(625985, "start", lambda: start)))
_l_(625988)