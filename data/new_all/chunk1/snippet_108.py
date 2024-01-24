# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49474632/typeerror-create-superuser-missing-1-required-positional-argument-profile-p
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(393558)

except ImportError:
    pass
try:
    from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
    _l_(393560)

except ImportError:
    pass


class UserManager(_n_(393561, "BaseUserManager", lambda: BaseUserManager)):
    _l_(393641)

    def create_user(self, email, full_name, profile_picture=None, gender=None, password=None, is_admin=False, is_staff=False, is_active=True):
        _l_(393616)

        if not _n_(393562, "email", lambda: email):
            _l_(393566)

            raise _c_(393564, _n_(393563, "ValueError", lambda: ValueError), "User must have an email")
            _l_(393565)
        if not _n_(393567, "password", lambda: password):
            _l_(393571)

            raise _c_(393569, _n_(393568, "ValueError", lambda: ValueError), "User must have a password")
            _l_(393570)
        if not _n_(393572, "full_name", lambda: full_name):
            _l_(393576)

            raise _c_(393574, _n_(393573, "ValueError", lambda: ValueError), "User must have a full name")
            _l_(393575)

        user = _c_(393583, _a_(393578, _n_(393577, "self", lambda: self), "model"), email=_c_(393582, _a_(393580, _n_(393579, "self", lambda: self), "normalize_email"), _n_(393581, "email", lambda: email))
        )
        _l_(393584)
        _n_(393585, "user", lambda: user).full_name = _n_(393586, "full_name", lambda: full_name)
        _l_(393587)
        _c_(393591, _a_(393589, _n_(393588, "user", lambda: user), "set_password"), _n_(393590, "password", lambda: password))  # change password to hash
        _l_(393592)  # change password to hash
        # user.profile_picture = profile_picture
        _n_(393593, "user", lambda: user).gender = _n_(393594, "gender", lambda: gender)
        _l_(393595)
        _n_(393596, "user", lambda: user).admin = _n_(393597, "is_admin", lambda: is_admin)
        _l_(393598)
        _n_(393599, "user", lambda: user).profile_picture = _n_(393600, "profile_picture", lambda: profile_picture)
        _l_(393601)
        _n_(393602, "user", lambda: user).staff = _n_(393603, "is_staff", lambda: is_staff)
        _l_(393604)
        _n_(393605, "user", lambda: user).active = _n_(393606, "is_active", lambda: is_active)
        _l_(393607)
        _c_(393612, _a_(393609, _n_(393608, "user", lambda: user), "save"), using=_a_(393611, _n_(393610, "self", lambda: self), "_db"))
        _l_(393613)
        aux = _n_(393614, "user", lambda: user)
        _l_(393615)
        return aux

    def create_staffuser(self, email, profile_picture, gender, full_name, password=None):
        _l_(393628)

        user = _c_(393624, _a_(393618, _n_(393617, "self", lambda: self), "create_user"), _n_(393619, "email", lambda: email),
            _n_(393620, "full_name", lambda: full_name),
            _n_(393621, "profile_picture", lambda: profile_picture),
            _n_(393622, "gender", lambda: gender),
            password=_n_(393623, "password", lambda: password),
            is_staff=True,
        )
        _l_(393625)
        aux = _n_(393626, "user", lambda: user)
        _l_(393627)
        return aux

    def create_superuser(self, email, profile_picture, gender, full_name, password=None):
        _l_(393640)

        user = _c_(393636, _a_(393630, _n_(393629, "self", lambda: self), "create_user"), _n_(393631, "email", lambda: email),
            _n_(393632, "full_name", lambda: full_name),
            _n_(393633, "profile_picture", lambda: profile_picture),
            _n_(393634, "gender", lambda: gender),
            password=_n_(393635, "password", lambda: password),
            is_staff=True,
            is_admin=True,
        )
        _l_(393637)
        aux = _n_(393638, "user", lambda: user)
        _l_(393639)
        return aux


class User(_n_(393642, "AbstractBaseUser", lambda: AbstractBaseUser)):
    _l_(393713)

    username = _c_(393645, _a_(393644, _n_(393643, "models", lambda: models), "CharField"), max_length=255)
    _l_(393646)
    full_name = _c_(393649, _a_(393648, _n_(393647, "models", lambda: models), "CharField"), max_length=255)
    _l_(393650)
    email = _c_(393653, _a_(393652, _n_(393651, "models", lambda: models), "EmailField"), max_length=255, unique=True,)
    _l_(393654)
    profile_picture = _c_(393657, _a_(393656, _n_(393655, "models", lambda: models), "ImageField"), upload_to='user_data/profile_picture', null=True, blank=True)
    _l_(393658)
    gender = _c_(393661, _a_(393660, _n_(393659, "models", lambda: models), "CharField"), max_length=255, blank=True, default='rather_not_say')
    _l_(393662)
    active = _c_(393665, _a_(393664, _n_(393663, "models", lambda: models), "BooleanField"), default=True)
    _l_(393666)
    staff = _c_(393669, _a_(393668, _n_(393667, "models", lambda: models), "BooleanField"), default=False)  # a admin user; non super-user
    _l_(393670)  # a admin user; non super-user
    admin = _c_(393673, _a_(393672, _n_(393671, "models", lambda: models), "BooleanField"), default=False)  # a superuser
    _l_(393674)  # a superuser
    # notice the absence of a "Password field", that's built in.

    USERNAME_FIELD = 'email'
    _l_(393675)
    REQUIRED_FIELDS = ['full_name', 'gender']  # Email & Password are required by default.
    _l_(393676)  # Email & Password are required by default.

    objects = _c_(393678, _n_(393677, "UserManager", lambda: UserManager))
    _l_(393679)

    def get_full_name(self):
        _l_(393683)

        aux = _a_(393681, _n_(393680, "self", lambda: self), "email")
        _l_(393682)
        # The user is identified by their email address
        return aux

    def get_short_name(self):
        _l_(393687)

        aux = _a_(393685, _n_(393684, "self", lambda: self), "email")
        _l_(393686)
        # The user is identified by their email address
        return aux

    def __str__(self):
        _l_(393691)

        aux = _a_(393689, _n_(393688, "self", lambda: self), "email")
        _l_(393690)
        return aux

    @_n_(393692, "staticmethod", lambda: staticmethod)
    def has_perm(perm, obj=None):
        _l_(393694)

        aux = True
        _l_(393693)
         # "Does the user have a specific permission?"
         # Simplest possible answer: Yes, always
        return aux

    @_n_(393695, "staticmethod", lambda: staticmethod)
    def has_module_perms(app_label):
        _l_(393697)

        aux = True
        _l_(393696)
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return aux

    @_n_(393698, "property", lambda: property)
    def is_staff(self):
        _l_(393702)

        aux = _a_(393700, _n_(393699, "self", lambda: self), "staff")
        _l_(393701)
        # "Is the user a member of staff?"
        return aux

    @_n_(393703, "property", lambda: property)
    def is_admin(self):
        _l_(393707)

        aux = _a_(393705, _n_(393704, "self", lambda: self), "admin")
        _l_(393706)
        # "Is the user a admin member?"
        return aux

    @_n_(393708, "property", lambda: property)
    def is_active(self):
        _l_(393712)

        aux = _a_(393710, _n_(393709, "self", lambda: self), "active")
        _l_(393711)
        # "Is the user active?"
        return aux