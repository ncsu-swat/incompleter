# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/944592/best-practice-for-using-assert
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    _l_(1545521)

    assert False
    _l_(1545514)
    raise _c_(1545516, _n_(1545515, "Exception", lambda: Exception), 'Python assertions are not working. This tool relies on Python assertions to do its job. Possible causes are running with the "-O" flag or running a precompiled (".pyo" or ".pyc") module.')
    _l_(1545517)
except _n_(1545518, "AssertionError", lambda: AssertionError):
    _l_(1545520)

    pass
    _l_(1545519)

