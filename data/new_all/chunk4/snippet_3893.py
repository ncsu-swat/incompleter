# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65811328/why-do-i-get-a-typeerror-while-updating-hash-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import string, random, hashlib
    _l_(635480)

except ImportError:
    pass

def hash_and_salt(password):
    _l_(635506)

    password_hash = _c_(635483, _a_(635482, _n_(635481, "hashlib", lambda: hashlib), "sha256"))
    _l_(635484)
    salt = _c_(635493, _a_(635485, '', "join"), (_c_(635490, _a_(635487, _n_(635486, "random", lambda: random), "choice"), _a_(635489, _n_(635488, "string", lambda: string), "digits")) for i in _c_(635492, _n_(635491, "range", lambda: range), 8)))
    _l_(635494)
    _c_(635499, _a_(635496, _n_(635495, "password_hash", lambda: password_hash), "update"), _n_(635497, "salt", lambda: salt) + _n_(635498, "password", lambda: password))
    _l_(635500)
    aux = _c_(635503, _a_(635502, _n_(635501, "password_hash", lambda: password_hash), "hexdigest")) , _n_(635504, "salt", lambda: salt) 
    _l_(635505) 
    return aux 



_c_(635508, _n_(635507, "hash_and_salt", lambda: hash_and_salt), password="hello_world")
_l_(635509)