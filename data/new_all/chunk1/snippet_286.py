# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56261606/how-to-fix-typeerror-a-bytes-like-object-is-required-not-str-error-in-pyth
# logger.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import logging
    _l_(376710)

except ImportError:
    pass
try:
    import os
    _l_(376712)

except ImportError:
    pass
try:
    import classpathDir as cf
    _l_(376714)

except ImportError:
    pass


def getLogger(loggerForFile):
    _l_(376761)

    logger = _c_(376722, _a_(376716, _n_(376715, "logging", lambda: logging), "getLogger"), _c_(376721, _a_(376719, _a_(376718, _n_(376717, "os", lambda: os), "path"), "basename"), _n_(376720, "loggerForFile", lambda: loggerForFile)))
    _l_(376723)
    if not _a_(376725, _n_(376724, "logger", lambda: logger), "handlers"):
        _l_(376758)

        _c_(376732, _a_(376727, _n_(376726, "logging", lambda: logging), "basicConfig"), format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%d/%m/%Y %I:%M:%S %p', filename=_a_(376729, _n_(376728, "cf", lambda: cf), "ROOT_DIR") + "/output/processing.log",
                            filemode='wb', level=_a_(376731, _n_(376730, "logging", lambda: logging), "DEBUG"))
        _l_(376733)
        console = _c_(376736, _a_(376735, _n_(376734, "logging", lambda: logging), "StreamHandler"))
        _l_(376737)
        _c_(376742, _a_(376739, _n_(376738, "console", lambda: console), "setLevel"), _a_(376741, _n_(376740, "logging", lambda: logging), "DEBUG"))
        _l_(376743)
        # set a format which is simpler for console use
        formatter = _c_(376746, _a_(376745, _n_(376744, "logging", lambda: logging), "Formatter"), '%(asctime)s %(name)-12s: %(levelname)-8s %(message)s',
                                      datefmt='%d/%m/%Y %I:%M:%S')
        _l_(376747)
        # tell the handler to use this format
        _c_(376751, _a_(376749, _n_(376748, "console", lambda: console), "setFormatter"), _n_(376750, "formatter", lambda: formatter))
        _l_(376752)
        # add the handler to the root logger
        _c_(376756, _a_(376754, _n_(376753, "logger", lambda: logger), "addHandler"), _n_(376755, "console", lambda: console))
        _l_(376757)
    aux = _n_(376759, "logger", lambda: logger)
    _l_(376760)
    return aux


if _n_(376762, "__name__", lambda: __name__) == '__main__':
    _l_(376766)

    _c_(376764, _n_(376763, "print", lambda: print), "Logging config module")
    _l_(376765)