# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47863796/type-error-encountered-while-working-on-custom-encode-in-python-3-6
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(609846)

except ImportError:
    pass
try:
    import sys
    _l_(609848)

except ImportError:
    pass
try:
    import base64
    _l_(609850)

except ImportError:
    pass

def encode(key, clear):
    _l_(609886)

    """encode custom """
    enc = []
    _l_(609851)
    for i in _c_(609856, _n_(609852, "range", lambda: range), _c_(609855, _n_(609853, "len", lambda: len), _n_(609854, "clear", lambda: clear))):
        _l_(609878)

        key_c = _n_(609857, "key", lambda: key)[_n_(609858, "i", lambda: i) % _c_(609861, _n_(609859, "len", lambda: len), _n_(609860, "key", lambda: key))]
        _l_(609862)
        enc_c = _c_(609871, _n_(609863, "chr", lambda: chr), (_c_(609867, _n_(609864, "ord", lambda: ord), _n_(609865, "clear", lambda: clear)[_n_(609866, "i", lambda: i)]) + _c_(609870, _n_(609868, "ord", lambda: ord), _n_(609869, "key_c", lambda: key_c))) % 256)
        _l_(609872)
        #change the int or str
        _c_(609876, _a_(609874, _n_(609873, "enc", lambda: enc), "append"), _n_(609875, "enc_c", lambda: enc_c))
        _l_(609877)
    aux = _c_(609884, _a_(609880, _n_(609879, "base64", lambda: base64), "urlsafe_b64encode"), _c_(609883, _a_(609881, "", "join"), _n_(609882, "enc", lambda: enc)))
    _l_(609885)
    return aux

clear = "ABCDEFGH"
_l_(609887)
encode_var = _c_(609890, _n_(609888, "encode", lambda: encode), "crumbs", _n_(609889, "clear", lambda: clear))
_l_(609891)