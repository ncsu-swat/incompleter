# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1112343/how-do-i-capture-sigint-in-python
#!/usr/bin/env python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import signal
    _l_(1540567)

except ImportError:
    pass
try:
    import sys
    _l_(1540569)

except ImportError:
    pass

def signal_handler(sig, frame):
    _l_(1540577)

    _c_(1540571, _n_(1540570, "print", lambda: print), 'You pressed Ctrl+C!')
    _l_(1540572)
    _c_(1540575, _a_(1540574, _n_(1540573, "sys", lambda: sys), "exit"), 0)
    _l_(1540576)

_c_(1540583, _a_(1540579, _n_(1540578, "signal", lambda: signal), "signal"), _a_(1540581, _n_(1540580, "signal", lambda: signal), "SIGINT"), _n_(1540582, "signal_handler", lambda: signal_handler))
_l_(1540584)
_c_(1540586, _n_(1540585, "print", lambda: print), 'Press Ctrl+C')
_l_(1540587)
_c_(1540590, _a_(1540589, _n_(1540588, "signal", lambda: signal), "pause"))
_l_(1540591)

