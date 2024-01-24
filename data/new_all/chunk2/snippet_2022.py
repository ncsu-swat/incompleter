# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68994258/django-typeerror-httpresponseforbidden-object-is-not-callable
#models
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(472547)

except ImportError:
    pass
try:
    from django.contrib.auth.models import User
    _l_(472549)

except ImportError:
    pass
try:
    from django.db.models.deletion import CASCADE
    _l_(472551)

except ImportError:
    pass
try:
    from PIL import Image
    _l_(472553)

except ImportError:
    pass


class Profile(_a_(472555, _n_(472554, "models", lambda: models), "Model")):
    _l_(472602)

    user = _c_(472561, _a_(472557, _n_(472556, "models", lambda: models), "OneToOneField"), _n_(472558, "User", lambda: User),on_delete=_a_(472560, _n_(472559, "models", lambda: models), "CASCADE"))
    _l_(472562)
    image = _c_(472565, _a_(472564, _n_(472563, "models", lambda: models), "ImageField"), default='default.jpg', upload_to='profile_pic')
    _l_(472566)

    def __str__(self):
        _l_(472571)

        aux = f'{_a_(472569, _a_(472568, _n_(472567, "self", lambda: self), "user"), "username")} Profile'
        _l_(472570)
        return aux

    def save(self):
        _l_(472601)

        _c_(472574, _a_(472573, _n_(472572, 'super', lambda: super)(), 'save'))     
        _l_(472575)     
        img = _c_(472581, _a_(472577, _n_(472576, 'Image', lambda: Image), 'open'), _a_(472580, _a_(472579, _n_(472578, 'self', lambda: self), 'image'), 'path'))
        _l_(472582)
        if _a_(472584, _n_(472583, 'img', lambda: img), 'height') > 300 and _a_(472586, _n_(472585, 'img', lambda: img), 'width') > 300:
            _l_(472600)

            output_size=(300,300)
            _l_(472587)
            _c_(472591, _a_(472589, _n_(472588, 'img', lambda: img), 'thumbnail'), _n_(472590, 'output_size', lambda: output_size))
            _l_(472592)
            _c_(472598, _a_(472594, _n_(472593, 'img', lambda: img), 'save'), _a_(472597, _a_(472596, _n_(472595, 'self', lambda: self), 'image'), 'path'))
            _l_(472599)