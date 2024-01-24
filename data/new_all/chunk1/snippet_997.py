# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56637422/why-is-user-query-triggering-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class CustomUser(_n_(385017, "AbstractUser", lambda: AbstractUser)):
    _l_(385038)

    username = _c_(385019, _a_(385018, models, "CharField"), max_length=11, blank=True, default= 
     'newUser', verbose_name="User Group")
    _l_(385020)
    email = _c_(385023, _a_(385021, models, "EmailField"), _c_(385022, _, 'email address'), unique=True)
    _l_(385024)

    USERNAME_FIELD = 'email'
    _l_(385025)
    REQUIRED_FIELDS = []
    _l_(385026)

    objects = CustomUserManager
    _l_(385027)

    # add additional fields in here
    display_name = _c_(385029, _a_(385028, models, "SlugField"), max_length=50, unique=True)
    _l_(385030)
    phone = _c_(385032, _a_(385031, models, "CharField"), max_length=14, blank=True, help_text="XXX-XXX-XXXX")
    _l_(385033)

    def __str__(self):
        _l_(385037)

        aux = _a_(385035, _n_(385034, "self", lambda: self), "display_name")
        _l_(385036)
        return aux