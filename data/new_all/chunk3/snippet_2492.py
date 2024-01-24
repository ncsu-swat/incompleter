# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74934265/python-threading-typeerror-too-many-arguments
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import threading
    _l_(562944)

except ImportError:
    pass

class ReadWrite:
    _l_(563056)

    threadList = [0] * 20
    _l_(562945)

    def __init__(self, origData):
        _l_(562961)

        _n_(562946, "self", lambda: self).readerLock = _c_(562949, _a_(562948, _n_(562947, "threading", lambda: threading), "Lock"))
        _l_(562950)
        _n_(562951, "self", lambda: self).writerLock = _c_(562954, _a_(562953, _n_(562952, "threading", lambda: threading), "Lock"))
        _l_(562955)
        _n_(562956, "self", lambda: self).data = _n_(562957, "origData", lambda: origData)
        _l_(562958)
        _n_(562959, "self", lambda: self).readerCount = 0
        _l_(562960)

    def acquireReadLock(self):
        _l_(562967)

        _c_(562965, _a_(562964, _a_(562963, _n_(562962, "self", lambda: self), "readerLock"), "acquire"))
        _l_(562966)

    def releaseReadLock(self):
        _l_(562973)

        _c_(562971, _a_(562970, _a_(562969, _n_(562968, "self", lambda: self), "readerLock"), "release"))
        _l_(562972)

    def acquireWriteLock(self):
        _l_(562979)

        _c_(562977, _a_(562976, _a_(562975, _n_(562974, "self", lambda: self), "writerLock"), "acquire"))
        _l_(562978)

    def releaseWriteLock(self):
        _l_(562985)

        _c_(562983, _a_(562982, _a_(562981, _n_(562980, "self", lambda: self), "writerLock"), "release"))
        _l_(562984)

    def printData(self, threadName):
        _l_(562992)

        _c_(562990, _n_(562986, "print", lambda: print), _n_(562987, "threadName", lambda: threadName), ' printed ', _a_(562989, _n_(562988, "self", lambda: self), "data"))
        _l_(562991)

    def modifyData(self, threadName, newData):
        _l_(563003)

        _c_(562998, _n_(562993, "print", lambda: print), _n_(562994, "threadName", lambda: threadName), ' changed ', _a_(562996, _n_(562995, "self", lambda: self), "data"), ' to ', _n_(562997, "newData", lambda: newData))
        _l_(562999)
        _n_(563000, "self", lambda: self).data = _n_(563001, "newData", lambda: newData)
        _l_(563002)
    
    def run(self):
        _l_(563055)

        for x in _c_(563005, _n_(563004, "range", lambda: range), 20):
            _l_(563045)

            threadString = 'Thread' + _c_(563008, _n_(563006, "str", lambda: str), _n_(563007, "x", lambda: x))
            _l_(563009)
            if _n_(563010, "x", lambda: x) % 6:
                _l_(563038)

                _a_(563012, _n_(563011, "self", lambda: self), "threadList")[_n_(563013, "x", lambda: x)] = _c_(563019, _a_(563015, _n_(563014, "threading", lambda: threading), "Thread"), target=_a_(563017, _n_(563016, "self", lambda: self), "printData"), args=_n_(563018, "threadString", lambda: (threadString)))
                _l_(563020)
            else:
                newData = _a_(563022, _n_(563021, "self", lambda: self), "data") + _c_(563025, _n_(563023, "str", lambda: str), _n_(563024, "x", lambda: x))
                _l_(563026)
                _a_(563028, _n_(563027, "self", lambda: self), "threadList")[_n_(563029, "x", lambda: x)] = _c_(563036, _a_(563031, _n_(563030, "threading", lambda: threading), "Thread"), target=_a_(563033, _n_(563032, "self", lambda: self), "modifyData"), args=(_n_(563034, "threadString", lambda: threadString), _n_(563035, "newData", lambda: newData)))
                _l_(563037)
            _c_(563043, _a_(563042, _a_(563040, _n_(563039, "self", lambda: self), "threadList")[_n_(563041, "x", lambda: x)], "start"))
            _l_(563044)

        for x in _c_(563047, _n_(563046, "range", lambda: range), 20):
            _l_(563054)

            _c_(563052, _a_(563051, _a_(563049, _n_(563048, "self", lambda: self), "threadList")[_n_(563050, "x", lambda: x)], "join"))
            _l_(563053)
myVar = _c_(563058, _n_(563057, "ReadWrite", lambda: ReadWrite), 'Hello')
_l_(563059)
_c_(563062, _a_(563061, _n_(563060, "myVar", lambda: myVar), "run"))
_l_(563063)