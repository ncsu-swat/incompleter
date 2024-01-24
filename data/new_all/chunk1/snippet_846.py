# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63101250/i-am-getting-an-attribute-error-while-trying-to-build-a-user-registration-form-u
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(406275)

except ImportError:
    pass
try:
    from django.contrib.auth.models import User
    _l_(406277)

except ImportError:
    pass
# Create your models here.

class UserProfileInfo(_a_(406279, _n_(406278, "models", lambda: models), "Model")):
    _l_(406300)

    user = _c_(406285, _a_(406281, _n_(406280, "models", lambda: models), "OneToOneField"), _n_(406282, "User", lambda: User),on_delete=_a_(406284, _n_(406283, "models", lambda: models), "CASCADE"))
    _l_(406286)

    # additional
    portfolio_site = _c_(406289, _a_(406288, _n_(406287, "models", lambda: models), "URLField"), blank=True)
    _l_(406290)

    profile_pic = _c_(406293, _a_(406292, _n_(406291, "models", lambda: models), "ImageField"), upload_to='profile_pics',blank=True)
    _l_(406294)

    def __str__(self):
        _l_(406299)

        aux = _a_(406297, _a_(406296, _n_(406295, "self", lambda: self), "user"), "username")
        _l_(406298)
        return aux