# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63854512/how-to-fix-error-typeerror-a-bytes-like-object-is-required-not-str
#-*- coding: utf-8 -*-
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sha3
    _l_(639070)

except ImportError:
    pass
try:
    import pyopencl as cl
    _l_(639072)

except ImportError:
    pass
try:
    import Keccak
    _l_(639074)

except ImportError:
    pass
try:
    import time
    _l_(639076)

except ImportError:
    pass
#Initialize OpenCL
platforms = _c_(639079, _a_(639078, _n_(639077, "cl", lambda: cl), "get_platforms"))
_l_(639080)
devices = _c_(639083, _a_(639082, _n_(639081, "platforms", lambda: platforms)[0], "get_devices"))
_l_(639084)
context = _c_(639088, _a_(639086, _n_(639085, "cl", lambda: cl), "Context"), _n_(639087, "devices", lambda: devices)[:2])
_l_(639089)
queue = _c_(639098, _a_(639091, _n_(639090, "cl", lambda: cl), "CommandQueue"), _n_(639092, "context", lambda: context), _a_(639094, _n_(639093, "context", lambda: context), "devices")[0],
                        properties=_a_(639097, _a_(639096, _n_(639095, "cl", lambda: cl), "command_queue_properties"), "PROFILING_ENABLE"))
_l_(639099)
program = _c_(639109, _a_(639108, _c_(639107, _a_(639101, _n_(639100, "cl", lambda: cl), "Program"), _n_(639102, "context", lambda: context), _c_(639106, _a_(639105, _c_(639104, _n_(639103, "open", lambda: open), 'sha3.cl'), "read"))), "build"), options='')
_l_(639110)

#Parameters for SHA 512
r = 576
_l_(639111)
c = 1024
_l_(639112)
n = 512
_l_(639113)

inputlist = []
_l_(639114)
_c_(639117, _a_(639116, _n_(639115, "inputlist", lambda: inputlist), "append"), "a" * 1000)
_l_(639118)


start = _c_(639121, _a_(639120, _n_(639119, "time", lambda: time), "time"))
_l_(639122)
result = _c_(639132, _a_(639124, _n_(639123, "sha3", lambda: sha3), "Keccak"), _n_(639125, "inputlist", lambda: inputlist), _n_(639126, "n", lambda: n), _n_(639127, "r", lambda: r),_n_(639128, "c", lambda: c), _n_(639129, "program", lambda: program), _n_(639130, "context", lambda: context), _n_(639131, "queue", lambda: queue))
_l_(639133)
_c_(639135, _n_(639134, "print", lambda: print), "Hashing Result is")
_l_(639136)
_c_(639139, _n_(639137, "print", lambda: print), _n_(639138, "result", lambda: result))
_l_(639140)
_c_(639148, _n_(639141, "print", lambda: print), "Time taken is: " + _c_(639147, _n_(639142, "str", lambda: str), _c_(639145, _a_(639144, _n_(639143, "time", lambda: time), "time")) - _n_(639146, "start", lambda: start)))
_l_(639149)