# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77422709/django-attributeerror-type-object-has-no-attribute-meta
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(616696)

except ImportError:
    pass


class AppUserManager(_n_(616697, "BaseUserManager", lambda: BaseUserManager)):
    _l_(616773)


    def _create_user(self, email, password, **extra_fields):
        _l_(616727)

        """
        Creates and saves a User with the given email and password.
        """
        if not _n_(616698, "email", lambda: email):
            _l_(616702)

            raise _c_(616700, _n_(616699, "ValueError", lambda: ValueError), 'The given email must be set')
            _l_(616701)
        email = _c_(616706, _a_(616704, _n_(616703, "self", lambda: self), "normalize_email"), _n_(616705, "email", lambda: email))
        _l_(616707)
        user = _c_(616712, _a_(616709, _n_(616708, "self", lambda: self), "model"), email=_n_(616710, "email", lambda: email), **_n_(616711, "extra_fields", lambda: extra_fields))
        _l_(616713)
        _c_(616717, _a_(616715, _n_(616714, "user", lambda: user), "set_password"), _n_(616716, "password", lambda: password))
        _l_(616718)
        _c_(616723, _a_(616720, _n_(616719, "user", lambda: user), "save"), using=_a_(616722, _n_(616721, "self", lambda: self), "_db"))
        _l_(616724)
        aux = _n_(616725, "user", lambda: user)
        _l_(616726)
        return aux

    def create_user(self, email, password=None, **extra_fields):
        _l_(616739)

        _c_(616730, _a_(616729, _n_(616728, "extra_fields", lambda: extra_fields), "setdefault"), 'is_superuser', False)
        _l_(616731)
        aux = _c_(616737, _a_(616733, _n_(616732, "self", lambda: self), "_create_user"), _n_(616734, "email", lambda: email), _n_(616735, "password", lambda: password), **_n_(616736, "extra_fields", lambda: extra_fields))
        _l_(616738)
        return aux

    def create_superuser(self, email, password, **extra_fields):
        _l_(616770)


        _c_(616742, _a_(616741, _n_(616740, "extra_fields", lambda: extra_fields), "setdefault"), 'is_superuser', True)
        _l_(616743)
        _c_(616746, _a_(616745, _n_(616744, "extra_fields", lambda: extra_fields), "setdefault"), 'is_staff', True)
        _l_(616747)
        _c_(616750, _a_(616749, _n_(616748, "extra_fields", lambda: extra_fields), "setdefault"), 'is_active', True)
        _l_(616751)

        _c_(616754, _a_(616753, _n_(616752, "extra_fields", lambda: extra_fields), "pop"), 'tag')
        _l_(616755)
        if _c_(616758, _a_(616757, _n_(616756, "extra_fields", lambda: extra_fields), "get"), 'is_superuser') is not True:
            _l_(616762)

            raise _c_(616760, _n_(616759, "ValueError", lambda: ValueError), 'Superuser must have is_superuser=True.')
            _l_(616761)
        aux = _c_(616768, _a_(616764, _n_(616763, "self", lambda: self), "_create_user"), _n_(616765, "email", lambda: email), _n_(616766, "password", lambda: password), **_n_(616767, "extra_fields", lambda: extra_fields))
        _l_(616769)

        return aux
    class Meta:
        _l_(616772)

        db_table = 'app_user_manager'
        _l_(616771)