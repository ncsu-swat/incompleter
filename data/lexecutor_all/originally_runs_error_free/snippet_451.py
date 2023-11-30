# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4934806/how-can-i-find-scripts-directory
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(1543336)

except ImportError:
    pass
exec_filepath = _c_(1543341, _a_(1543339, _a_(1543338, _n_(1543337, "os", lambda: os), "path"), "realpath"), _n_(1543340, "__file__", lambda: __file__))
_l_(1543342)
exec_dirpath = _n_(1543343, "exec_filepath", lambda: exec_filepath)[0:_c_(1543346, _n_(1543344, "len", lambda: len), _n_(1543345, "exec_filepath", lambda: exec_filepath))-_c_(1543353, _n_(1543347, "len", lambda: len), _c_(1543352, _a_(1543350, _a_(1543349, _n_(1543348, "os", lambda: os), "path"), "basename"), _n_(1543351, "__file__", lambda: __file__)))]
_l_(1543354)

