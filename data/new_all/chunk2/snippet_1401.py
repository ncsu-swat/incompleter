# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64882685/typeerror-object-of-type-user-is-not-json-serializable-why-is-this-happening
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class UserCreateAPIView(_n_(460795, "ModelViewSet", lambda: ModelViewSet)):
    _l_(460802)

    queryset = _c_(460798, _a_(460797, _a_(460796, EndUser, "objects"), "all"))
    _l_(460799)
    serializer_class = NewUserSerializer
    _l_(460800)
    permission_classes = (AllowAny,)
    _l_(460801)