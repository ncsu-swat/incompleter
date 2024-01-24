# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57662873/filenotfounderror-winerror-3-the-system-cannot-find-the-path-specified
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from rest_framework import routers
    _l_(398896)

except ImportError:
    pass
try:
    from .viewsets import NoteViewSet
    _l_(398898)

except ImportError:
    pass

router = _c_(398901, _a_(398900, _n_(398899, "routers", lambda: routers), "SimpleRouter"))
_l_(398902)
_c_(398906, _a_(398904, _n_(398903, "router", lambda: router), "register"), 'notes', _n_(398905, "NoteViewSet", lambda: NoteViewSet))
_l_(398907)

urlpatterns = _a_(398909, _n_(398908, "router", lambda: router), "urls")
_l_(398910)