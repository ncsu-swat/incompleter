# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75606176/not-using-django-auth-login-required-decorator-will-throw-a-typeerror-of-adding
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Post(_a_(618118, _n_(618117, "models", lambda: models), "Model")):
    _l_(618143)

    id = _c_(618121, _a_(618119, models, "UUIDField"), primary_key=True,default=_a_(618120, uuid, "uuid4"))
    _l_(618122)
    user = _c_(618124, _a_(618123, models, "CharField"), max_length=100)
    _l_(618125)
    image = _c_(618127, _a_(618126, models, "ImageField"), upload_to="post_images")
    _l_(618128)
    caption = _c_(618130, _a_(618129, models, "TextField"))
    _l_(618131)
    created_at = _c_(618134, _a_(618132, models, "DateTimeField"), default=_a_(618133, datetime, "now"))
    _l_(618135)
    no_of_likes = _c_(618137, _a_(618136, models, "IntegerField"), default=0)
    _l_(618138)

    def __str__(self):
        _l_(618142)

        aux = _a_(618140, _n_(618139, "self", lambda: self), "user")
        _l_(618141)
        return aux

class LikePost(_a_(618145, _n_(618144, "models", lambda: models), "Model")):
    _l_(618156)

    post_id = _c_(618147, _a_(618146, models, "CharField"), max_length=500)
    _l_(618148)
    username = _c_(618150, _a_(618149, models, "CharField"), max_length=100)
    _l_(618151)

    def __str__(self):
        _l_(618155)

        aux = _a_(618153, _n_(618152, "self", lambda: self), "username")
        _l_(618154)
        return aux