# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58761510/typeerror-get-object-takes-1-positional-argument-but-2-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class UserMobileViewSet(_a_(533649, _n_(533648, "generics", lambda: generics), "ListCreateAPIView")):
    _l_(533709)

    authentication_classes = (_a_(533650, authentication, "TokenAuthentication"),)
    _l_(533651)
    permission_classes = (_a_(533652, permissions, "IsAuthenticated"),)
    _l_(533653)
    queryset = _c_(533656, _a_(533655, _a_(533654, UserMobileDevice, "objects"), "all"))
    _l_(533657)
    serializer_class = UserMobileSerializer
    _l_(533658)

    def get_user(self, id):
        _l_(533670)

        try:
            _l_(533669)

            _c_(533663, _a_(533661, _a_(533660, _n_(533659, "UserMobileDevice", lambda: UserMobileDevice), "objects"), "get"), user=_n_(533662, "id", lambda: id))
            _l_(533664)
        except _a_(533666, _n_(533665, "User", lambda: User), "DoesNotExist"):
            _l_(533668)

            aux = None
            _l_(533667)
            return aux



    def create(self, request, *args, **kwargs):
        _l_(533708)

        myModel = None
        _l_(533671)
        id = _c_(533675, _a_(533674, _a_(533673, _n_(533672, "request", lambda: request), "data"), "get"), "user")  #id = 52 pk = 2
        _l_(533676)  #id = 52 pk = 2
        _c_(533679, _n_(533677, "print", lambda: print), _n_(533678, "id", lambda: id))
        _l_(533680)
        if _n_(533681, "id", lambda: id):
            _l_(533691)

            myModel=_c_(533685, _a_(533683, _n_(533682, "self", lambda: self), "get_user"), _n_(533684, "id", lambda: id))
            _l_(533686)
            _c_(533689, _n_(533687, "print", lambda: print), _n_(533688, "myModel", lambda: myModel))
            _l_(533690)
        if _n_(533692, "myModel", lambda: myModel):
            _l_(533707)

            aux = _c_(533698, _a_(533694, _n_(533693, "self", lambda: self), "update"), _n_(533695, "request", lambda: request), *_n_(533696, "args", lambda: args), **_n_(533697, "kwargs", lambda: kwargs))
            _l_(533699)
            return aux
        else:
            aux = _c_(533705, _a_(533701, _n_(533700, "self", lambda: self), "create"), _n_(533702, "request", lambda: request), *_n_(533703, "args", lambda: args), **_n_(533704, "kwargs", lambda: kwargs))
            _l_(533706)
            return aux