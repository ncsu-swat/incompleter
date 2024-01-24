# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72492502/nameerror-name-f-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class User(_n_(340930, "AbstractUser", lambda: AbstractUser)):
    _l_(340964)

    user_pic = _c_(340932, _a_(340931, models, "ImageField"), upload_to='img/',default="",null=True, blank=True)
    _l_(340933)
    coins = _c_(340935, _a_(340934, models, "IntegerField"), default=10)
    _l_(340936)
    def get_image(self):
        _l_(340949)

        if _a_(340938, _n_(340937, "self", lambda: self), "user_pic") and _c_(340942, _n_(340939, "hasattr", lambda: hasattr), _a_(340941, _n_(340940, "self", lambda: self), "user_pic"), 'url'):
            _l_(340948)

            aux = _a_(340945, _a_(340944, _n_(340943, "self", lambda: self), "user_pic"), "url")
            _l_(340946)
            return aux
        else:
            aux = '/path/to/default/image'
            _l_(340947)
            return aux
    def give_coins(user, count):
        _l_(340963)

        _n_(340950, "user", lambda: user).coins = _c_(340952, _n_(340951, "F", lambda: F), 'coins') + _n_(340953, "count", lambda: count)
        _l_(340954)
        _c_(340957, _a_(340956, _n_(340955, "user", lambda: user), "save"), update_fields=('coins',))
        _l_(340958)
        _c_(340961, _a_(340960, _n_(340959, "user", lambda: user), "refresh_from_db"), fields=('coins',))
        _l_(340962)