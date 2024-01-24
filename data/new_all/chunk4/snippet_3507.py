# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73118754/filenotfounderror-in-unzipping-python-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(590392)

except ImportError:
    pass
try:
    import zipfile
    _l_(590394)

except ImportError:
    pass

directory = 'D:\\Python ds and alg by mostafa'
_l_(590395)
for file in _c_(590399, _a_(590397, _n_(590396, "os", lambda: os), "listdir"), _n_(590398, "directory", lambda: directory)):
    _l_(590412)

    if _c_(590402, _a_(590401, _n_(590400, "file", lambda: file), "endswith"), '.zip'):
        _l_(590411)

        _c_(590409, _a_(590407, _c_(590406, _a_(590404, _n_(590403, "zipfile", lambda: zipfile), "ZipFile"), _n_(590405, "file", lambda: file)), "extractall"), _n_(590408, "directory", lambda: directory))
        _l_(590410)