# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66065071/got-attributeerror-when-attempting-to-get-a-value-for-field-text-on-serializer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Comment(_a_(553699, _n_(553698, "models", lambda: models), "Model")) :
    _l_(553724)

    text = _c_(553702, _a_(553700, models, "TextField"), validators=[_c_(553701, MinLengthValidator, 3, "Comment must be greater than 3 characters")]
    )
    _l_(553703)

    post = _c_(553706, _a_(553704, models, "ForeignKey"), Post, on_delete=_a_(553705, models, "CASCADE"))
    _l_(553707)
    owner = _c_(553711, _a_(553708, models, "ForeignKey"), _a_(553709, settings, "AUTH_USER_MODEL"), on_delete=_a_(553710, models, "CASCADE"))
    _l_(553712)

    created_at = _c_(553714, _a_(553713, models, "DateTimeField"), auto_now_add=True)
    _l_(553715)
    updated_at = _c_(553717, _a_(553716, models, "DateTimeField"), auto_now=True)
    _l_(553718)

    # Shows up in the admin list
    def __str__(self):
        _l_(553723)

        aux = _a_(553721, _a_(553720, _n_(553719, "self", lambda: self), "post"), "title")
        _l_(553722)
        return aux