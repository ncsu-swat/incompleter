# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74637643/typeerror-argument-of-type-int-is-not-iterable-in-aes-algorithm-using-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from Crypto.Cipher import AES
    _l_(342760)

except ImportError:
    pass
try:
    from Crypto.Util.Padding import pad
    _l_(342762)

except ImportError:
    pass

key = 'QwroeApp90652321'
_l_(342763)
_n_(342764, "AES", lambda: AES).key_size=128
_l_(342765)
_n_(342766, "AES", lambda: AES).block_size=128
_l_(342767)
plaintext = "wdrdooloo"
_l_(342768)
cipher = _c_(342776, _a_(342770, _n_(342769, "AES", lambda: AES), "new"), _c_(342773, _a_(342772, _n_(342771, "key", lambda: key), "encode"), 'utf8'), _a_(342775, _n_(342774, "AES", lambda: AES), "MODE_ECB"))
_l_(342777)
msg =_c_(342785, _a_(342779, _n_(342778, "cipher", lambda: cipher), "encrypt"), _c_(342784, _n_(342780, "pad", lambda: pad), _c_(342783, _a_(342782, _n_(342781, "plaintext", lambda: plaintext), "encode"), 'utf8'), 16))
_l_(342786)
_c_(342791, _n_(342787, "print", lambda: print), _c_(342790, _a_(342789, _n_(342788, "msg", lambda: msg), "hex")))
_l_(342792)