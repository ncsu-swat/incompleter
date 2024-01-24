# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41719307/typeerror-popen-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import subprocess, codecs
    _l_(400111)

except ImportError:
    pass

def serviceStatus(RadiaService):
    _l_(400140)

    status = []
    _l_(400112)
    cmd = 'sc query ' + _n_(400113, "RadiaService", lambda: RadiaService)
    _l_(400114)
    pDetails = _c_(400120, _a_(400116, _n_(400115, "subprocess", lambda: subprocess), "Popen"), _n_(400117, "cmd", lambda: cmd), shell = True, stdout = _a_(400119, _n_(400118, "subprocess", lambda: subprocess), "PIPE"))
    _l_(400121)
    for item in _c_(400123, _n_(400122, "pDetails", lambda: pDetails)):
        _l_(400129)

        _c_(400127, _a_(400125, _n_(400124, "status", lambda: status), "append"), _n_(400126, "item", lambda: item))
        _l_(400128)
    finalStatus = _c_(400134, _a_(400133, _c_(400132, _a_(400130, b'', "join"), _n_(400131, "status", lambda: status)), "decode"), 'utf-8')
    _l_(400135)
    _c_(400138, _n_(400136, "print", lambda: print), _n_(400137, "finalStatus", lambda: finalStatus))
    _l_(400139)

if _n_(400141, "__name__", lambda: __name__) == '__main__':
    _l_(400145)

    _c_(400143, _n_(400142, "serviceStatus", lambda: serviceStatus), 'RCA')
    _l_(400144)