# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69410573/nameerror-name-request-is-not-defined-error-after-instantiating-custom-oauth2
from __future__ import annotations
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(458684)
try:
    from typing import Optional
    _l_(458686)

except ImportError:
    pass
try:
    from fastapi import status
    _l_(458688)

except ImportError:
    pass
try:
    from starlette.requests import Request
    _l_(458690)

except ImportError:
    pass
try:
    from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
    _l_(458692)

except ImportError:
    pass
try:
    from fastapi.security import OAuth2
    _l_(458694)

except ImportError:
    pass
try:
    from fastapi.security.utils import get_authorization_scheme_param
    _l_(458696)

except ImportError:
    pass


class OAuth2PasswordBearerCookie(_n_(458697, "OAuth2", lambda: OAuth2)):
    _l_(458777)

    def __init__(
        self,
        tokenUrl: _n_(458698, "str", lambda: str),
        scheme_name: _n_(458699, "str", lambda: str) = None,
        scopes: _n_(458700, "dict", lambda: dict) = None,
        auto_error: _n_(458701, "bool", lambda: bool) = True,
    ):
        _l_(458717)

        if not _n_(458702, "scopes", lambda: scopes):
            _l_(458704)

            scopes = {}
            _l_(458703)
        flows = _c_(458708, _n_(458705, "OAuthFlowsModel", lambda: OAuthFlowsModel), password={"tokenUrl": _n_(458706, "tokenUrl", lambda: tokenUrl), "scopes": _n_(458707, "scopes", lambda: scopes)})
        _l_(458709)
        _c_(458715, _a_(458711, _n_(458710, "super", lambda: super)(), "__init__"), flows=_n_(458712, "flows", lambda: flows), scheme_name=_n_(458713, "scheme_name", lambda: scheme_name), auto_error=_n_(458714, "auto_error", lambda: auto_error))
        _l_(458716)

    async def __call__(self, request: _n_(458718, "Request", lambda: Request)) -> _n_(458719, "Optional", lambda: Optional)[_n_(458720, "str", lambda: str)]:
        _l_(458776)

        header_authorization: _n_(458721, "str", lambda: str) = _c_(458725, _a_(458724, _a_(458723, _n_(458722, "request", lambda: request), "headers"), "get"), "Authorization")
        _l_(458726)
        cookie_authorization: _n_(458727, "str", lambda: str) = _c_(458731, _a_(458730, _a_(458729, _n_(458728, "request", lambda: request), "cookies"), "get"), "Authorization")
        _l_(458732)

        header_scheme, header_param = _c_(458735, _n_(458733, "get_authorization_scheme_param", lambda: get_authorization_scheme_param), _n_(458734, "header_authorization", lambda: header_authorization)
        )
        _l_(458736)
        cookie_scheme, cookie_param = _c_(458739, _n_(458737, "get_authorization_scheme_param", lambda: get_authorization_scheme_param), _n_(458738, "cookie_authorization", lambda: cookie_authorization)
        )
        _l_(458740)

        if _c_(458743, _a_(458742, _n_(458741, "header_scheme", lambda: header_scheme), "lower")) == "bearer":
            _l_(458759)

            authorization = True
            _l_(458744)
            scheme = _n_(458745, "header_scheme", lambda: header_scheme)
            _l_(458746)
            param = _n_(458747, "header_param", lambda: header_param)
            _l_(458748)

        elif _c_(458751, _a_(458750, _n_(458749, "cookie_scheme", lambda: cookie_scheme), "lower")) == "bearer":
            _l_(458758)

            authorization = True
            _l_(458752)
            scheme = _n_(458753, "cookie_scheme", lambda: cookie_scheme)
            _l_(458754)
            param = _n_(458755, "cookie_param", lambda: cookie_param)
            _l_(458756)

        else:
            authorization = False
            _l_(458757)

        if not _n_(458760, "authorization", lambda: authorization) or _c_(458763, _a_(458762, _n_(458761, "scheme", lambda: scheme), "lower")) != "bearer":
            _l_(458773)

            if _a_(458765, _n_(458764, "self", lambda: self), "auto_error"):
                _l_(458772)

                raise _c_(458769, _n_(458766, "HTTPException", lambda: HTTPException), status_code=_a_(458768, _n_(458767, "status", lambda: status), "HTTP_401_UNAUTHORIZED"),
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
                _l_(458770)
            else:
                aux = None
                _l_(458771)
                return aux
        aux = _n_(458774, "param", lambda: param)
        _l_(458775)
        return aux