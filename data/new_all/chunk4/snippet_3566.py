# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72095878/typeerror-create-superuser-missing-2-required-positional-arguments
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(594378)

except ImportError:
    pass
try:
    from django.core.mail import send_mail
    _l_(594380)

except ImportError:
    pass
try:
    from distutils.command.upload import upload
    _l_(594382)

except ImportError:
    pass
try:
    from django.db import models
    _l_(594384)

except ImportError:
    pass
try:
    from django.contrib.auth.base_user import AbstractBaseUser
    _l_(594386)

except ImportError:
    pass
try:
    from django.contrib.auth.models import PermissionsMixin
    _l_(594388)

except ImportError:
    pass
try:
    from django.utils import timezone
    _l_(594390)

except ImportError:
    pass
try:
    from phonenumber_field.modelfields import PhoneNumberField
    _l_(594392)

except ImportError:
    pass
try:
    from .managers import UserManger
    _l_(594394)

except ImportError:
    pass

GENDER_MALE = "m"
_l_(594395)
GENDER_FEMALE = "f"
_l_(594396)
OTHER = "o"
_l_(594397)

GENDER_CHOICES = (
    (_n_(594398, "GENDER_MALE", lambda: GENDER_MALE), "Male"),
    (_n_(594399, "GENDER_FEMALE", lambda: GENDER_FEMALE), "Female"),
    (_n_(594400, "OTHER", lambda: OTHER), "Other"),
)
_l_(594401)


class User(_n_(594402, "AbstractBaseUser", lambda: AbstractBaseUser)):
    _l_(594489)


    email = _c_(594405, _a_(594404, _n_(594403, "models", lambda: models), "EmailField"), verbose_name='email address',
        max_length=255,
        unique=True,
    )
    _l_(594406)
    date_of_birth = _c_(594409, _a_(594408, _n_(594407, "models", lambda: models), "DateField"))
    _l_(594410)
    first_name = _c_(594413, _a_(594412, _n_(594411, "models", lambda: models), "CharField"), max_length=30, blank=True)
    _l_(594414)
    last_name = _c_(594417, _a_(594416, _n_(594415, "models", lambda: models), "CharField"), max_length=30, blank=True)
    _l_(594418)
    gender = _c_(594422, _a_(594420, _n_(594419, "models", lambda: models), "CharField"), max_length=1, choices=_n_(594421, "GENDER_CHOICES", lambda: GENDER_CHOICES), blank=True)
    _l_(594423)
    picture = _c_(594426, _a_(594425, _n_(594424, "models", lambda: models), "ImageField"), upload_to='images/users', null=True, verbose_name="")
    _l_(594427)
    is_active = _c_(594430, _a_(594429, _n_(594428, "models", lambda: models), "BooleanField"), default=True)
    _l_(594431)
    #is_staff = models.BooleanField(default=False)
    phone = _c_(594433, _n_(594432, "PhoneNumberField", lambda: PhoneNumberField))
    _l_(594434)
    is_admin = _c_(594437, _a_(594436, _n_(594435, "models", lambda: models), "BooleanField"), default=False)
    _l_(594438)
    #credits =models.PositiveIntegerField(default=100)
    linkedin_token = _c_(594441, _a_(594440, _n_(594439, "models", lambda: models), "TextField"), blank=True, default='')
    _l_(594442)
    expiry_date = _c_(594445, _a_(594444, _n_(594443, "models", lambda: models), "DateTimeField"), null=True, blank=True)
    _l_(594446)

    objects = _c_(594448, _n_(594447, "UserManger", lambda: UserManger))
    _l_(594449)

    USERNAME_FIELD = 'email'
    _l_(594450)
    REQUIRED_FIELDS = ['first_name' , 'last_name']
    _l_(594451)
    def get_full_name(self):
        _l_(594461)

        full_name = '%S %s' % (_a_(594453, _n_(594452, "self", lambda: self), "first_name"), _a_(594455, _n_(594454, "self", lambda: self), "last_name"))
        _l_(594456)
        aux = _c_(594459, _a_(594458, _n_(594457, "full_name", lambda: full_name), "strip"))
        _l_(594460)
        return aux

    def get_short_name(self):
        _l_(594465)

        aux = _a_(594463, _n_(594462, "self", lambda: self), "first_name")
        _l_(594464)
        return aux

    def __str__(self):
        _l_(594469)

        aux = _a_(594467, _n_(594466, "self", lambda: self), "email")
        _l_(594468)
        return aux

    def has_perm(self, prem, obj=None):
        _l_(594472)

        "Does the user have a specific permission?"
        _l_(594470)
        aux = True
        _l_(594471)
        return aux

    def has_module_perm(self, app_label):
        _l_(594475)

        "Does the user have permissions to view the app `app_label`?"
        _l_(594473)
        aux = True
        _l_(594474)
        return aux
    ''''
    @property
    def is_staff(self):
        "Is the user a member of staff"
        return self.is_admin'''
    _l_(594476)
    
    """@property
    def is_out_of_credits(self):
        "Is the user out of credits"
        return self.credits > 0
    @property
    def has_sufficient_credits(self,cost):
        return self.credits - cost >= 0
        """
    @_n_(594477, "property", lambda: property)
    def linkedin_signed_in(self):
        _l_(594488)

        aux = _c_(594481, _n_(594478, "bool", lambda: bool), _a_(594480, _n_(594479, "self", lambda: self), "linkedin_token")) and _a_(594483, _n_(594482, "self", lambda: self), "expiry_date") > _c_(594486, _a_(594485, _n_(594484, "timezone", lambda: timezone), "now"))
        _l_(594487)
        return aux