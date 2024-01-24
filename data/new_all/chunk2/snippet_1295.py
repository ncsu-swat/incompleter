# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54831355/how-to-fix-bcrypt-type-error-unicode-objects-must-be-encoded-before-hashing
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import bcrypt
    _l_(437676)

except ImportError:
    pass

password = _c_(437678, _n_(437677, "input", lambda: input), "Input your desired password: ")
_l_(437679)
hashedPassword = _c_(437686, _a_(437681, _n_(437680, "bcrypt", lambda: bcrypt), "hashpw"), _n_(437682, "password", lambda: password), _c_(437685, _a_(437684, _n_(437683, "bcrypt", lambda: bcrypt), "gensalt")))
_l_(437687)