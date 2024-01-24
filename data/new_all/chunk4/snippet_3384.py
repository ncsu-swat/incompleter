# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75031533/attributeerror-text-in-django
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.urls import path, include
    _l_(603075)

except ImportError:
    pass
try:
    from . import views
    _l_(603077)

except ImportError:
    pass

urlpatterns = [
    _c_(603081, _n_(603078, "path", lambda: path), '', _a_(603080, _n_(603079, "views", lambda: views), "chatbot_view"), name="chatbot")
]
_l_(603082)