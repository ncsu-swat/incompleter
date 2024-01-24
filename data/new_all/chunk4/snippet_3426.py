# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74599866/typeerror-argument-of-type-mx-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import dns.resolver
    _l_(594361)

except ImportError:
    pass
answer=_c_(594364, _a_(594363, _a_(594362, dns, "resolver"), "resolve"), "google.com", "MX")
_l_(594365)
for data in _n_(594366, "answer", lambda: answer):
    _l_(594376)

    _c_(594369, _n_(594367, "print", lambda: print), _n_(594368, "data", lambda: data))
    _l_(594370)
    if "smtp.google.com" in _n_(594371, "data", lambda: data):
        _l_(594375)

        _c_(594373, _n_(594372, "print", lambda: print), "cool")
        _l_(594374)