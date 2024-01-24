# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64113949/attributeerror-bytes-object-has-no-attribute-encode-in-python-3-6
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(545176)

except ImportError:
    pass
try:
    import json
    _l_(545178)

except ImportError:
    pass
try:
    import pymssql
    _l_(545180)

except ImportError:
    pass
try:
    from pymongo import MongoClient
    _l_(545182)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(545184)

except ImportError:
    pass
try:
    from cryptography.fernet import Fernet
    _l_(545186)

except ImportError:
    pass

encrypted_pwd='gAAAAABfcsCIlNNosZ2bWzUDueAVoIPjUFOqjNCOIOTUrOkrf_TK2FaC1L5b0VXo2ZKBz1VYA25jVfXBQQ5Y-vwTZA7339onZw=='
_l_(545187)

def vantiveDvDBConnection():
    _l_(545197)

    conn = _c_(545193, _a_(545189, _n_(545188, "pymssql", lambda: pymssql), "connect"), 'abc.def.ad.is.net:5010','itcompl',_c_(545192, _n_(545190, "decrypt_message", lambda: decrypt_message), _n_(545191, "encrypted_pwd", lambda: encrypted_pwd)), 'VN2DV')
    _l_(545194)
    aux = _n_(545195, "conn", lambda: conn)
    _l_(545196)
    return aux

def decrypt_message(enc_message):
    _l_(545227)

    _c_(545199, _n_(545198, "print", lambda: print), "inside decrypt")
    _l_(545200)
    key=_c_(545202, _n_(545201, "load_key", lambda: load_key))
    _l_(545203)
    _c_(545206, _n_(545204, "print", lambda: print), _n_(545205, "key", lambda: key))
    _l_(545207)
    f=_c_(545210, _n_(545208, "Fernet", lambda: Fernet), _n_(545209, "key", lambda: key))
    _l_(545211)
    _c_(545216, _n_(545212, "print", lambda: print), _c_(545215, _a_(545214, _n_(545213, "enc_message", lambda: enc_message), "encode")))
    _l_(545217)
    decrypt_message=_c_(545223, _a_(545219, _n_(545218, "f", lambda: f), "decrypt"), _c_(545222, _a_(545221, _n_(545220, "enc_message", lambda: enc_message), "encode")))
    _l_(545224)
    aux = _n_(545225, "decrypt_message", lambda: decrypt_message)
    _l_(545226)
    return aux