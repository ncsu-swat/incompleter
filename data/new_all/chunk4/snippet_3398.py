# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74904901/python-google-voice-api-login-error-attributeerror-nonetype-object-has-no-at
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from googlevoice import Voice
    _l_(632042)

except ImportError:
    pass
try:
    import keyring
    _l_(632044)

except ImportError:
    pass

if _n_(632045, "__name__", lambda: __name__) == '__main__':
    _l_(632063)

    gv = _c_(632047, _n_(632046, "Voice", lambda: Voice))
    _l_(632048)
    usr = _c_(632051, _a_(632050, _n_(632049, "keyring", lambda: keyring), "get_password"), '2', '2')
    _l_(632052)
    pwd = _c_(632055, _a_(632054, _n_(632053, "keyring", lambda: keyring), "get_password"), '1', '1')
    _l_(632056)
    client = _c_(632061, _a_(632058, _n_(632057, "gv", lambda: gv), "login"), _n_(632059, "usr", lambda: usr),_n_(632060, "pwd", lambda: pwd))
    _l_(632062)