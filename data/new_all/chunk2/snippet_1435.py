# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59516802/typeerror-a-bytes-like-object-is-required-not-str-xxxxxx
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def create_key(x):
    _l_(460322)

    try:
        import base64
        _l_(460269)

    except ImportError:
        pass
    try:
        import os
        _l_(460271)

    except ImportError:
        pass
    try:
        from cryptography.hazmat.backends import default_backend
        _l_(460273)

    except ImportError:
        pass
    try:
        from cryptography.hazmat.primitives import hashes
        _l_(460275)

    except ImportError:
        pass
    try:
        from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
        _l_(460277)

    except ImportError:
        pass

    password_provided = _c_(460280, _n_(460278, "str", lambda: str), _n_(460279, "x", lambda: x))
    _l_(460281)
    password = _c_(460284, _a_(460283, _n_(460282, "password_provided", lambda: password_provided), "encode"))
    _l_(460285)
    salt = b'\xfb|\xe8\xe0\xe5\x9d\x11\xf5\xbc 8o\xbe<\xd9\x92'
    _l_(460286)
    kdf = _c_(460294, _n_(460287, "PBKDF2HMAC", lambda: PBKDF2HMAC), algorithm=_c_(460290, _a_(460289, _n_(460288, "hashes", lambda: hashes), "SHA256")),
        length=32,
        salt=_n_(460291, "salt", lambda: salt),
        iterations=100000,
        backend=_c_(460293, _n_(460292, "default_backend", lambda: default_backend))
    )
    _l_(460295)
    key = _c_(460302, _a_(460297, _n_(460296, "base64", lambda: base64), "urlsafe_b64encode"), _c_(460301, _a_(460299, _n_(460298, "kdf", lambda: kdf), "derive"), _n_(460300, "password", lambda: password)))
    _l_(460303)
    f1 = _c_(460305, _n_(460304, "open", lambda: open), 'keys.key', 'ab')
    _l_(460306)
    _c_(460310, _a_(460308, _n_(460307, "f1", lambda: f1), "write"), _n_(460309, "key", lambda: key))
    _l_(460311)
    _c_(460316, _a_(460313, _n_(460312, "f1", lambda: f1), "write"), _a_(460315, _n_(460314, "os", lambda: os), "linesep"))
    _l_(460317)
    _c_(460320, _a_(460319, _n_(460318, "f1", lambda: f1), "close"))
    _l_(460321)


_c_(460324, _n_(460323, "create_key", lambda: create_key), 'sairam')
_l_(460325)