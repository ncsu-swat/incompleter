# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68084804/typeerror-lambda-takes-1-positional-argument-but-2-were-given-in-simplefix
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def decode(self, message: _n_(425592, "FixMessage", lambda: FixMessage), nth: _n_(425593, "int", lambda: int) = 1):
    _l_(425607)

    if (val := _c_(425598, _a_(425595, _n_(425594, "message", lambda: message), "get"), _n_(425596, "FIELD_ENCRYPT_METHOD", lambda: FIELD_ENCRYPT_METHOD), _n_(425597, "nth", lambda: nth))) is not None:
        _l_(425606)

        _n_(425599, "self", lambda: self).encrypt_method = _c_(425604, _n_(425600, "EncryptMethod", lambda: EncryptMethod), _c_(425603, _n_(425601, "int", lambda: int), _n_(425602, "val", lambda: val)))
        _l_(425605)