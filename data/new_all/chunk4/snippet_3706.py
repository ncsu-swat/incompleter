# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69555882/type-error-init-requires-1-positional-argument-yet-2-are-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class User(_n_(635447, "AbstractUser", lambda: AbstractUser)):
    _l_(635457)

    is_moderator = _c_(635449, _a_(635448, models, "BooleanField"), default = False)
    _l_(635450)
    about = _c_(635452, _a_(635451, models, "TextField"), blank = True, null = True)
    _l_(635453)
    notifications = _c_(635455, _a_(635454, models, "ManyToManyField"), Notification, related_name = 
    'notifications_user', blank = True)
    _l_(635456)