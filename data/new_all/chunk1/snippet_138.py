# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75565224/in-pyvis-i-always-get-this-error-attributeerror-nonetype-object-has-no-attr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pyvis.network import Network
    _l_(396387)

except ImportError:
    pass
g = _c_(396389, _n_(396388, "Network", lambda: Network))
_l_(396390)
_c_(396393, _a_(396392, _n_(396391, "g", lambda: g), "add_node"), 0)
_l_(396394)
_c_(396397, _a_(396396, _n_(396395, "g", lambda: g), "add_node"), 1)
_l_(396398)
_c_(396401, _a_(396400, _n_(396399, "g", lambda: g), "add_edge"), 0, 1)
_l_(396402)
_c_(396405, _a_(396404, _n_(396403, "g", lambda: g), "show"), 'test.html')
_l_(396406)