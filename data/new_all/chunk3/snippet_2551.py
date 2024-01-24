# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71877489/typeerror-object-of-type-httpresponseredirect-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class EntryLayerView(_a_(550622, _n_(550621, "generics", lambda: generics), "GenericAPIView")):
    _l_(550639)

    permission_classes = (_a_(550623, permissions, "IsAuthenticated"),)
    _l_(550624)

    def post(self, request, *args, **kwargs):
        _l_(550638)

        body = _a_(550626, _n_(550625, "request", lambda: request), "data")
        _l_(550627)
        response = _c_(550630, _n_(550628, "get_endpoint", lambda: get_endpoint), _n_(550629, "validated_body", lambda: validated_body)) #Don't worry about this line
        _l_(550631) #Don't worry about this line
        aux = _c_(550636, _n_(550632, "Response", lambda: Response), _n_(550633, "response", lambda: response), status=_a_(550635, _n_(550634, "status", lambda: status), "HTTP_200_OK"))
        _l_(550637)
        return aux


class startconversation(_a_(550641, _n_(550640, "generics", lambda: generics), "GenericAPIView")):
    _l_(550653)

    permission_classes = (_a_(550642, permissions, "AllowAny"),)
    _l_(550643)

    def post(self, request, *args, **kwargs):
        _l_(550652)

        _c_(550645, _n_(550644, "print", lambda: print), "I'm inside the view")
        _l_(550646)
        redirect = _c_(550650, _a_(550649, _a_(550648, _n_(550647, "request", lambda: request), "GET"), "get"), 'all the data')
        _l_(550651)