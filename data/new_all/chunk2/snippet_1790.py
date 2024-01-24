# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55826705/pycryptodome-when-verifying-attributeerror-io-bufferedreader-object-has-no
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def verify_signature(message, signature):
    _l_(460827)

    h = _c_(460806, _a_(460804, _n_(460803, "SHA256", lambda: SHA256), "new"), _n_(460805, "message", lambda: message))
    _l_(460807)
    try:
        _l_(460826)

        _c_(460815, _a_(460812, _c_(460811, _a_(460809, _n_(460808, "pkcs1_15", lambda: pkcs1_15), "new"), _n_(460810, "pub_key_new", lambda: pub_key_new)), "verify"), _n_(460813, "h", lambda: h), _n_(460814, "signature", lambda: signature))
        _l_(460816)
        _c_(460818, _n_(460817, "print", lambda: print), "The signature is valid.")
        _l_(460819)
    except (_n_(460820, "ValueError", lambda: ValueError), _n_(460821, "TypeError", lambda: TypeError)):
        _l_(460825)

        _c_(460823, _n_(460822, "print", lambda: print), "The signature is not valid.")
        _l_(460824)

_c_(460837, _n_(460828, "verify_signature", lambda: verify_signature), _c_(460832, _a_(460830, _n_(460829, "base64", lambda: base64), "standard_b64decode"), _n_(460831, "data", lambda: data)['EncryptedString']), _c_(460836, _a_(460834, _n_(460833, "base64", lambda: base64), "standard_b64decode"), _n_(460835, "data", lambda: data)['SignedDataString']))
_l_(460838)