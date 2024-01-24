# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75316722/nested-keyword-arguments-emitting-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def send(self, request: _a_(597935, _n_(597934, "requests", lambda: requests), "PrepareRequest"), **kwargs):
    _l_(597944)

    ...
    _l_(597936)
    _c_(597941, _a_(597938, _n_(597937, "super", lambda: super)(), "send"), request=_n_(597939, "request", lambda: request), **_n_(597940, "kwargs", lambda: kwargs))
    _l_(597942)
    ...
    _l_(597943)