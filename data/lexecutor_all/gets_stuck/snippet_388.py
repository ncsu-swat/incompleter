# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/189645/how-can-i-break-out-of-multiple-loops
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
while True:
    _l_(1538568)

    break_statement=0
    _l_(1538551)
    while True:
        _l_(1538564)

        ok = _c_(1538553, _n_(1538552, "raw_input", lambda: raw_input), "Is this ok? (y/n)")
        _l_(1538554)
        if _n_(1538555, "ok", lambda: ok) == "n" or _n_(1538556, "ok", lambda: ok) == "N":
            _l_(1538558)

            break
            _l_(1538557)
        if _n_(1538559, "ok", lambda: ok) == "y" or _n_(1538560, "ok", lambda: ok) == "Y":
            _l_(1538563)

            break_statement=1
            _l_(1538561)
            break
            _l_(1538562)
    if _n_(1538565, "break_statement", lambda: break_statement)==1:
        _l_(1538567)

        break
        _l_(1538566)

