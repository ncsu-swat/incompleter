# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/36077266/how-do-i-raise-a-filenotfounderror-properly
#!/usr/bin/env python3

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(410665)

except ImportError:
    pass

if not _c_(410669, _a_(410668, _a_(410667, _n_(410666, "os", lambda: os), "path"), "isfile"), "nothing.txt"):
    _l_(410672)

    raise _n_(410670, "FileNotFoundError", lambda: FileNotFoundError)
    _l_(410671)