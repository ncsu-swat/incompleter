# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58784123/one-to-one-relationship-how-to-fix-got-attributeerror-when-attempting-to-get-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ProfileView(_n_(463212, "APIView", lambda: APIView)):
    _l_(463230)

    permission_classes = (_a_(463213, permissions, "IsAuthenticated"),)
    _l_(463214)

    def get(self, request):
        _l_(463229)

        user = _a_(463216, _n_(463215, "request", lambda: request), "user")
        _l_(463217)
        serializer = _c_(463220, _n_(463218, "ProfileSerializer", lambda: ProfileSerializer), _n_(463219, "user", lambda: user))
        _l_(463221)
        aux = _c_(463227, _n_(463222, "Response", lambda: Response), _a_(463224, _n_(463223, "serializer", lambda: serializer), "data"), status=_a_(463226, _n_(463225, "status", lambda: status), "HTTP_200_OK"))
        _l_(463228)

        return aux