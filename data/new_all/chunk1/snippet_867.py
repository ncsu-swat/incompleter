# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58683181/django-rest-framework-authentication-permissions-error-typeerror-str-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class DroneList(_a_(400702, _n_(400701, "generics", lambda: generics), "ListCreateAPIView")):
    _l_(400721)

    queryset = _c_(400705, _a_(400704, _a_(400703, Drone, "objects"), "all"))
    _l_(400706)
    serializer_class = DroneSerializer
    _l_(400707)
    name = 'drone-list'
    _l_(400708)
    permission_classes = (
        'permissions.IsAuthenticatedOrReadOnly',
        'custompermission.IsCurrentUserOwnerOrReadOnly',
    )
    _l_(400709)
    filterset_fields = (
        'name',
        'drone_category',
        'manufacturing_date',
        'has_it_competed',
    )
    _l_(400710)
    search_fileds = (
        'name',
    )
    _l_(400711)
    ordering_fields = (
        'name',
        'manufacturing_date',
    )
    _l_(400712)
    def perform_create(self, serializer):
        _l_(400720)

        _c_(400718, _a_(400714, _n_(400713, "serializer", lambda: serializer), "save"), owner=_a_(400717, _a_(400716, _n_(400715, "self", lambda: self), "request"), "user"))
        _l_(400719)

class DroneDetail(_a_(400723, _n_(400722, "generics", lambda: generics), "RetrieveUpdateDestroyAPIView")):
    _l_(400731)

    queryset = _c_(400726, _a_(400725, _a_(400724, Drone, "objects"), "all"))
    _l_(400727)
    serializer_class = DroneSerializer
    _l_(400728)
    name = 'drone-detail'
    _l_(400729)
    permission_classes = (
        'permissions.IsAuthenticatedOrReadOnly',
        'custompermission.IsCurrentUserOwnerOrReadOnly',
    )
    _l_(400730)