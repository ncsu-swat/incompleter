# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55826705/pycryptodome-when-verifying-attributeerror-io-bufferedreader-object-has-no
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def get_signature(message):
    _l_(446018)

    h = _c_(446006, _a_(446004, _n_(446003, "SHA256", lambda: SHA256), "new"), _n_(446005, "message", lambda: message))
    _l_(446007)
    signature = _c_(446014, _a_(446012, _c_(446011, _a_(446009, _n_(446008, "pkcs1_15", lambda: pkcs1_15), "new"), _n_(446010, "priv_keyObj", lambda: priv_keyObj)), "sign"), _n_(446013, "h", lambda: h))
    _l_(446015)
    aux = _n_(446016, "signature", lambda: signature)
    _l_(446017)
    return aux

ENCODING = 'utf-8'
_l_(446019)

_c_(446040, _n_(446020, "print", lambda: print), _c_(446039, _a_(446022, _n_(446021, "json", lambda: json), "dumps"), {
    'EncryptedString':      _c_(446029, _a_(446027, _c_(446026, _a_(446024, _n_(446023, "base64", lambda: base64), "standard_b64encode"), _n_(446025, "encrypted_data", lambda: encrypted_data)), "decode"), _n_(446028, "ENCODING", lambda: ENCODING)),
    'SignedDataString':     _c_(446038, _a_(446036, _c_(446035, _a_(446031, _n_(446030, "base64", lambda: base64), "standard_b64encode"), _c_(446034, _n_(446032, "get_signature", lambda: get_signature), _n_(446033, "encrypted_data", lambda: encrypted_data))), "decode"), _n_(446037, "ENCODING", lambda: ENCODING)),
}))
_l_(446041)