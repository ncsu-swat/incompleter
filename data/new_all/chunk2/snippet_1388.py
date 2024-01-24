# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66003120/airflow-2-0-attributeerror-myoperator-object-has-no-attribute-kwargs
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from airflow.models.baseoperator import BaseOperator
    _l_(459035)

except ImportError:
    pass
try:
    from airflow.utils.decorators import apply_defaults
    _l_(459037)

except ImportError:
    pass

class MyOperator(_n_(459038, "BaseOperator", lambda: BaseOperator)):
    _l_(459056)


    @_n_(459039, "apply_defaults", lambda: apply_defaults)
    def __init__(self,
                 name,
                 *args,
                 **kwargs):
        _l_(459051)

        _c_(459046, _a_(459043, _n_(459040, "super", lambda: super)(_n_(459041, "MyOperator", lambda: MyOperator), _n_(459042, "self", lambda: self)), "__init__"), *_n_(459044, "args", lambda: args), **_n_(459045, "kwargs", lambda: kwargs))
        _l_(459047)
        _n_(459048, "self", lambda: self).name = _n_(459049, "name", lambda: name)
        _l_(459050)

    def execute(self, context):
        _l_(459055)

        aux = _a_(459053, _n_(459052, "self", lambda: self), "kwargs")
        _l_(459054)

        return aux