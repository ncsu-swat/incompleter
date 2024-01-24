# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53947049/attributeerror-at-login-type-object-super-has-no-attribute-save
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(432087)

except ImportError:
    pass
try:
    from django.contrib.auth.models import User
    _l_(432089)

except ImportError:
    pass
try:
    from PIL import Image
    _l_(432091)

except ImportError:
    pass


class Profile(_a_(432093, _n_(432092, "models", lambda: models), "Model")):
    _l_(432140)

    user = _c_(432099, _a_(432095, _n_(432094, "models", lambda: models), "OneToOneField"), _n_(432096, "User", lambda: User), on_delete=_a_(432098, _n_(432097, "models", lambda: models), "CASCADE"))
    _l_(432100)
    image = _c_(432103, _a_(432102, _n_(432101, "models", lambda: models), "ImageField"), default='default.jpg', 
    upload_to='profile_pics')
    _l_(432104)

    def __str__(self):
        _l_(432109)

        aux = f'{_a_(432107, _a_(432106, _n_(432105, "self", lambda: self), "user"), "username")} Profile'
        _l_(432108)
        return aux

    def save(self):
        _l_(432139)

        _c_(432112, _a_(432111, _n_(432110, 'super', lambda: super), 'save'))
        _l_(432113)
        img = _c_(432119, _a_(432115, _n_(432114, 'Image', lambda: Image), 'open'), _a_(432118, _a_(432117, _n_(432116, 'self', lambda: self), 'image'), 'path'))
        _l_(432120)

        if _a_(432122, _n_(432121, 'img', lambda: img), 'height') > 300 or _a_(432124, _n_(432123, 'img', lambda: img), 'width') > 300:
            _l_(432138)

            output_size = (300, 300)
            _l_(432125)
            _c_(432129, _a_(432127, _n_(432126, 'img', lambda: img), 'thumbnail'), _n_(432128, 'output_size', lambda: output_size))
            _l_(432130)
            _c_(432136, _a_(432132, _n_(432131, 'img', lambda: img), 'save'), _a_(432135, _a_(432134, _n_(432133, 'self', lambda: self), 'image'), 'path'))
            _l_(432137)