# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56214565/typeerror-object-of-type-user-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from rest_framework.views import APIView
    _l_(538323)

except ImportError:
    pass
try:
    from rest_framework.response import Response
    _l_(538325)

except ImportError:
    pass
try:
    import json
    _l_(538327)

except ImportError:
    pass

class MyView(_n_(538328, "APIView", lambda: APIView)):
    _l_(538358)

    try:
        from .serializers import MySerializer
        _l_(538330)

    except ImportError:
        pass
    try:
        from app.permissions import MyPermissionClass
        _l_(538332)

    except ImportError:
        pass
    try:
        from .models import MyModel
        _l_(538334)

    except ImportError:
        pass

    serializer_class = MySerializer
    _l_(538335)
    queryset = _c_(538338, _a_(538337, _a_(538336, MyModel, "objects"), "all"))
    _l_(538339)
    permission_classes = (MyPermissionClass,)
    _l_(538340)
    pagination_class = None
    _l_(538341)

    def get(self, request, *args, **kwargs):
        _l_(538357)

        data=_c_(538346, _n_(538342, "myfunction", lambda: myfunction), _n_(538343, "a", lambda: a),_n_(538344, "b", lambda: b),_n_(538345, "c", lambda: c))
        _l_(538347)
        # data={list}<class 'list'>: [<User: Negiiii | negiiii>, <User: Negiiii | negiiii>]
        data=_c_(538351, _a_(538349, _n_(538348, "json", lambda: json), "dumps"), _n_(538350, "data", lambda: data))
        _l_(538352)
        aux = _c_(538355, _n_(538353, "Response", lambda: Response), {"data":_n_(538354, "data", lambda: data)})
        _l_(538356)
        return aux