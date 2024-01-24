# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69891656/python-typeerror-missing-1-required-positional-argument-only-when-using-threa
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(591159)

except ImportError:
    pass
try:
    import multiprocessing
    _l_(591161)

except ImportError:
    pass
try:
    from multiprocessing import Process, Pool
    _l_(591163)

except ImportError:
    pass
try:
    from concurrent.futures import ThreadPoolExecutor
    _l_(591165)

except ImportError:
    pass

class GlobalValues(_n_(591166, "object", lambda: object)):
    _l_(591181)

    #singleton thread pool 
    Executor : _n_(591167, "ThreadPoolExecutor", lambda: ThreadPoolExecutor) = None
    _l_(591168)
    @_n_(591169, "staticmethod", lambda: staticmethod)
    def getThreadPoolExecutor():
        _l_(591180)

        if _a_(591171, _n_(591170, "GlobalValues", lambda: GlobalValues), "Executor")==None:
            _l_(591176)

            _n_(591172, "GlobalValues", lambda: GlobalValues).Executor = _c_(591174, _n_(591173, "ThreadPoolExecutor", lambda: ThreadPoolExecutor), 500)
            _l_(591175)
        aux = _a_(591178, _n_(591177, "GlobalValues", lambda: GlobalValues), "Executor")
        _l_(591179)
        return aux