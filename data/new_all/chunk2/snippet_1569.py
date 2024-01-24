# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76454850/attributeerror-property-object-has-no-attribute-get-when-using-depends-in
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def authenticate_request(request: _n_(438795, "Request", lambda: Request)) -> _n_(438796, "User", lambda: User):
    _l_(438840)

    cookie1 = _c_(438800, _a_(438799, _a_(438798, _n_(438797, "request", lambda: request), "cookies"), "get"), "x")
    _l_(438801)
    cookie2 = _c_(438805, _a_(438804, _a_(438803, _n_(438802, "request", lambda: request), "cookies"), "get"), "y")
    _l_(438806)
    if _n_(438807, "cookie1", lambda: cookie1) is not None and _n_(438808, "cookie2", lambda: cookie2) is not None:
        _l_(438833)

        tenant = _c_(438811, _n_(438809, "get_tenant", lambda: get_tenant), _n_(438810, "request", lambda: request))
        _l_(438812)
        if user := _c_(438817, _n_(438813, "authenticate_cookies", lambda: authenticate_cookies), _n_(438814, "cookie1", lambda: cookie1), _n_(438815, "cookie2", lambda: cookie2), _n_(438816, "tenant", lambda: tenant)):
            _l_(438832)

            if not _c_(438822, _a_(438819, _n_(438818, "tenant", lambda: tenant), "startswith"), _a_(438821, _n_(438820, "user", lambda: user), "tenant")):
                _l_(438829)

                _c_(438824, _n_(438823, "print", lambda: print), "Unauthorized: Token hostname mismatch")
                _l_(438825)
                raise _c_(438827, _n_(438826, "Exception", lambda: Exception), "Token hostname mismatch")
                _l_(438828)
            aux = _n_(438830, "user", lambda: user)
            _l_(438831)
            return aux
    _c_(438835, _n_(438834, "print", lambda: print), "Unauthorized: please login")
    _l_(438836)
    raise _c_(438838, _n_(438837, "HTTPException", lambda: HTTPException), status_code=401, detail="Unauthorized: please login")
    _l_(438839)