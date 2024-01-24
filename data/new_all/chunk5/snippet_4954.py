# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72492502/nameerror-name-f-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class User(_n_(685810, "AbstractUser", lambda: AbstractUser)):
    _l_(685844)

    user_pic = _c_(685812, _a_(685811, models, "ImageField"), upload_to='img/',default="",null=True, blank=True)
    _l_(685813)
    coins = _c_(685815, _a_(685814, models, "IntegerField"), default=10)
    _l_(685816)
    def get_image(self):
        _l_(685829)

        if _a_(685818, _n_(685817, "self", lambda: self), "user_pic") and _c_(685822, _n_(685819, "hasattr", lambda: hasattr), _a_(685821, _n_(685820, "self", lambda: self), "user_pic"), 'url'):
            _l_(685828)

            aux = _a_(685825, _a_(685824, _n_(685823, "self", lambda: self), "user_pic"), "url")
            _l_(685826)
            return aux
        else:
            aux = '/path/to/default/image'
            _l_(685827)
            return aux
    def give_coins(user, count):
        _l_(685843)

        _n_(685830, "user", lambda: user).coins = _c_(685832, _n_(685831, "F", lambda: F), 'coins') + _n_(685833, "count", lambda: count)
        _l_(685834)
        _c_(685837, _a_(685836, _n_(685835, "user", lambda: user), "save"), update_fields=('coins',))
        _l_(685838)
        _c_(685841, _a_(685840, _n_(685839, "user", lambda: user), "refresh_from_db"), fields=('coins',))
        _l_(685842)