# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68118319/typeerror-object-type-class-str-cannot-be-passed-to-c-code-using-pycryptodo
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from base64 import b64encode, b64decode
    _l_(562830)

except ImportError:
    pass
try:
    from Crypto.Cipher import AES
    _l_(562832)

except ImportError:
    pass

SOME_SECRET_KEY = 'HPo7OLqB4Fkk4E2yGOtwqw8H5fHR9kNx67OR4g4UdlA='
_l_(562833)
SOME_IV = 'p5ldmBPdd/9pjC0bDC/nSg=='
_l_(562834)
secret_key_in_bytes = _c_(562839, _n_(562835, "bytes", lambda: bytes), _c_(562838, _n_(562836, "b64decode", lambda: b64decode), _n_(562837, "SOME_SECRET_KEY", lambda: SOME_SECRET_KEY)))
_l_(562840)
iv_in_bytes = _c_(562845, _n_(562841, "bytes", lambda: bytes), _c_(562844, _n_(562842, "b64decode", lambda: b64decode), _n_(562843, "SOME_IV", lambda: SOME_IV)))
_l_(562846)

def decrypt_with_padding(data):
    _l_(562872)

    cypto_obj = _c_(562853, _a_(562848, _n_(562847, "AES", lambda: AES), "new"), _n_(562849, "secret_key_in_bytes", lambda: secret_key_in_bytes), _a_(562851, _n_(562850, "AES", lambda: AES), "MODE_CBC"), _n_(562852, "iv_in_bytes", lambda: iv_in_bytes))
    _l_(562854)
    decrypted = _c_(562860, _a_(562856, _n_(562855, "cypto_obj", lambda: cypto_obj), "decrypt"), _c_(562859, _n_(562857, "b64decode", lambda: b64decode), _n_(562858, "data", lambda: data)))
    _l_(562861)
    bytes_to_string = _c_(562864, _a_(562863, _n_(562862, "decrypted", lambda: decrypted), "decode"), "utf-8")
    _l_(562865)
    decrypted_data = _c_(562868, _n_(562866, "pkcs5_unpad", lambda: pkcs5_unpad), _n_(562867, "bytes_to_string", lambda: bytes_to_string))
    _l_(562869)
    aux = _n_(562870, "decrypted_data", lambda: decrypted_data)
    _l_(562871)
    return aux


def encrypt_with_padding(data):
    _l_(562896)

    cypto_obj = _c_(562879, _a_(562874, _n_(562873, "AES", lambda: AES), "new"), _n_(562875, "secret_key_in_bytes", lambda: secret_key_in_bytes), _a_(562877, _n_(562876, "AES", lambda: AES), "MODE_CBC"), _n_(562878, "iv_in_bytes", lambda: iv_in_bytes))
    _l_(562880)
    encrypted_data = _c_(562888, _a_(562882, _n_(562881, "cypto_obj", lambda: cypto_obj), "encrypt"), _c_(562887, _n_(562883, "pkcs5_pad", lambda: pkcs5_pad), _c_(562886, _n_(562884, "str", lambda: str), _n_(562885, "data", lambda: data))))
    _l_(562889)
    aux = _c_(562894, _a_(562893, _c_(562892, _n_(562890, "b64encode", lambda: b64encode), _n_(562891, "encrypted_data", lambda: encrypted_data)), "decode"))
    _l_(562895)
    return aux


def pkcs5_pad(s, BLOCK_SIZE=16):
    _l_(562911)

    aux = _n_(562897, "s", lambda: s) + (_n_(562898, "BLOCK_SIZE", lambda: BLOCK_SIZE) - _c_(562901, _n_(562899, "len", lambda: len), _n_(562900, "s", lambda: s)) % _n_(562902, "BLOCK_SIZE", lambda: BLOCK_SIZE)) * _c_(562909, _n_(562903, "chr", lambda: chr), _n_(562904, "BLOCK_SIZE", lambda: BLOCK_SIZE) - _c_(562907, _n_(562905, "len", lambda: len), _n_(562906, "s", lambda: s)) % _n_(562908, "BLOCK_SIZE", lambda: BLOCK_SIZE)
    )
    _l_(562910)
    return aux


def pkcs5_unpad(s):
    _l_(562917)

    aux = _n_(562912, "s", lambda: s)[0: -_c_(562915, _n_(562913, "ord", lambda: ord), _n_(562914, "s", lambda: s)[-1])]
    _l_(562916)
    return aux


if _n_(562918, "__name__", lambda: __name__) == "__main__":
    _l_(562936)

    data = '{"idServicio":79, "idProducto":209 , "referencia": "40425475190118187271", "montoPago": 9999, "telefono":"1111111111", "horaLocal":"20200401222821"}'
    _l_(562919)
    encrypted = _c_(562922, _n_(562920, "encrypt_with_padding", lambda: encrypt_with_padding), _n_(562921, "data", lambda: data))
    _l_(562923)
    _c_(562926, _n_(562924, "print", lambda: print), _n_(562925, "encrypted", lambda: encrypted))
    _l_(562927)
    decrypted = _c_(562930, _n_(562928, "decrypt_with_padding", lambda: decrypt_with_padding), _n_(562929, "encrypted", lambda: encrypted))
    _l_(562931)
    _c_(562934, _n_(562932, "print", lambda: print), _n_(562933, "decrypted", lambda: decrypted))
    _l_(562935)