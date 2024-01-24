# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/19919285/nameerror-global-name-username-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(467101)

except ImportError:
    pass
try:
    from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
    _l_(467103)

except ImportError:
    pass
try:
    from django.utils.translation import ugettext_lazy as _
    _l_(467105)

except ImportError:
    pass
try:
    from django.utils import timezone
    _l_(467107)

except ImportError:
    pass
try:
    from django.core.mail import send_mail
    _l_(467109)

except ImportError:
    pass
try:
    from django.contrib.auth.signals import user_logged_in
    _l_(467111)

except ImportError:
    pass


def update_last_login(sender, user, **kwargs):
    _l_(467121)

    """
    A signal receiver which updates the last_login date for
    the user logging in.
    """
    _n_(467112, "user", lambda: user).last_login = _c_(467115, _a_(467114, _n_(467113, "timezone", lambda: timezone), "now"))
    _l_(467116)
    _c_(467119, _a_(467118, _n_(467117, "user", lambda: user), "save"), update_fields=['last_login'])
    _l_(467120)
_c_(467125, _a_(467123, _n_(467122, "user_logged_in", lambda: user_logged_in), "connect"), _n_(467124, "update_last_login", lambda: update_last_login))
_l_(467126)

class UserManager(_n_(467127, "BaseUserManager", lambda: BaseUserManager)):
    _l_(467183)


    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        _l_(467165)

        """
        Creates and saves a User with the given email and password.
        """
        now = _c_(467130, _a_(467129, _n_(467128, "timezone", lambda: timezone), "now"))
        _l_(467131)
        if not _n_(467132, "email", lambda: email):
            _l_(467136)

            raise _c_(467134, _n_(467133, "ValueError", lambda: ValueError), 'The given email must be set')
            _l_(467135)
        email = _c_(467140, _a_(467138, _n_(467137, "self", lambda: self), "normalize_email"), _n_(467139, "email", lambda: email))
        _l_(467141)
        user = _c_(467150, _a_(467143, _n_(467142, "self", lambda: self), "model"), email=_n_(467144, "email", lambda: email),
                          is_staff=_n_(467145, "is_staff", lambda: is_staff), is_active=True,
                          is_superuser=_n_(467146, "is_superuser", lambda: is_superuser), last_login=_n_(467147, "now", lambda: now),
                          date_joined=_n_(467148, "now", lambda: now), **_n_(467149, "extra_fields", lambda: extra_fields))
        _l_(467151)
        _c_(467155, _a_(467153, _n_(467152, "user", lambda: user), "set_password"), _n_(467154, "password", lambda: password))
        _l_(467156)
        _c_(467161, _a_(467158, _n_(467157, "user", lambda: user), "save"), using=_a_(467160, _n_(467159, "self", lambda: self), "_db"))
        _l_(467162)
        aux = _n_(467163, "user", lambda: user)
        _l_(467164)
        return aux

    def create_user(self, email, password=None, **extra_fields):
        _l_(467173)

        aux = _c_(467171, _a_(467167, _n_(467166, "self", lambda: self), "_create_user"), _n_(467168, "email", lambda: email), _n_(467169, "password", lambda: password), False, False,
                                 **_n_(467170, "extra_fields", lambda: extra_fields))
        _l_(467172)
        return aux

    def create_superuser(self, email, password, **extra_fields):
        _l_(467182)

        aux = _c_(467180, _a_(467175, _n_(467174, "self", lambda: self), "_create_user"), _n_(467176, "username", lambda: username), _n_(467177, "email", lambda: email), _n_(467178, "password", lambda: password), True, True,
                                 **_n_(467179, "extra_fields", lambda: extra_fields))
        _l_(467181)
        return aux

class User(_n_(467184, "AbstractBaseUser", lambda: AbstractBaseUser), _n_(467185, "PermissionsMixin", lambda: PermissionsMixin)):
    _l_(467260)

    email = _c_(467190, _a_(467187, _n_(467186, "models", lambda: models), "EmailField"), _c_(467189, _n_(467188, "_", lambda: _), 'email address'), max_length=254,
                              unique=True, db_index=True, blank=True)
    _l_(467191)
    is_staff = _c_(467198, _a_(467193, _n_(467192, "models", lambda: models), "BooleanField"), _c_(467195, _n_(467194, "_", lambda: _), 'staff status'), default=False,
        help_text=_c_(467197, _n_(467196, "_", lambda: _), 'Designates whether the user can log into this admin '
                    'site.'))
    _l_(467199)
    is_active = _c_(467206, _a_(467201, _n_(467200, "models", lambda: models), "BooleanField"), _c_(467203, _n_(467202, "_", lambda: _), 'active'), default=True,
        help_text=_c_(467205, _n_(467204, "_", lambda: _), 'Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    _l_(467207)
    date_joined = _c_(467214, _a_(467209, _n_(467208, "models", lambda: models), "DateTimeField"), _c_(467211, _n_(467210, "_", lambda: _), 'date joined'), default=_a_(467213, _n_(467212, "timezone", lambda: timezone), "now"))
    _l_(467215)

    objects = _c_(467217, _n_(467216, "UserManager", lambda: UserManager))
    _l_(467218)

    USERNAME_FIELD = 'email'
    _l_(467219)
    REQUIRED_FIELDS = []
    _l_(467220)

    class Meta:
        _l_(467227)

        verbose_name = _c_(467222, _n_(467221, "_", lambda: _), 'user')
        _l_(467223)
        verbose_name_plural = _c_(467225, _n_(467224, "_", lambda: _), 'users')
        _l_(467226)

    def get_full_name(self):
        _l_(467234)

        aux = _c_(467232, _n_(467228, "getattr", lambda: getattr), _n_(467229, "self", lambda: self), _a_(467231, _n_(467230, "self", lambda: self), "USERNAME_FIELD"))
        _l_(467233)
        return aux

    def get_short_name(self):
        _l_(467241)

        aux = _c_(467239, _n_(467235, "getattr", lambda: getattr), _n_(467236, "self", lambda: self), _a_(467238, _n_(467237, "self", lambda: self), "USERNAME_FIELD"))
        _l_(467240)
        return aux

    def email_user(self, subject, message, from_email=None, **kwargs):
        _l_(467251)

        """
        Sends an email to this User.
        """
        _c_(467249, _n_(467242, "send_mail", lambda: send_mail), _n_(467243, "subject", lambda: subject), _n_(467244, "message", lambda: message), _n_(467245, "from_email", lambda: from_email), [_a_(467247, _n_(467246, "self", lambda: self), "email")], **_n_(467248, "kwargs", lambda: kwargs))
        _l_(467250)

    def __str__(self):
        _l_(467255)

        aux = _a_(467253, _n_(467252, "self", lambda: self), "email")
        _l_(467254)
        return aux

    def __unicode__(self):
        _l_(467259)

        aux = _a_(467257, _n_(467256, "self", lambda: self), "email")
        _l_(467258)
        return aux