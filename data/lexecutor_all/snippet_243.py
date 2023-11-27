# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2186525/how-to-use-glob-to-find-files-recursively
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pathlib import Path
    _l_(1538907)

except ImportError:
    pass

for path in _c_(1538911, _a_(1538910, _c_(1538909, _n_(1538908, "Path", lambda: Path), 'src'), "rglob"), '*.c'):
    _l_(1538917)

    _c_(1538915, _n_(1538912, "print", lambda: print), _a_(1538914, _n_(1538913, "path", lambda: path), "name"))
    _l_(1538916)
try:
    import fnmatch
    _l_(1538919)

except ImportError:
    pass
try:
    import os
    _l_(1538921)

except ImportError:
    pass

matches = []
_l_(1538922)
for root, dirnames, filenames in _c_(1538925, _a_(1538924, _n_(1538923, "os", lambda: os), "walk"), 'src'):
    _l_(1538941)

    for filename in _c_(1538929, _a_(1538927, _n_(1538926, "fnmatch", lambda: fnmatch), "filter"), _n_(1538928, "filenames", lambda: filenames), '*.c'):
        _l_(1538940)

        _c_(1538938, _a_(1538931, _n_(1538930, "matches", lambda: matches), "append"), _c_(1538937, _a_(1538934, _a_(1538933, _n_(1538932, "os", lambda: os), "path"), "join"), _n_(1538935, "root", lambda: root), _n_(1538936, "filename", lambda: filename)))
        _l_(1538939)

