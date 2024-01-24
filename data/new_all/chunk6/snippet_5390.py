# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57740763/getting-typeerror-byte-indices-must-be-integers-or-slices-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(353040)

except ImportError:
    pass

class Branches(_a_(353042, _n_(353041, "models", lambda: models), "Model")):
    _l_(353079)


    ifsc       = _c_(353045, _a_(353044, _n_(353043, "models", lambda: models), "CharField"), max_length=1009)
    _l_(353046)
    bank_id    = _c_(353049, _a_(353048, _n_(353047, "models", lambda: models), "IntegerField"))
    _l_(353050)
    branch     = _c_(353053, _a_(353052, _n_(353051, "models", lambda: models), "CharField"), max_length=1009)
    _l_(353054)
    address    = _c_(353057, _a_(353056, _n_(353055, "models", lambda: models), "CharField"), max_length=1500)
    _l_(353058)
    city       = _c_(353061, _a_(353060, _n_(353059, "models", lambda: models), "CharField"), max_length=1999)
    _l_(353062)
    district   = _c_(353065, _a_(353064, _n_(353063, "models", lambda: models), "CharField"), max_length=1999)
    _l_(353066)
    state      = _c_(353069, _a_(353068, _n_(353067, "models", lambda: models), "CharField"), max_length=1000)
    _l_(353070)
    bank_name  = _c_(353073, _a_(353072, _n_(353071, "models", lambda: models), "CharField"), max_length=1000)
    _l_(353074)


    def __str__(self):
        _l_(353078)

        aux = _a_(353076, _n_(353075, "self", lambda: self), "branch")
        _l_(353077)
        return aux
try:
    from urllib.request import urlopen, Request
    _l_(353081)

except ImportError:
    pass
try:
    from io import StringIO
    _l_(353083)

except ImportError:
    pass
try:
    import csv
    _l_(353085)

except ImportError:
    pass

for row in _c_(353087, _n_(353086, "urlopen", lambda: urlopen), 'https://raw.githubusercontent.com/snarayanank2/indian_banks/dc7ac64137ecf24bfc564f3d6151331215cf4783/bank_branches.csv'):
    _l_(353101)

    _c_(353099, _a_(353090, _a_(353089, _n_(353088, "Branches", lambda: Branches), "objects"), "create"), ifsc=_n_(353091, "row", lambda: row)['ifsc'], bank_id=_n_(353092, "row", lambda: row)['bank_id'], branch=_n_(353093, "row", lambda: row)['branch'], address=_n_(353094, "row", lambda: row)['address'], city=_n_(353095, "row", lambda: row)['city'], district=_n_(353096, "row", lambda: row)['district'], state=_n_(353097, "row", lambda: row)['state'], bank_name=_n_(353098, "row", lambda: row)['bank_name'])
    _l_(353100)