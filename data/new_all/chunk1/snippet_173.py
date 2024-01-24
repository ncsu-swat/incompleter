# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41401417/with-os-scandir-raises-attributeerror-exit
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(383070, _a_(383068, _n_(383067, "os", lambda: os), "scandir"), _n_(383069, "path", lambda: path)) as it:
    _l_(383086)

    for entry in _n_(383071, "it", lambda: it):
        _l_(383085)

        if not _c_(383075, _a_(383074, _a_(383073, _n_(383072, "entry", lambda: entry), "name"), "startswith"), '.') and _c_(383078, _a_(383077, _n_(383076, "entry", lambda: entry), "is_file")):
            _l_(383084)

            _c_(383082, _n_(383079, "print", lambda: print), _a_(383081, _n_(383080, "entry", lambda: entry), "name"))
            _l_(383083)