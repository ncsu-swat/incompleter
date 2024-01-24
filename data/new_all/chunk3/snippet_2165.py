# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60541782/attributeerror-when-patching-class-variable-when-mocking
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from mocking_module.sample_class import SampleClass
    _l_(528498)

except ImportError:
    pass

def do_something():
    _l_(528506)

    sample_class = _c_(528500, _n_(528499, "SampleClass", lambda: SampleClass))
    _l_(528501)
    aux = _c_(528504, _a_(528503, _n_(528502, "sample_class", lambda: sample_class), "get_base_url"))
    _l_(528505)
    return aux