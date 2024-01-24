# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69555882/type-error-init-requires-1-positional-argument-yet-2-are-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class User(_n_(617337, "AbstractUser", lambda: AbstractUser)):
    _l_(617347)

    is_moderator = _c_(617339, _a_(617338, models, "BooleanField"), default = False)
    _l_(617340)
    about = _c_(617342, _a_(617341, models, "TextField"), blank = True, null = True)
    _l_(617343)
    notifications = _c_(617345, _a_(617344, models, "ManyToManyField"), Notification, related_name = 
    'notifications_user', blank = True)
    _l_(617346)