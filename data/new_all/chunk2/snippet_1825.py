# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51443890/scapy-indexing-traceroute-result-with-get-trace-method-returns-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from scapy.all import *
    _l_(467349)

except ImportError:
    pass

target = '52.54.2.173'
_l_(467350)
result, unans = _c_(467353, _n_(467351, "traceroute", lambda: traceroute), _n_(467352, "target", lambda: target))
_l_(467354)

_c_(467361, _n_(467355, "print", lambda: print), _c_(467360, _a_(467359, _c_(467358, _a_(467357, _n_(467356, "result", lambda: result), "get_trace")), "keys")))
_l_(467362)