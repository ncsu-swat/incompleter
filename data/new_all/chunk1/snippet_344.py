# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47215264/file-not-found-error-in-os-rename
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(379582)

except ImportError:
    pass

old_dir = '/Users/User/Desktop/MyFolder'
_l_(379583)

for f in _c_(379587, _a_(379585, _n_(379584, "os", lambda: os), "listdir"), _n_(379586, "old_dir", lambda: old_dir)):
    _l_(379624)

    file_name, file_ext = _c_(379592, _a_(379590, _a_(379589, _n_(379588, "os", lambda: os), "path"), "splitext"), _n_(379591, "f", lambda: f))
    _l_(379593)
    _c_(379596, _a_(379595, _n_(379594, "file_name", lambda: file_name), "split"), '-')
    _l_(379597)

    split_file_name = _c_(379600, _a_(379599, _n_(379598, "file_name", lambda: file_name), "split"), '-')
    _l_(379601)

    new_dir = _c_(379611, _a_(379604, _a_(379603, _n_(379602, "os", lambda: os), "path"), "join"), _n_(379605, "old_dir", lambda: old_dir),
                           _c_(379608, _a_(379606, '-', "join"), _n_(379607, "split_file_name", lambda: split_file_name)[:3]),
                           _n_(379609, "split_file_name", lambda: split_file_name)[5],
                           _n_(379610, "f", lambda: f))
    _l_(379612)

    _c_(379622, _a_(379614, _n_(379613, "os", lambda: os), "rename"), _c_(379620, _a_(379617, _a_(379616, _n_(379615, "os", lambda: os), "path"), "join"), _n_(379618, "old_dir", lambda: old_dir), _n_(379619, "f", lambda: f)), _n_(379621, "new_dir", lambda: new_dir))
    _l_(379623)