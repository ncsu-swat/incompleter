# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68410926/is-there-a-way-to-solve-enter-attributeerror-in-contextdecorator
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class CmTag(_n_(549380, "ContextDecorator", lambda: ContextDecorator)):
    _l_(549424)


    def __init__(self, cm_tag_func):
        _l_(549384)

        _n_(549381, "self", lambda: self).cm_tag_func = _n_(549382, "cm_tag_func", lambda: cm_tag_func)
        _l_(549383)
    def __enter__(self):
        _l_(549387)

        aux = _n_(549385, "self", lambda: self)
        _l_(549386)
        return aux

    def __exit__(self, exc_type, exc_value, tb):
        _l_(549405)

        if _n_(549388, "exc_type", lambda: exc_type) is not None:
            _l_(549404)

            _c_(549394, _a_(549390, _n_(549389, "traceback", lambda: traceback), "print_exception"), _n_(549391, "exc_type", lambda: exc_type), _n_(549392, "exc_value", lambda: exc_value), _n_(549393, "tb", lambda: tb))
            _l_(549395)
        else:
            name = _a_(549398, _a_(549397, _n_(549396, "self", lambda: self), "cm_tag_func"), "__name__")
            _l_(549399)
            _c_(549402, _n_(549400, "print", lambda: print), _n_(549401, "name", lambda: name))
            _l_(549403)

    def __call__(self, **kwargs):
        _l_(549423)


        name = _a_(549408, _a_(549407, _n_(549406, "self", lambda: self), "cm_tag_func"), "__name__")
        _l_(549409)
        _c_(549412, _n_(549410, "print", lambda: print), _n_(549411, "name", lambda: name))
        _l_(549413)
        _c_(549416, _n_(549414, "print", lambda: print), _n_(549415, "kwargs", lambda: kwargs))
        _l_(549417)
        _c_(549421, _a_(549419, _n_(549418, "self", lambda: self), "cm_tag_func"), **_n_(549420, "kwargs", lambda: kwargs))
        _l_(549422)

@_n_(549425, "CmTag", lambda: CmTag)
def testing(**kwargs):
    _l_(549427)

    pass
    _l_(549426)

with _c_(549429, _n_(549428, "testing", lambda: testing), foo='bar') as t:
    _l_(549433)

    _c_(549431, _n_(549430, "print", lambda: print), 'a test')
    _l_(549432)