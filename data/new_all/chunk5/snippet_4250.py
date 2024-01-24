# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57584882/filenotfounderror-errno-2-no-such-file-or-directory-2mcrefe-jpg
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(706416)

except ImportError:
    pass
try:
    from PIL import Image
    _l_(706418)

except ImportError:
    pass

folder = '/Users/abc'
_l_(706419)
if not _c_(706423, _a_(706421, _n_(706420, "os", lambda: os), "listdir"), _n_(706422, "folder", lambda: folder)):
    _l_(706433)

    _c_(706425, _n_(706424, "print", lambda: print), 'Folder not found')
    _l_(706426)
else:
    _c_(706431, _n_(706427, "print", lambda: print), _c_(706430, _a_(706428, '"{}" found', "format"), _n_(706429, "folder", lambda: folder)))
    _l_(706432)

for file in _c_(706437, _a_(706435, _n_(706434, "os", lambda: os), "listdir"), _n_(706436, "folder", lambda: folder)):
    _l_(706447)

    _c_(706440, _n_(706438, "print", lambda: print), _n_(706439, "file", lambda: file))
    _l_(706441)
    data = _c_(706445, _a_(706443, _n_(706442, "Image", lambda: Image), "open"), _n_(706444, "file", lambda: file),'r')
    _l_(706446)
_c_(706449, _n_(706448, "print", lambda: print), 'Done')
_l_(706450)