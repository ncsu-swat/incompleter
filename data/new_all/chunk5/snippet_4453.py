# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57584882/filenotfounderror-errno-2-no-such-file-or-directory-2mcrefe-jpg
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(662468)

except ImportError:
    pass
try:
    from PIL import Image
    _l_(662470)

except ImportError:
    pass

folder = '/Users/abc'
_l_(662471)
if not _c_(662475, _a_(662473, _n_(662472, "os", lambda: os), "listdir"), _n_(662474, "folder", lambda: folder)):
    _l_(662485)

    _c_(662477, _n_(662476, "print", lambda: print), 'Folder not found')
    _l_(662478)
else:
    _c_(662483, _n_(662479, "print", lambda: print), _c_(662482, _a_(662480, '"{}" found', "format"), _n_(662481, "folder", lambda: folder)))
    _l_(662484)

for file in _c_(662489, _a_(662487, _n_(662486, "os", lambda: os), "listdir"), _n_(662488, "folder", lambda: folder)):
    _l_(662499)

    _c_(662492, _n_(662490, "print", lambda: print), _n_(662491, "file", lambda: file))
    _l_(662493)
    data = _c_(662497, _a_(662495, _n_(662494, "Image", lambda: Image), "open"), _n_(662496, "file", lambda: file),'r')
    _l_(662498)
_c_(662501, _n_(662500, "print", lambda: print), 'Done')
_l_(662502)