# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72095878/typeerror-create-superuser-missing-2-required-positional-arguments
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib.auth.base_user import BaseUserManager
    _l_(634311)

except ImportError:
    pass

class UserManger(_n_(634312, "BaseUserManager", lambda: BaseUserManager)):
    _l_(634376)

    def create_user(self, email, first_name, last_name, password=None):
        _l_(634347)

        if not _n_(634313, "email", lambda: email):
            _l_(634317)

            raise _c_(634315, _n_(634314, "ValueError", lambda: ValueError), "Users must have an email address")
            _l_(634316)
        if not _n_(634318, "first_name", lambda: first_name) or _n_(634319, "last_name", lambda: last_name):
            _l_(634323)

            raise _c_(634321, _n_(634320, "ValueError", lambda: ValueError), "Users must have a first and last name")
            _l_(634322)

        user = _c_(634332, _a_(634325, _n_(634324, "self", lambda: self), "model"), email=_c_(634329, _a_(634327, _n_(634326, "self", lambda: self), "normalize_email"), _n_(634328, "email", lambda: email)),
            first_name=_n_(634330, "first_name", lambda: first_name),
            last_name=_n_(634331, "last_name", lambda: last_name),
        )
        _l_(634333)

        _c_(634337, _a_(634335, _n_(634334, "user", lambda: user), "set_password"), _n_(634336, "password", lambda: password))
        _l_(634338)
        _c_(634343, _a_(634340, _n_(634339, "user", lambda: user), "save"), using=_a_(634342, _n_(634341, "self", lambda: self), "_db"))
        _l_(634344)
        aux = _n_(634345, "user", lambda: user)
        _l_(634346)
        return aux

    def create_superuser(self, email,password, first_name, last_name):
        _l_(634375)

        user = _c_(634357, _a_(634349, _n_(634348, "self", lambda: self), "create_user"), email=_c_(634353, _a_(634351, _n_(634350, "self", lambda: self), "normalize_email"), _n_(634352, "email", lambda: email)),
            password=_n_(634354, "password", lambda: password),
            first_name=_n_(634355, "first_name", lambda: first_name),
            last_name=_n_(634356, "last_name", lambda: last_name),
        )
        _l_(634358)
        _c_(634363, _a_(634360, _n_(634359, "user", lambda: user), "set_password"), _a_(634362, _n_(634361, "user", lambda: user), "password"))
        _l_(634364)
        #user.is_staff = True
        _n_(634365, "user", lambda: user).is_superuser = True
        _l_(634366)
        #user.is_admin = True
        _c_(634371, _a_(634368, _n_(634367, "user", lambda: user), "save"), using=_a_(634370, _n_(634369, "self", lambda: self), "_db"))
        _l_(634372)
        aux = _n_(634373, "user", lambda: user)
        _l_(634374)
        return aux