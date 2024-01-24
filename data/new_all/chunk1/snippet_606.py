# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71743807/typeerror-reverse-takes-exactly-2-arguments-1-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.urls import path
    _l_(387514)

except ImportError:
    pass
try:
    from . import views
    _l_(387516)

except ImportError:
    pass

urlpatterns = [
    _c_(387522, _n_(387517, "path", lambda: path), "api/v2/app/nextdialog", _c_(387521, _a_(387520, _a_(387519, _n_(387518, "views", lambda: views), "NextDialog"), "as_view")), name="app-next-dialog"),
]
_l_(387523)