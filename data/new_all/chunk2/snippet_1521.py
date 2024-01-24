# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46578472/attributeerror-customuser-object-has-no-attribute-first-name
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from time import timezone
    _l_(469904)

except ImportError:
    pass
try:
    from django.db import models
    _l_(469906)

except ImportError:
    pass
try:
    from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
    _l_(469908)

except ImportError:
    pass
try:
    from django.core.mail import send_mail
    _l_(469910)

except ImportError:
    pass
try:
    from django.utils.translation import ugettext_lazy as _
    _l_(469912)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(469914)

except ImportError:
    pass
now = _c_(469917, _a_(469916, _n_(469915, "datetime", lambda: datetime), "now"))
_l_(469918)

class CustomUserManager(_n_(469919, "BaseUserManager", lambda: BaseUserManager)):
    _l_(469969)

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        _l_(469952)

        """
        Creates and saves a User with the given email and password.
        """

        if not _n_(469920, "email", lambda: email):
            _l_(469924)

            raise _c_(469922, _n_(469921, "ValueError", lambda: ValueError), 'The given email must be set')
            _l_(469923)

        email = _c_(469928, _a_(469926, _n_(469925, "self", lambda: self), "normalize_email"), _n_(469927, "email", lambda: email))
        _l_(469929)
        user = _c_(469937, _a_(469931, _n_(469930, "self", lambda: self), "model"), email=_n_(469932, "email", lambda: email),
                          is_staff=_n_(469933, "is_staff", lambda: is_staff), is_active=True,
                          is_superuser=_n_(469934, "is_superuser", lambda: is_superuser), last_login=_n_(469935, "now", lambda: now),
                           **_n_(469936, "extra_fields", lambda: extra_fields))
        _l_(469938)
        _c_(469942, _a_(469940, _n_(469939, "user", lambda: user), "set_password"), _n_(469941, "password", lambda: password))
        _l_(469943)
        _c_(469948, _a_(469945, _n_(469944, "user", lambda: user), "save"), using=_a_(469947, _n_(469946, "self", lambda: self), "_db"))
        _l_(469949)
        aux = _n_(469950, "user", lambda: user)
        _l_(469951)
        return aux

    def create_user(self, email, password=None, **extra_fields):
        _l_(469960)

        aux = _c_(469958, _a_(469954, _n_(469953, "self", lambda: self), "_create_user"), _n_(469955, "email", lambda: email), _n_(469956, "password", lambda: password), False, False, **_n_(469957, "extra_fields", lambda: extra_fields))
        _l_(469959)
        return aux

    def create_superuser(self, email, password, **extra_fields):
        _l_(469968)

        aux = _c_(469966, _a_(469962, _n_(469961, "self", lambda: self), "_create_user"), _n_(469963, "email", lambda: email), _n_(469964, "password", lambda: password), True, True, **_n_(469965, "extra_fields", lambda: extra_fields))
        _l_(469967)
        return aux

class CustomUser(_n_(469970, "AbstractBaseUser", lambda: AbstractBaseUser), _n_(469971, "PermissionsMixin", lambda: PermissionsMixin)):
    _l_(470049)

    username    = _c_(469974, _a_(469973, _n_(469972, "models", lambda: models), "CharField"), max_length=254, unique=True)
    _l_(469975)
    email       = _c_(469978, _a_(469977, _n_(469976, "models", lambda: models), "EmailField"), blank=True, unique=True)
    _l_(469979)
    address1    = _c_(469982, _a_(469981, _n_(469980, "models", lambda: models), "CharField"), max_length=254, blank=True)
    _l_(469983)
    address2    = _c_(469986, _a_(469985, _n_(469984, "models", lambda: models), "CharField"), max_length=254, blank=True)
    _l_(469987)
    area_code   = _c_(469990, _a_(469989, _n_(469988, "models", lambda: models), "CharField"), max_length=20, blank=True)
    _l_(469991)
    country_code     = _c_(469994, _a_(469993, _n_(469992, "models", lambda: models), "CharField"), max_length=10, blank=True)
    _l_(469995)

    is_active    = _c_(469998, _a_(469997, _n_(469996, "models", lambda: models), "BooleanField"), default=True)
    _l_(469999)
    is_admin     = _c_(470002, _a_(470001, _n_(470000, "models", lambda: models), "BooleanField"), default=False)
    _l_(470003)
    is_staff     = _c_(470006, _a_(470005, _n_(470004, "models", lambda: models), "BooleanField"), default=False)
    _l_(470007)
    is_superuser = _c_(470010, _a_(470009, _n_(470008, "models", lambda: models), "BooleanField"), default=False)
    _l_(470011)

    USERNAME_FIELD = 'email'
    _l_(470012)
    REQUIRED_FIELDS = ['username', 'address1', 'address2', 'area_code', 'country_code']
    _l_(470013)

    objects = _c_(470015, _n_(470014, "CustomUserManager", lambda: CustomUserManager))
    _l_(470016)

    class Meta:
        _l_(470023)

        verbose_name = _c_(470018, _n_(470017, "_", lambda: _), 'user')
        _l_(470019)
        verbose_name_plural = _c_(470021, _n_(470020, "_", lambda: _), 'users')
        _l_(470022)

    def get_full_name(self):
        _l_(470033)

        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (_a_(470025, _n_(470024, "self", lambda: self), "first_name"), _a_(470027, _n_(470026, "self", lambda: self), "last_name"))
        _l_(470028)
        aux = _c_(470031, _a_(470030, _n_(470029, "full_name", lambda: full_name), "strip"))
        _l_(470032)
        return aux

    def get_short_name(self):
        _l_(470038)

        "Returns the short name for the user."
        _l_(470034)
        aux = _a_(470036, _n_(470035, "self", lambda: self), "first_name")
        _l_(470037)
        return aux

    def email_user(self, subject, message, from_email=None, **kwargs):
        _l_(470048)

        """
        Sends an email to this User.
        """
        _c_(470046, _n_(470039, "send_mail", lambda: send_mail), _n_(470040, "subject", lambda: subject), _n_(470041, "message", lambda: message), _n_(470042, "from_email", lambda: from_email), [_a_(470044, _n_(470043, "self", lambda: self), "email")], **_n_(470045, "kwargs", lambda: kwargs))
        _l_(470047)