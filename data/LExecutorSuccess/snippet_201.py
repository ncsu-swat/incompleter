# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(1538230)

except ImportError:
    pass
h = '{"foo":"bar", "foo2":"bar2"}'
_l_(1538231)
d = _c_(1538235, _a_(1538233, _n_(1538232, "json", lambda: json), "loads"), _n_(1538234, "h", lambda: h))
_l_(1538236)
_n_(1538237, "d", lambda: d)
_l_(1538238)
{u'foo': u'bar', u'foo2': u'bar2'}
_l_(1538239)
_c_(1538242, _n_(1538240, "type", lambda: type), _n_(1538241, "d", lambda: d))
_l_(1538243)

