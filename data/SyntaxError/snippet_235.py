# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def mkdirRecursive(dirpath):
    _l_(1539262)

    try:
        import os
        _l_(1539231)

    except ImportError:
        pass
    if _c_(1539236, _a_(1539234, _a_(1539233, _n_(1539232, "os", lambda: os), "path"), "isdir"), _n_(1539235, "dirpath", lambda: dirpath)):
        _l_(1539237)

return
    h,t = _c_(1539242, _a_(1539240, _a_(1539239, _n_(1539238, "os", lambda: os), "path"), "split"), _n_(1539241, "dirpath", lambda: dirpath)) # head/tail
    _l_(1539243) # head/tail
    if not _c_(1539248, _a_(1539246, _a_(1539245, _n_(1539244, "os", lambda: os), "path"), "isdir"), _n_(1539247, "h", lambda: h)):
        _l_(1539253)

        _c_(1539251, _n_(1539249, "mkdirRecursive", lambda: mkdirRecursive), _n_(1539250, "h", lambda: h))
        _l_(1539252)

    _c_(1539260, _a_(1539255, _n_(1539254, "os", lambda: os), "mkdir"), _c_(1539259, _n_(1539256, "join", lambda: join), _n_(1539257, "h", lambda: h),_n_(1539258, "t", lambda: t)))
    _l_(1539261)
# end mkdirRecursive

