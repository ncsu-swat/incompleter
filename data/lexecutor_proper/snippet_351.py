# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4888027/python-and-pip-list-all-versions-of-a-package-thats-available
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(62463)

except ImportError:
    pass
r = _c_(62466, _a_(62465, _n_(62464, "requests", lambda: requests), "get"), "https://pypi.org/pypi/Flask/json")
_l_(62467)
_c_(62474, _n_(62468, "print", lambda: print), _c_(62473, _a_(62472, _c_(62471, _a_(62470, _n_(62469, "r", lambda: r), "json"))['releases'], "keys")))
_l_(62475)

_c_(62477, _n_(62476, "dict_keys", lambda: dict_keys), ['0.1', '0.10', '0.10.1', '0.11', '0.11.1', '0.12', '0.12.1', '0.12.2', '0.12.3', '0.12.4', '0.2', '0.3', '0.3.1', '0.4', '0.5', '0.5.1', '0.5.2', '0.6', '0.6.1', '0.7', '0.7.1', '0.7.2', '0.8', '0.8.1', '0.9', '1.0', '1.0.1', '1.0.2'])
_l_(62478)

