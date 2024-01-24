# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60919083/getting-unexpected-nonetype-error-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import worker
    _l_(677414)

except ImportError:
    pass

def multiply_worker_value(arguments):
    _l_(677426)

    current_Worker = _n_(677415, "arguments", lambda: arguments)[0]
    _l_(677416)
    multiplier = _n_(677417, "arguments", lambda: arguments)[1]
    _l_(677418)
    new_worker = _c_(677422, _a_(677420, _n_(677419, "current_Worker", lambda: current_Worker), "change_value"), _n_(677421, "multiplier", lambda: multiplier))
    _l_(677423)
    aux = _n_(677424, "new_worker", lambda: new_worker)
    _l_(677425)
    return aux

current_worker = _c_(677429, _a_(677428, _n_(677427, "worker", lambda: worker), "Worker"))
_l_(677430)
_c_(677432, _n_(677431, "print", lambda: print), "Printing value:")
_l_(677433)
_c_(677438, _n_(677434, "print", lambda: print), _c_(677437, _a_(677436, _n_(677435, "current_worker", lambda: current_worker), "get_value"))[0])
_l_(677439)

while(_c_(677442, _a_(677441, _n_(677440, "current_worker", lambda: current_worker), "get_value"))[0] < 10):
    _l_(677449)

    paramList = [_n_(677443, "current_worker", lambda: current_worker),2]
    _l_(677444)
    current_worker = _c_(677447, _n_(677445, "multiply_worker_value", lambda: multiply_worker_value), _n_(677446, "paramList", lambda: paramList))
    _l_(677448)
_c_(677454, _n_(677450, "print", lambda: print), _c_(677453, _a_(677452, _n_(677451, "current_worker", lambda: current_worker), "get_value"))[0])
_l_(677455)