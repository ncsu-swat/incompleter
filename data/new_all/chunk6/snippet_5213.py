# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59291245/flask-login-attributeerror-int-object-has-no-attribute-is-authenticated
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class UserData(_n_(355028, "UserMixin", lambda: UserMixin)):
    _l_(355068)

    def __init__(self, username, password):
        _l_(355037)

        _n_(355029, "self", lambda: self).username = _n_(355030, "username", lambda: username)
        _l_(355031)
        _n_(355032, "self", lambda: self).password = _n_(355033, "password", lambda: password)
        _l_(355034)
        _n_(355035, "self", lambda: self)._authenticated = False
        _l_(355036)

    def is_authenticated(self):
        _l_(355041)

        aux = _a_(355039, _n_(355038, "self", lambda: self), "_authenticated")
        _l_(355040)
        return aux

    def is_active(self):
        _l_(355043)

        aux = True
        _l_(355042)
        return aux
        # return true if user is activte and authenticated

    def is_annonymous(self):
        _l_(355045)

        aux = False
        _l_(355044)
        return aux

    def get_id(self):
        _l_(355067)

        global connection
        _l_(355046)
        user_id = _c_(355051, _n_(355047, "get_user_id", lambda: get_user_id), _a_(355049, _n_(355048, "self", lambda: self), "username"), _n_(355050, "connection", lambda: connection))
        _l_(355052)
        unicode_user_id = _c_(355055, _n_(355053, "load_user", lambda: load_user), _n_(355054, "user_id", lambda: user_id))
        _l_(355056)
        if _n_(355057, "unicode_user_id", lambda: unicode_user_id) != 0:
            _l_(355060)

            _n_(355058, "self", lambda: self)._authenticated = True
            _l_(355059)

        _c_(355063, _n_(355061, "print", lambda: print), "userid:" , _n_(355062, "unicode_user_id", lambda: unicode_user_id))
        _l_(355064)
        aux = _n_(355065, "unicode_user_id", lambda: unicode_user_id)
        _l_(355066)
        return aux