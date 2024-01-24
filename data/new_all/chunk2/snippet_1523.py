# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45762517/attributeerror-rsa-object-has-no-attribute-n
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from Rsa import RsaEncryptionAndDecryption
    _l_(434345)

except ImportError:
    pass
try:
    from appJar import gui
    _l_(434347)

except ImportError:
    pass

app = _c_(434349, _n_(434348, "gui", lambda: gui))
_l_(434350)
rsa = _c_(434353, _a_(434352, _n_(434351, "RsaEncryptionAndDecryption", lambda: RsaEncryptionAndDecryption), "Rsa"))
_l_(434354)

def encode(name):
    _l_(434384)

    msg = _c_(434357, _a_(434356, _n_(434355, "app", lambda: app), "getEntry"), 'Input to Encode Here')
    _l_(434358)
    if _n_(434359, "msg", lambda: msg) != '':
        _l_(434383)

        p, q = _c_(434362, _a_(434361, _n_(434360, "rsa", lambda: rsa), "findingPandQ"))
        _l_(434363)

        while _n_(434364, "p", lambda: p) == _n_(434365, "q", lambda: q):
            _l_(434370)

            p, q = _c_(434368, _a_(434367, _n_(434366, "rsa", lambda: rsa), "findingPandQ"))
            _l_(434369)

        n, e, d = _c_(434375, _a_(434372, _n_(434371, "rsa", lambda: rsa), "generate_keys"), _n_(434373, "p", lambda: p), _n_(434374, "q", lambda: q))
        _l_(434376)

        _c_(434381, _n_(434377, "print", lambda: print), _n_(434378, "n", lambda: n), _n_(434379, "e", lambda: e), _n_(434380, "d", lambda: d))
        _l_(434382)