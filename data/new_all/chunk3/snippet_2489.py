# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74975991/shutil-copyfile-permissionerror-or-filenotfounderror-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(572227)

except ImportError:
    pass
try:
    import shutil
    _l_(572229)

except ImportError:
    pass
try:
    from pathlib import Path
    _l_(572231)

except ImportError:
    pass

DATA_DIR = _c_(572234, _a_(572233, _n_(572232, "Path", lambda: Path), "cwd")) / 'sourceFolder'
_l_(572235)
files = _c_(572239, _a_(572237, _n_(572236, "os", lambda: os), "listdir"), _n_(572238, "DATA_DIR", lambda: DATA_DIR))
_l_(572240)
_c_(572248, _a_(572242, _n_(572241, "shutil", lambda: shutil), "copyfile"), _c_(572247, _a_(572245, _a_(572244, _n_(572243, "os", lambda: os), "path"), "join"), 'sourceFolder', _n_(572246, "files", lambda: files)[0]), '/destFolder')
_l_(572249)