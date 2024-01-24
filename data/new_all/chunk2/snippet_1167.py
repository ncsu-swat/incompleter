# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70382456/typeerror-function-takes-x-positional-argument-but-x-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _n_(448861, "__name__", lambda: __name__) == '__main__':
    _l_(448884)

    pth = "/home/abd/Downloads/"
    _l_(448862)
    pth2 = "/home/abd/Desktop/"
    _l_(448863)

    Proc1 = _c_(448868, _a_(448865, _n_(448864, "multiprocessing", lambda: multiprocessing), "Process"), target=_n_(448866, "watcher", lambda: watcher), args=_n_(448867, "pth", lambda: (pth)))
    _l_(448869)
    Proc2 = _c_(448874, _a_(448871, _n_(448870, "multiprocessing", lambda: multiprocessing), "Process"), target=_n_(448872, "watcher", lambda: watcher), args=_n_(448873, "pth2", lambda: (pth2)))
    _l_(448875)
    _c_(448878, _a_(448877, _n_(448876, "Proc1", lambda: Proc1), "start"))
    _l_(448879)
    _c_(448882, _a_(448881, _n_(448880, "Proc2", lambda: Proc2), "start"))
    _l_(448883)