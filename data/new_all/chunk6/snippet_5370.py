# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50805607/python-3-name-error-from-input-within-a-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def multiply(num_1, num_2):
    _l_(358907)

    num_1 = _c_(358889, _n_(358888, "input", lambda: input), "enter a whole number:")
    _l_(358890)
    num_2 = _c_(358892, _n_(358891, "input", lambda: input), "enter another whole number:")
    _l_(358893)
    result = _c_(358896, _n_(358894, "int", lambda: int), _n_(358895, "num_1", lambda: num_1))*_c_(358899, _n_(358897, "int", lambda: int), _n_(358898, "num_2", lambda: num_2))
    _l_(358900)
    aux = (_n_(358901, "num_1", lambda: num_1) + " * " + _n_(358902, "num_2", lambda: num_2) + " = " + _c_(358905, _n_(358903, "str", lambda: str), _n_(358904, "result", lambda: result)))
    _l_(358906)
    return aux

_c_(358911, _n_(358908, "multiply", lambda: multiply), _n_(358909, "num_1", lambda: num_1), _n_(358910, "num_2", lambda: num_2))
_l_(358912)