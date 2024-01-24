# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76454850/attributeerror-property-object-has-no-attribute-get-when-using-depends-in
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(448319, _a_(448318, _n_(448317, "app", lambda: app), "get"), "/")
async def home(user: _n_(448320, "Annotated", lambda: Annotated)[_n_(448321, "User", lambda: User), _c_(448326, _n_(448322, "Depends", lambda: Depends), _c_(448325, _n_(448323, "authenticate_request", lambda: authenticate_request), _n_(448324, "Request", lambda: Request)))]):
    _l_(448336)

    """
    status _summary_
    Returns status message if service is running
    """
    if _c_(448330, _n_(448327, "isinstance", lambda: isinstance), _n_(448328, "user", lambda: user), _n_(448329, "User", lambda: User)):
        _l_(448332)

        aux = {"Welcome, service is running ok!"}
        _l_(448331)
        return aux
    raise _c_(448334, _n_(448333, "HTTPException", lambda: HTTPException), status_code=401,
        detail="User not authorized!",
    )
    _l_(448335)