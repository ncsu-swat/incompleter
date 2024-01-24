# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76454850/attributeerror-property-object-has-no-attribute-get-when-using-depends-in
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(470101, _a_(470100, _n_(470099, "app", lambda: app), "get"), "/")
async def home(request: _n_(470102, "Request", lambda: Request)):
    _l_(470116)

    """
    status _summary_
    Returns status message if service is running
    """
    user = _c_(470105, _n_(470103, "authenticate_request", lambda: authenticate_request), request=_n_(470104, "request", lambda: request))
    _l_(470106)
    if _c_(470110, _n_(470107, "isinstance", lambda: isinstance), _n_(470108, "user", lambda: user), _n_(470109, "User", lambda: User)):
        _l_(470112)

        aux = {"Welcome, service is running ok!"}
        _l_(470111)
        return aux
    raise _c_(470114, _n_(470113, "HTTPException", lambda: HTTPException), status_code=401,
        detail="User not authorized!",
    )
    _l_(470115)