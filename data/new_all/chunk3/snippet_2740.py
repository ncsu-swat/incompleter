# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64730163/type-error-bool-object-is-not-callable
#views.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ProfileRetrieveUpdateView (_a_(547763, _n_(547762, "generics", lambda: generics), "RetrieveUpdateAPIView")):
    _l_(547771)

    queryset = _c_(547766, _a_(547765, _a_(547764, Profile, "objects"), "all"))
    _l_(547767)
    serializer_class = ProfileSerializer
    _l_(547768)
    permission_classes = (_n_(547769, "IsOwner", lambda: IsOwner),)
    _l_(547770)



#permissions
class IsOwner(_a_(547773, _n_(547772, "permissions", lambda: permissions), "BasePermission")):
    _l_(547788)

    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):
        _l_(547781)

        aux = _a_(547775, _n_(547774, "request", lambda: request), "user") and _c_(547779, _a_(547778, _a_(547777, _n_(547776, "request", lambda: request), "user"), "is_authenticated"))
        _l_(547780)
        return aux

    def has_object_permission(self, request, view, obj):
        _l_(547787)

        aux = _a_(547783, _n_(547782, "obj", lambda: obj), "user") == _a_(547785, _n_(547784, "request", lambda: request), "user")
        _l_(547786)
        return aux