# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58603924/attributeerror-object-has-no-attribute-user-loader
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask_login import UserMixin, LoginManager
    _l_(455321)

except ImportError:
    pass
try:
    from flaskapp import db, login_manager
    _l_(455323)

except ImportError:
    pass




@_a_(455325, _n_(455324, "login_manager", lambda: login_manager), "user_loader")
def get_user(user):
    _l_(455333)

    try:
        _l_(455332)

        aux = _c_(455328, _n_(455326, "get_id", lambda: get_id), _n_(455327, "user", lambda: user))
        _l_(455329)
        return aux
    except:
        _l_(455331)

        aux = None
        _l_(455330)
        return aux


class User(_a_(455335, _n_(455334, "db", lambda: db), "Model"),_n_(455336, "UserMixin", lambda: UserMixin)):
    _l_(455390)

    id          =_c_(455341, _a_(455338, _n_(455337, "db", lambda: db), "Column"), _a_(455340, _n_(455339, "db", lambda: db), "Integer"), primary_key=True)
    _l_(455342)
    username    =_c_(455348, _a_(455344, _n_(455343, "db", lambda: db), "Column"), _c_(455347, _a_(455346, _n_(455345, "db", lambda: db), "String"), 20),unique=True, nullable=False)
    _l_(455349)
    email       =_c_(455355, _a_(455351, _n_(455350, "db", lambda: db), "Column"), _c_(455354, _a_(455353, _n_(455352, "db", lambda: db), "String"), 120), unique=True, nullable=False)
    _l_(455356)
    password    =_c_(455362, _a_(455358, _n_(455357, "db", lambda: db), "Column"), _c_(455361, _a_(455360, _n_(455359, "db", lambda: db), "String"), 60), nullable=False)
    _l_(455363)
    powerlevel  =_c_(455368, _a_(455365, _n_(455364, "db", lambda: db), "Column"), _a_(455367, _n_(455366, "db", lambda: db), "Integer"), nullable=False)
    _l_(455369)

    def is_authenticated(self):
        _l_(455371)

        aux = True
        _l_(455370)
        return aux

    def is_active(self):
        _l_(455373)

        aux = True
        _l_(455372)
        return aux

    def is_anonymous(self):
        _l_(455375)

        aux = False
        _l_(455374)
        return aux

    def get_id(self):
        _l_(455381)

        aux = _c_(455379, _n_(455376, "int", lambda: int), _a_(455378, _n_(455377, "self", lambda: self), "id"))
        _l_(455380)
        return aux

    def __repr__(self):
        _l_(455389)

        aux = f"User('{_a_(455383, _n_(455382, 'self', lambda: self), 'username')}', '{_a_(455385, _n_(455384, 'self', lambda: self), 'email')}', '{_a_(455387, _n_(455386, 'self', lambda: self), 'powerlevel')}')"
        _l_(455388)
        return aux