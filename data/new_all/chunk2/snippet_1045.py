# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50557668/django-typeerror-at-admin-login-has-module-perms-takes-2-positional-argume
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(447083)

except ImportError:
    pass
try:
    from django.contrib.auth.models import AbstractUser
    _l_(447085)

except ImportError:
    pass

# Create your models here.

class User(_n_(447086, "AbstractUser", lambda: AbstractUser)):
    _l_(447095)

    email = _c_(447089, _a_(447088, _n_(447087, "models", lambda: models), "EmailField"), verbose_name='email',
                              unique=True, error_messages={'unique': 'Email is already occupied'})
    _l_(447090)

    class Meta(_a_(447092, _n_(447091, "AbstractUser", lambda: AbstractUser), "Meta")):
        _l_(447094)

        pass
        _l_(447093)