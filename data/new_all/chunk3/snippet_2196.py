# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58314475/django-typeerror-listserializer-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class KeyboardEvent(_a_(528523, _n_(528522, "models", lambda: models), "Model")):
    _l_(528538)

    value = _c_(528525, _a_(528524, models, "CharField"), max_length=15)
    _l_(528526)
    time = _c_(528528, _a_(528527, models, "DateTimeField"), auto_now=True)
    _l_(528529)
    user_id = _c_(528532, _a_(528530, models, "ForeignKey"), UserData,on_delete=_a_(528531, models, "CASCADE"))
    _l_(528533)
    def __str__(self):
        _l_(528537)

        aux = _a_(528535, _n_(528534, "self", lambda: self), "value")
        _l_(528536)
        return aux