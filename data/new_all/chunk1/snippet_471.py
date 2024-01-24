# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68053973/typeerror-cannot-pickle-module-object-in-fastapi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from fastapi import APIRouter, HTTPException, status, Depends
    _l_(386080)

except ImportError:
    pass
try:
    from fastapi.security.oauth2 import OAuth2PasswordRequestForm
    _l_(386082)

except ImportError:
    pass
try:
    from ..modules import oauth_module
    _l_(386084)

except ImportError:
    pass
try:
    from ..models.user_model import User
    _l_(386086)

except ImportError:
    pass
try:
    from ..schemas import token_schema
    _l_(386088)

except ImportError:
    pass

router = _c_(386090, _n_(386089, "APIRouter", lambda: APIRouter), prefix="/auth",
    tags=["auth"],
)
_l_(386091)

...
_l_(386092)

@_c_(386095, _a_(386094, _n_(386093, "router", lambda: router), "get"), "/my_info")
async def read_user_info(current_user: _n_(386096, "User", lambda: User) = _c_(386100, _n_(386097, "Depends", lambda: Depends), _a_(386099, _n_(386098, "oauth_module", lambda: oauth_module), "get_current_active_user"))):
    _l_(386103)

    aux = _n_(386101, "current_user", lambda: current_user)
    _l_(386102)
    return aux