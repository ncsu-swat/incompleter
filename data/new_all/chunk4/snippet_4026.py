# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63854512/how-to-fix-error-typeerror-a-bytes-like-object-is-required-not-str
#-*- coding: utf-8 -*-
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sha3
    _l_(634969)

except ImportError:
    pass
try:
    import pyopencl as cl
    _l_(634971)

except ImportError:
    pass
try:
    import Keccak
    _l_(634973)

except ImportError:
    pass
try:
    import time
    _l_(634975)

except ImportError:
    pass
#Initialize OpenCL
platforms = _c_(634978, _a_(634977, _n_(634976, "cl", lambda: cl), "get_platforms"))
_l_(634979)
devices = _c_(634982, _a_(634981, _n_(634980, "platforms", lambda: platforms)[0], "get_devices"))
_l_(634983)
context = _c_(634987, _a_(634985, _n_(634984, "cl", lambda: cl), "Context"), _n_(634986, "devices", lambda: devices)[:2])
_l_(634988)
queue = _c_(634997, _a_(634990, _n_(634989, "cl", lambda: cl), "CommandQueue"), _n_(634991, "context", lambda: context), _a_(634993, _n_(634992, "context", lambda: context), "devices")[0],
                        properties=_a_(634996, _a_(634995, _n_(634994, "cl", lambda: cl), "command_queue_properties"), "PROFILING_ENABLE"))
_l_(634998)
program = _c_(635008, _a_(635007, _c_(635006, _a_(635000, _n_(634999, "cl", lambda: cl), "Program"), _n_(635001, "context", lambda: context), _c_(635005, _a_(635004, _c_(635003, _n_(635002, "open", lambda: open), 'sha3.cl'), "read"))), "build"), options='')
_l_(635009)

#Parameters for SHA 512
r = 576
_l_(635010)
c = 1024
_l_(635011)
n = 512
_l_(635012)

inputlist = []
_l_(635013)
_c_(635016, _a_(635015, _n_(635014, "inputlist", lambda: inputlist), "append"), "a" * 1000)
_l_(635017)


start = _c_(635020, _a_(635019, _n_(635018, "time", lambda: time), "time"))
_l_(635021)
result = _c_(635031, _a_(635023, _n_(635022, "sha3", lambda: sha3), "Keccak"), _n_(635024, "inputlist", lambda: inputlist), _n_(635025, "n", lambda: n), _n_(635026, "r", lambda: r),_n_(635027, "c", lambda: c), _n_(635028, "program", lambda: program), _n_(635029, "context", lambda: context), _n_(635030, "queue", lambda: queue))
_l_(635032)
_c_(635034, _n_(635033, "print", lambda: print), "Hashing Result is")
_l_(635035)
_c_(635038, _n_(635036, "print", lambda: print), _n_(635037, "result", lambda: result))
_l_(635039)
_c_(635047, _n_(635040, "print", lambda: print), "Time taken is: " + _c_(635046, _n_(635041, "str", lambda: str), _c_(635044, _a_(635043, _n_(635042, "time", lambda: time), "time")) - _n_(635045, "start", lambda: start)))
_l_(635048)