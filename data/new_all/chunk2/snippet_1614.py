# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70557651/typeerror-using-pprint-on-counter-objects-that-have-been-updated-bit-of-an-ed
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    _l_(428425)

    _c_(428417, _a_(428416, _n_(428415, "intcounter", lambda: intcounter), "update"), {"Hello": "World"})
    _l_(428418)
except _n_(428419, "TypeError", lambda: TypeError) as t:
    _l_(428424)

    _c_(428422, _n_(428420, "print", lambda: print), _n_(428421, "t", lambda: t))
    _l_(428423)