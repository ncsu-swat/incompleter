# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57719844/how-to-fix-typeerror-nonetype-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
counter = 1000
_l_(349821)
while _n_(349822, "counter", lambda: counter) != 10000:
    _l_(349867)

    digits = [_c_(349825, _n_(349823, "int", lambda: int), _n_(349824, "x", lambda: x)) for x in _c_(349828, _n_(349826, "str", lambda: str), _n_(349827, "counter", lambda: counter))]
    _l_(349829)
    bigdigits = _c_(349832, _a_(349831, _n_(349830, "digits", lambda: digits), "sort"), reverse = True)
    _l_(349833)
    smalldigits = _c_(349836, _a_(349835, _n_(349834, "digits", lambda: digits), "sort"))
    _l_(349837)

    strbigdigs = [_c_(349840, _n_(349838, "str", lambda: str), _n_(349839, "i", lambda: i)) for i in _n_(349841, "bigdigits", lambda: bigdigits)]
    _l_(349842)
    bignum = _c_(349847, _n_(349843, "int", lambda: int), _c_(349846, _a_(349844, "", "join"), _n_(349845, "strbigdigs", lambda: strbigdigs)))
    _l_(349848)

    strsmalldigs = [_c_(349851, _n_(349849, "str", lambda: str), _n_(349850, "j", lambda: j)) for j in _n_(349852, "smalldigits", lambda: smalldigits)]
    _l_(349853)
    smallnum = _c_(349858, _n_(349854, "int", lambda: int), _c_(349857, _a_(349855, "", "join"), _n_(349856, "smalldigits", lambda: smalldigits)))
    _l_(349859)

    partialanswer = _n_(349860, "bignum", lambda: bignum) - _n_(349861, "smallnum", lambda: smallnum)
    _l_(349862)
    _c_(349865, _n_(349863, "print", lambda: print), _n_(349864, "partialanswer", lambda: partialanswer))
    _l_(349866)