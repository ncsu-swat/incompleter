# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62757155/typeerror-field-id-expected-a-number-but-got-user
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib import admin
    _l_(653991)

except ImportError:
    pass
try:
    from .models import BlogPost
    _l_(653993)

except ImportError:
    pass
# Register your models here.
_c_(653998, _a_(653996, _a_(653995, _n_(653994, "admin", lambda: admin), "site"), "register"), _n_(653997, "BlogPost", lambda: BlogPost))
_l_(653999)