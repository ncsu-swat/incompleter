# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56044891/typeerror-module-object-is-not-callable-flask-jwt
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask_jwt_extended import (
        JWTManager, jwt_required, create_access_token, create_refresh_token, get_jwt_identity, jwt_refresh_token_required
    )
    _l_(524306)

except ImportError:
    pass

@_c_(524309, _a_(524308, _n_(524307, "app", lambda: app), "route"), '/api/users/validate', methods=['POST'])
def validate_user():
    _l_(524363)


    if not _a_(524311, _n_(524310, "request", lambda: request), "json"):
        _l_(524315)

        _c_(524313, _n_(524312, "abort", lambda: abort), 400)
        _l_(524314)

    data = _c_(524318, _a_(524317, _n_(524316, "request", lambda: request), "get_json"))
    _l_(524319)

    if ('id_token' not in _n_(524320, "data", lambda: data)):
        _l_(524324)

        _c_(524322, _n_(524321, "abort", lambda: abort), 400, "id_token must be a parameter in the JSON")
        _l_(524323)

    decoded_token = _c_(524328, _a_(524326, _n_(524325, "auth", lambda: auth), "verify_id_token"), _n_(524327, "data", lambda: data)['id_token'])
    _l_(524329)

    if ('uid' not in _n_(524330, "decoded_token", lambda: decoded_token)):
        _l_(524362)

        aux = _c_(524333, _a_(524332, _n_(524331, "json", lambda: json), "dumps"), {'verified': False}), 200
        _l_(524334)
        return aux
    else:
        user = _c_(524340, _a_(524338, _a_(524337, _a_(524336, _n_(524335, "mongo", lambda: mongo), "db"), "users"), "find_one"), {'_id': _n_(524339, "decoded_token", lambda: decoded_token)['uid']})
        _l_(524341)

        if _n_(524342, "user", lambda: user):
            _l_(524361)

            access_token = _c_(524345, _n_(524343, "create_access_token", lambda: create_access_token), identity=_n_(524344, "user", lambda: user)['_id'])
            _l_(524346)
            refresh_token = _c_(524349, _n_(524347, "create_refresh_token", lambda: create_refresh_token), identity=_n_(524348, "user", lambda: user)['_id'])
            _l_(524350)
            aux = _c_(524355, _a_(524352, _n_(524351, "json", lambda: json), "dumps"), {'verified': True, 'access_token': _n_(524353, "access_token", lambda: access_token), 'refresh_token': _n_(524354, "refresh_token", lambda: refresh_token)}), 200
            _l_(524356)
            return aux
        else:
            aux = _c_(524359, _a_(524358, _n_(524357, "json", lambda: json), "dumps"), {'verified': False, 'message': 'unable to locate user'}), 401
            _l_(524360)
            return aux