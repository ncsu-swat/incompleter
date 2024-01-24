# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52826653/classmethod-error-typeerror-call-takes-2-positional-arguments-but-3-wer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class MyModel(_n_(402007, "TimeStampedModel", lambda: TimeStampedModel)):
    _l_(402017)

    some_field = _c_(402009, _a_(402008, models, "CharField"))
    _l_(402010)

    @_n_(402011, "classmethod", lambda: classmethod)
    def my_class_method(cls, value, other_value):
        _l_(402016)

        _c_(402014, _n_(402012, "print", lambda: print), _n_(402013, "value", lambda: value))
        _l_(402015)