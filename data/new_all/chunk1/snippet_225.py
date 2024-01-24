# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/35957085/python3-typeerror-list-indices-must-be-integers-or-slices-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
list = []
_l_(382837)

string = 'AAAABBBCCDAABBB'
_l_(382838)

i = 1
_l_(382839)

for i in _n_(382840, "string", lambda: string):
    _l_(382846)

    _c_(382844, _a_(382842, _n_(382841, "list", lambda: list), "append"), _n_(382843, "i", lambda: i))
    _l_(382845)

_c_(382849, _n_(382847, "print", lambda: print), _n_(382848, "list", lambda: list))
_l_(382850)

for element in _n_(382851, "list", lambda: list):
    _l_(382863)

    if _n_(382852, "list", lambda: list)[_n_(382853, "element", lambda: element)] == _n_(382854, "list", lambda: list)[_n_(382855, "element", lambda: element)-1]:
        _l_(382862)

        _c_(382860, _a_(382857, _n_(382856, "list", lambda: list), "remove"), _n_(382858, "list", lambda: list)[_n_(382859, "element", lambda: element)])
        _l_(382861)

_c_(382866, _n_(382864, "print", lambda: print), _n_(382865, "list", lambda: list))
_l_(382867)