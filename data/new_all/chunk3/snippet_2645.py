# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68055130/attributeerror-at-akolaprofile-myregistration-object-has-no-attribute-get
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(545948)

except ImportError:
    pass
try:
    from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
    _l_(545950)

except ImportError:
    pass
try:
    from django.utils import timezone
    _l_(545952)

except ImportError:
    pass
try:
    from .manager import FirstManager
    _l_(545954)

except ImportError:
    pass

class MyRegistration(_n_(545955, "AbstractBaseUser", lambda: AbstractBaseUser), _n_(545956, "PermissionsMixin", lambda: PermissionsMixin)):
    _l_(546009)

    location_list=[
        ('Solapur', 'Solapur'),
        ('Latur', 'Latur'),
        ('Dhule', 'Dhule'),
        ('Akola', 'Akola'),
        ('Nashik', 'Nashik')
        ]
    _l_(545957)
    username=_c_(545960, _a_(545959, _n_(545958, "models", lambda: models), "CharField"), max_length=10, unique=True)
    _l_(545961)
    email=_c_(545964, _a_(545963, _n_(545962, "models", lambda: models), "EmailField"), unique=True)
    _l_(545965)
    first_name=_c_(545968, _a_(545967, _n_(545966, "models", lambda: models), "CharField"), max_length=150)
    _l_(545969)
    last_name=_c_(545972, _a_(545971, _n_(545970, "models", lambda: models), "CharField"), max_length=150)
    _l_(545973)
    location=_c_(545976, _a_(545975, _n_(545974, "models", lambda: models), "CharField"), max_length=10, choices=location_list, default='Latur')
    _l_(545977)
    designation=_c_(545980, _a_(545979, _n_(545978, "models", lambda: models), "CharField"), max_length=70)
    _l_(545981)
    is_active=_c_(545984, _a_(545983, _n_(545982, "models", lambda: models), "BooleanField"), default=False)
    _l_(545985)
    is_staff=_c_(545988, _a_(545987, _n_(545986, "models", lambda: models), "BooleanField"), default=False)
    _l_(545989)
    start_date=_c_(545994, _a_(545991, _n_(545990, "models", lambda: models), "DateTimeField"), default=_a_(545993, _n_(545992, "timezone", lambda: timezone), "now"))
    _l_(545995)
    last_login=_c_(545998, _a_(545997, _n_(545996, "models", lambda: models), "DateTimeField"), null=True)
    _l_(545999)


    USERNAME_FIELD='username'
    _l_(546000)
    REQUIRED_FIELDS=['email', 'first_name', 'last_name', 'location', 'designation']
    _l_(546001)
    objects=_c_(546003, _n_(546002, "FirstManager", lambda: FirstManager))
    _l_(546004)
    def __str__(self):
        _l_(546008)

        aux = _a_(546006, _n_(546005, "self", lambda: self), "username")
        _l_(546007)
        return aux