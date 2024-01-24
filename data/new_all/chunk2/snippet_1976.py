# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72095459/typeerror-token-must-be-bytes-when-it-is-already-bytes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from cryptography.fernet import InvalidToken
    _l_(434083)

except ImportError:
    pass
try:
    from framework.local_storage_encryption import encrypt_data, decrypt_data
    _l_(434085)

except ImportError:
    pass

# get_history() ->
# -1: unknown exception
# 0: success
# 1: invalid key

def get_history(key):
    _l_(434114)

    try:
        _l_(434112)

        value = []
        _l_(434086)
        string_plain = _c_(434093, _n_(434087, "decrypt_data", lambda: decrypt_data), _n_(434088, "key", lambda: key), _c_(434092, _a_(434091, _c_(434090, _n_(434089, "open", lambda: open), 'local_storage/HISTORY'), "readlines")))
        _l_(434094)
        for url in _c_(434097, _a_(434096, _n_(434095, "string_plain", lambda: string_plain), "split"), "\n"):
            _l_(434103)

            _c_(434101, _a_(434099, _n_(434098, "value", lambda: value), "append"), _n_(434100, "url", lambda: url))
            _l_(434102)
        aux = _n_(434104, "value", lambda: value)
        _l_(434105)
        return aux
    except _n_(434106, "InvalidToken", lambda: InvalidToken) as exc:
        _l_(434111)

        _c_(434108, _n_(434107, "print", lambda: print), f"[!!!] Unable to load search history as the decryption key provided is invalid.")
        _l_(434109)
        aux = [], 1
        _l_(434110)
        return aux
    aux = [], -1
    _l_(434113)

    return aux

def save_history(key, value: _n_(434115, "list", lambda: list)):
    _l_(434132)

    string_plain = ""
    _l_(434116)
    for url in _n_(434117, "value", lambda: value):
        _l_(434120)

        string_plain += f"{_n_(434118, 'url', lambda: url)}\n"
        _l_(434119)

    with _c_(434122, _n_(434121, "open", lambda: open), 'local_storage/HISTORY', 'wb') as file:
        _l_(434131)

        _c_(434129, _a_(434124, _n_(434123, "file", lambda: file), "write"), _c_(434128, _n_(434125, "encrypt_data", lambda: encrypt_data), _n_(434126, "key", lambda: key), _n_(434127, "string_plain", lambda: string_plain)))
        _l_(434130)

history = _c_(434134, _n_(434133, "get_history", lambda: get_history), "test") # this function itself raises the error
_l_(434135) # this function itself raises the error