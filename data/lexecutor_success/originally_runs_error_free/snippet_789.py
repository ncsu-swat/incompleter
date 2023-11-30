# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3503879/assign-output-of-os-system-to-a-variable-and-prevent-it-from-being-displayed-on
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from subprocess import PIPE, run
    _l_(1543753)

except ImportError:
    pass

def out(command):
    _l_(1543763)

    result = _c_(1543758, _n_(1543754, "run", lambda: run), _n_(1543755, "command", lambda: command), stdout=_n_(1543756, "PIPE", lambda: PIPE), stderr=_n_(1543757, "PIPE", lambda: PIPE), universal_newlines=True, shell=True)
    _l_(1543759)
    aux = _a_(1543761, _n_(1543760, "result", lambda: result), "stdout")
    _l_(1543762)
    return aux

my_output = _c_(1543765, _n_(1543764, "out", lambda: out), "echo hello world")
_l_(1543766)
# Or
my_output = _c_(1543768, _n_(1543767, "out", lambda: out), ["echo", "hello world"])
_l_(1543769)

