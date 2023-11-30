# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/14058453/making-python-loggers-output-all-messages-to-stdout-in-addition-to-log-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import logging
    _l_(1538809)

except ImportError:
    pass

_c_(1538812, _a_(1538811, _n_(1538810, "logging", lambda: logging), "basicConfig"), filename="logfile.txt")
_l_(1538813)
stderrLogger=_c_(1538816, _a_(1538815, _n_(1538814, "logging", lambda: logging), "StreamHandler"))
_l_(1538817)
_c_(1538825, _a_(1538819, _n_(1538818, "stderrLogger", lambda: stderrLogger), "setFormatter"), _c_(1538824, _a_(1538821, _n_(1538820, "logging", lambda: logging), "Formatter"), _a_(1538823, _n_(1538822, "logging", lambda: logging), "BASIC_FORMAT")))
_l_(1538826)
_c_(1538832, _a_(1538830, _c_(1538829, _a_(1538828, _n_(1538827, "logging", lambda: logging), "getLogger")), "addHandler"), _n_(1538831, "stderrLogger", lambda: stderrLogger))
_l_(1538833)

