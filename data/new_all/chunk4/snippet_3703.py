# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69653682/typeerror-return-entry-takes-0-positional-arguments-but-1-was-given-the-conv
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def return_entry() :
    _l_(646020)

    content = _c_(646014, _a_(646013, _n_(646012, "ew", lambda: ew), "get"))
    _l_(646015)
    _c_(646018, _n_(646016, "print", lambda: print), _n_(646017, "content", lambda: content))
    _l_(646019)

ew = _c_(646024, _n_(646021, "Entry", lambda: Entry), _n_(646022, "root", lambda: root), font = _n_(646023, "myfont", lambda: myfont), width = 30)
_l_(646025)
_c_(646028, _a_(646027, _n_(646026, "ew", lambda: ew), "place"), x = 170, y = 100)
_l_(646029)
_c_(646033, _a_(646031, _n_(646030, "ew", lambda: ew), "bind"), '<Return>', _n_(646032, "return_entry", lambda: return_entry))
_l_(646034)