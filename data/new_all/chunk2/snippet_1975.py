# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72095459/typeerror-token-must-be-bytes-when-it-is-already-bytes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import base64
    _l_(464654)

except ImportError:
    pass
try:
    import os
    _l_(464656)

except ImportError:
    pass
try:
    from cryptography.fernet import Fernet
    _l_(464658)

except ImportError:
    pass
try:
    from cryptography.hazmat.primitives import hashes
    _l_(464660)

except ImportError:
    pass
try:
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    _l_(464662)

except ImportError:
    pass

def decrypt_data(key, data):
    _l_(464692)

    key = _c_(464667, _n_(464663, "bytes", lambda: bytes), _c_(464666, _a_(464665, _n_(464664, "key", lambda: key), "encode"), 'utf-8'))
    _l_(464668)
    SALT = b'\xbf\xd4\xa9\xcei\xfa\xa7Db\x83\xbf\xa5.\xbe/\xd9'
    _l_(464669)

    kdf = _c_(464675, _n_(464670, "PBKDF2HMAC", lambda: PBKDF2HMAC), _c_(464673, _a_(464672, _n_(464671, "hashes", lambda: hashes), "SHA256")),
        length=32,
        salt=_n_(464674, "SALT", lambda: SALT),
        iterations=32000
    )
    _l_(464676)
    fernet = _c_(464685, _n_(464677, "Fernet", lambda: Fernet), _c_(464684, _a_(464679, _n_(464678, "base64", lambda: base64), "urlsafe_b64encode"), _c_(464683, _a_(464681, _n_(464680, "kdf", lambda: kdf), "derive"), _n_(464682, "key", lambda: key))))
    _l_(464686)
    aux = _c_(464690, _a_(464688, _n_(464687, "fernet", lambda: fernet), "decrypt"), _n_(464689, "data", lambda: data))
    _l_(464691)
    return aux

def encrypt_data(key, data):
    _l_(464726)

    key = _c_(464697, _n_(464693, "bytes", lambda: bytes), _c_(464696, _a_(464695, _n_(464694, "key", lambda: key), "encode"), 'utf-8'))
    _l_(464698)
    SALT = b'\xbf\xd4\xa9\xcei\xfa\xa7Db\x83\xbf\xa5.\xbe/\xd9'
    _l_(464699)

    kdf = _c_(464705, _n_(464700, "PBKDF2HMAC", lambda: PBKDF2HMAC), _c_(464703, _a_(464702, _n_(464701, "hashes", lambda: hashes), "SHA256")),
        length=32,
        salt=_n_(464704, "SALT", lambda: SALT),
        iterations=32000
    )
    _l_(464706)

    key = _c_(464713, _a_(464708, _n_(464707, "base64", lambda: base64), "urlsafe_b64encode"), _c_(464712, _a_(464710, _n_(464709, "kdf", lambda: kdf), "derive"), _n_(464711, "key", lambda: key)))
    _l_(464714)
    fernet = _c_(464717, _n_(464715, "Fernet", lambda: Fernet), _n_(464716, "key", lambda: key))
    _l_(464718)
    aux = _c_(464724, _a_(464720, _n_(464719, "fernet", lambda: fernet), "encrypt"), _c_(464723, _a_(464722, _n_(464721, "data", lambda: data), "encode")))
    _l_(464725)
    return aux