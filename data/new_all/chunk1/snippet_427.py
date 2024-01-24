# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47784216/django-rest-framework-attributeerror-function-object-has-no-attribute-model
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from rest_framework.viewsets import ModelViewSet
    _l_(406032)

except ImportError:
    pass
try:
    from developers.models import Developers
    _l_(406034)

except ImportError:
    pass
try:
    from .serializers import DevSerializer
    _l_(406036)

except ImportError:
    pass


class DevViewSet(_n_(406037, "ModelViewSet", lambda: ModelViewSet)):
    _l_(406044)

    queryset = _a_(406040, _a_(406039, _n_(406038, "Developers", lambda: Developers), "objects"), "all")
    _l_(406041)
    serializer_class = _n_(406042, "DevSerializer", lambda: DevSerializer)
    _l_(406043)