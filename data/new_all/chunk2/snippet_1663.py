# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65701682/django-models-in-admin-return-typeerror-bad-operand-type-for-unary-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib import admin
    _l_(475118)

except ImportError:
    pass
try:
    from .models import CurrencyManagementAssetsModel
    _l_(475120)

except ImportError:
    pass

_c_(475125, _a_(475123, _a_(475122, _n_(475121, "admin", lambda: admin), "site"), "register"), _n_(475124, "CurrencyManagementAssetsModel", lambda: CurrencyManagementAssetsModel))
_l_(475126)