# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58188060/attributeerror-module-calc-views-has-no-attribute-home
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.urls import path
    _l_(534238)

except ImportError:
    pass
try:
    from . import views
    _l_(534240)

except ImportError:
    pass

urlpatterns = [
    _c_(534244, _n_(534241, "path", lambda: path), '',_a_(534243, _n_(534242, "views", lambda: views), "home"), name='home')
]
_l_(534245)