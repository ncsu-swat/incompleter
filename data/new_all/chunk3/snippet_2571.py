# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71181635/psychopy-runtime-error-while-logging-a-message-typeerror-not-supported-b
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from psychopy import logging
    _l_(557147)

except ImportError:
    pass
log = _c_(557152, _a_(557149, _n_(557148, "logging", lambda: logging), "LogFile"), "WS_Dev.log", level = _a_(557151, _n_(557150, "logging", lambda: logging), "DEBUG"), filemode = "w")
_l_(557153)
_c_(557158, _a_(557155, _n_(557154, "logging", lambda: logging), "log"), _a_(557157, _n_(557156, "logging", lambda: logging), "DEBUG"), "in getArguments()")
_l_(557159)