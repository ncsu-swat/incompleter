# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/33022424/typeerror-str-does-not-support-the-buffer-interface-python-3-4-conversion
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from base64 import b64encode
    _l_(473050)

except ImportError:
    pass

username = 'manager'
_l_(473051)
password = 'test.manager'
_l_(473052)

headers = {"Authorization": " Basic " + _c_(473056, _n_(473053, "b64encode", lambda: b64encode), _n_(473054, "username", lambda: username) + ":" + _n_(473055, "password", lambda: password)), "Content-Type": "application/json"}
_l_(473057)