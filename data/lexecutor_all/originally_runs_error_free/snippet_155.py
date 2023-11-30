# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(1545019)

except ImportError:
    pass

def bash(command):
    _l_(1545029)

    output = _c_(1545025, _a_(1545024, _c_(1545023, _a_(1545021, _n_(1545020, "os", lambda: os), "popen"), _n_(1545022, "command", lambda: command)), "read"))
    _l_(1545026)
    aux = _n_(1545027, "output", lambda: output)
    _l_(1545028)
    return aux

print_me = _c_(1545031, _n_(1545030, "bash", lambda: bash), 'ls -l')
_l_(1545032)
_c_(1545035, _n_(1545033, "print", lambda: print), _n_(1545034, "print_me", lambda: print_me))
_l_(1545036)

