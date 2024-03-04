# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4789837/how-to-terminate-a-python-subprocess-launched-with-shell-true
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _c_(64863, _n_(64860, "isinstance", lambda: isinstance), _n_(64861, "command", lambda: command), _n_(64862, "unicode", lambda: unicode)):
    _l_(64868)

    cmd = _c_(64866, _a_(64865, _n_(64864, "command", lambda: command), "encode"), 'utf8')
    _l_(64867)
args = _c_(64872, _a_(64870, _n_(64869, "shlex", lambda: shlex), "split"), _n_(64871, "cmd", lambda: cmd))
_l_(64873)

p = _c_(64881, _a_(64875, _n_(64874, "subprocess", lambda: subprocess), "Popen"), _n_(64876, "args", lambda: args), stdout=_a_(64878, _n_(64877, "subprocess", lambda: subprocess), "PIPE"), stderr=_a_(64880, _n_(64879, "subprocess", lambda: subprocess), "STDOUT"))
_l_(64882)

