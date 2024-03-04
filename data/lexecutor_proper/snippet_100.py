# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/67631/how-can-i-import-a-module-dynamically-given-the-full-path
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
path = _c_(61692, _a_(61691, _a_(61690, _n_(61689, "os", lambda: os), "path"), "join"), './path/to/folder/with/py/files', '*.py')
_l_(61693)
for infile in _c_(61697, _a_(61695, _n_(61694, "glob", lambda: glob), "glob"), _n_(61696, "path", lambda: path)):
    _l_(61712)

    basename = _c_(61702, _a_(61700, _a_(61699, _n_(61698, "os", lambda: os), "path"), "basename"), _n_(61701, "infile", lambda: infile))
    _l_(61703)
    basename_without_extension = _n_(61704, "basename", lambda: basename)[:-3]
    _l_(61705)

    # http://docs.python.org/library/imp.html?highlight=imp#module-imp
    _c_(61710, _a_(61707, _n_(61706, "imp", lambda: imp), "load_source"), _n_(61708, "basename_without_extension", lambda: basename_without_extension), _n_(61709, "infile", lambda: infile))
    _l_(61711)

