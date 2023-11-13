# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/954834/how-do-i-use-raw-input-in-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import platform
    _l_(1544993)

except ImportError:
    pass
def str_input(str=''):
    _l_(1545014)

    py_version = _c_(1544996, _a_(1544995, _n_(1544994, "platform", lambda: platform), "python_version")) # fetch the python version currently in use
    _l_(1544997) # fetch the python version currently in use
    if _c_(1545000, _n_(1544998, "int", lambda: int), _n_(1544999, "py_version", lambda: py_version)[0]) == 2:
        _l_(1545005)

        aux = _c_(1545003, _n_(1545001, "raw_input", lambda: raw_input), _n_(1545002, "str", lambda: str)) # input string in python2
        _l_(1545004) # input string in python2
        return aux # input string in python2
    if _c_(1545008, _n_(1545006, "int", lambda: int), _n_(1545007, "py_version", lambda: py_version)[0]) == 3:
        _l_(1545013)

        aux = _c_(1545011, _n_(1545009, "input", lambda: input), _n_(1545010, "str", lambda: str)) # input string in python3
        _l_(1545012) # input string in python3
        return aux # input string in python3

_c_(1545016, _n_(1545015, "str_input", lambda: str_input), "Your Name: ")
_l_(1545017)

