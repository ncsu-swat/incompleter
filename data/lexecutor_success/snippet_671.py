# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(1547024)

except ImportError:
    pass

# Clear Windows command prompt.
if (_a_(1547026, _n_(1547025, "os", lambda: os), "name") in ('ce', 'nt', 'dos')):
    _l_(1547038)

    _c_(1547029, _a_(1547028, _n_(1547027, "os", lambda: os), "system"), 'cls')
    _l_(1547030)

# Clear the Linux terminal.
elif ('posix' in _a_(1547032, _n_(1547031, "os", lambda: os), "name")):
    _l_(1547037)

    _c_(1547035, _a_(1547034, _n_(1547033, "os", lambda: os), "system"), 'clear')
    _l_(1547036)
try:
    import os
    _l_(1547040)

except ImportError:
    pass

def clear():
    _l_(1547055)

    if _a_(1547042, _n_(1547041, "os", lambda: os), "name") == 'posix':
        _l_(1547054)

        _c_(1547045, _a_(1547044, _n_(1547043, "os", lambda: os), "system"), 'clear')
        _l_(1547046)

    elif _a_(1547048, _n_(1547047, "os", lambda: os), "name") in ('ce', 'nt', 'dos'):
        _l_(1547053)

        _c_(1547051, _a_(1547050, _n_(1547049, "os", lambda: os), "system"), 'cls')
        _l_(1547052)


_c_(1547057, _n_(1547056, "clear", lambda: clear))
_l_(1547058)

