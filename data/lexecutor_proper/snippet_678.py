# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6921699/can-i-get-json-to-load-into-an-ordereddict
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
my_ordered_dict = _c_(64183, _a_(64179, _n_(64178, "json", lambda: json), "loads"), _n_(64180, "json_str", lambda: json_str), object_pairs_hook=_a_(64182, _n_(64181, "collections", lambda: collections), "OrderedDict"))
_l_(64184)
try:
    import simplejson as json
    _l_(64186)

except ImportError:
    pass
try:
    import ordereddict
    _l_(64188)

except ImportError:
    pass

my_ordered_dict = _c_(64194, _a_(64190, _n_(64189, "json", lambda: json), "loads"), _n_(64191, "json_str", lambda: json_str), object_pairs_hook=_a_(64193, _n_(64192, "ordereddict", lambda: ordereddict), "OrderedDict"))
_l_(64195)

