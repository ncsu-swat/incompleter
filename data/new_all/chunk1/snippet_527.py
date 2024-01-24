# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52675510/attributeerror-settings-object-has-no-attribute-auth-user-model-value-after
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class User(_n_(398769, "AbstractUser", lambda: AbstractUser)):
    _l_(398784)


    image = _c_(398771, _a_(398770, models, "ImageField"), upload_to=get_image_path, blank=True, null=True)
    _l_(398772)
    objects = _c_(398773, NewUserManager)
    _l_(398774)

    USERNAME_FIELD = 'username'
    _l_(398775)
    REQUIRED_FIELDS = ['email']
    _l_(398776)

    def __str__(self):
        _l_(398780)

        aux = _a_(398778, _n_(398777, "self", lambda: self), "email")
        _l_(398779)
        return aux

    class Meta(_a_(398781, AbstractUser, "Meta")):
        _l_(398783)

        swappable = 'stack.User'
        _l_(398782)