# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58784123/one-to-one-relationship-how-to-fix-got-attributeerror-when-attempting-to-get-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class MyUser(_n_(427740, "AbstractBaseUser", lambda: AbstractBaseUser)):
    _l_(427771)

    username = _c_(427742, _a_(427741, models, "CharField"), max_length=300,
        unique=True
    )
    _l_(427743)
    email = _c_(427745, _a_(427744, models, "EmailField"), max_length=255,
        unique=True,
        verbose_name='email address'
    )
    _l_(427746)
    is_admin = _c_(427748, _a_(427747, models, "BooleanField"), default=False)
    _l_(427749)
    is_staff = _c_(427751, _a_(427750, models, "BooleanField"), default=False)
    _l_(427752)
    is_student = _c_(427754, _a_(427753, models, "BooleanField"), default=False)
    _l_(427755)
    is_teacher = _c_(427757, _a_(427756, models, "BooleanField"), default=False)
    _l_(427758)

    objects = _c_(427759, UserManager)
    _l_(427760)

    USERNAME_FIELD = 'username'
    _l_(427761)
    REQUIRED_FIELDS = ['email']
    _l_(427762)

    def __str__(self):
        _l_(427766)

        aux = _a_(427764, _n_(427763, "self", lambda: self), "email")
        _l_(427765)
        return aux

    def get_short_name(self):
        _l_(427770)

        aux = _a_(427768, _n_(427767, "self", lambda: self), "email")
        _l_(427769)
        return aux

class Profile (_a_(427773, _n_(427772, "models", lambda: models), "Model")):
    _l_(427790)

    user = _c_(427777, _a_(427774, models, "OneToOneField"), _n_(427775, "MyUser", lambda: MyUser), on_delete=_a_(427776, models, "CASCADE")) 
    _l_(427778) 
    image = _c_(427780, _a_(427779, models, "ImageField"), default='default.jpg', upload_to='profile_pictures') #blank - true
    _l_(427781) #blank - true
    bio = _c_(427783, _a_(427782, models, "TextField"), max_length=500, blank=True)
    _l_(427784)

    def __str__(self):
        _l_(427789)

        aux = f'{_a_(427787, _a_(427786, _n_(427785, "self", lambda: self), "user"), "username")} Profile'
        _l_(427788)
        return aux