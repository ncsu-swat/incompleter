# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46591421/typeerror-str-object-is-not-callable-and-renaming-files
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(551042)

except ImportError:
    pass
try:
    import re
    _l_(551044)

except ImportError:
    pass

def rename_file():
    _l_(551084)

    file_list = _c_(551047, _a_(551046, _n_(551045, "os", lambda: os), "listdir"), r"C:\Users\mdvek\Desktop\Pyton Secret Message\prank")
    _l_(551048)
    saved_path = _c_(551051, _a_(551050, _n_(551049, "os", lambda: os), "getcwd"))
    _l_(551052)
    _c_(551055, _a_(551054, _n_(551053, "os", lambda: os), "chdir"), r"C:\Users\mdvek\Desktop\Pyton Secret Message\prank")
    _l_(551056)
    _c_(551059, _n_(551057, "print", lambda: print), _n_(551058, "saved_path", lambda: saved_path))
    _l_(551060)
    for file_name in _n_(551061, "file_list", lambda: file_list):
        _l_(551067)

        file_name = _c_(551065, _a_(551063, _n_(551062, "re", lambda: re), "sub"), '[0-9]','', _n_(551064, "file_name", lambda: file_name))
        _l_(551066)

    for file_name in _n_(551068, "file_list", lambda: file_list):
        _l_(551083)

        _c_(551076, _a_(551070, _n_(551069, "os", lambda: os), "rename"), _n_(551071, "file_name", lambda: file_name), _c_(551075, _a_(551073, _n_(551072, "re", lambda: re), "sub"), '[0-9]','', _n_(551074, "file_name", lambda: file_name)))
        _l_(551077)
        _c_(551081, _a_(551079, _n_(551078, "os", lambda: os), "chdir"), _n_(551080, "saved_path", lambda: saved_path))
        _l_(551082)

_c_(551086, _n_(551085, "rename_file", lambda: rename_file))
_l_(551087)