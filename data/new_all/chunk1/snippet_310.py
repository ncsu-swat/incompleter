# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49821328/pyspark-udf-attributeerror-nonetype-object-has-no-attribute-jvm
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_n_(383242, "staticmethod", lambda: staticmethod)
@_c_(383245, _a_(383244, _n_(383243, "F", lambda: F), "udf"), "array<int>")
def create_users_array(val):
    _l_(383251)

    """ Takes column of ints, returns column of arrays containing ints. """ 
    aux = [_n_(383246, "val", lambda: val) for _ in _c_(383249, _n_(383247, "range", lambda: range), _n_(383248, "val", lambda: val))]
    _l_(383250)
    return aux