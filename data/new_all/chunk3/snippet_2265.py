# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54564772/renaming-files-in-python-getting-filenotfounderror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(575752)

except ImportError:
    pass

old_dir = '/Users/User/Desktop/MyFolder'
_l_(575753)

for f in _c_(575757, _a_(575755, _n_(575754, "os", lambda: os), "listdir"), _n_(575756, "old_dir", lambda: old_dir)):
    _l_(575794)

    file_name, file_ext = _c_(575762, _a_(575760, _a_(575759, _n_(575758, "os", lambda: os), "path"), "splitext"), _n_(575761, "f", lambda: f))
    _l_(575763)
    _c_(575766, _a_(575765, _n_(575764, "file_name", lambda: file_name), "split"), '-')
    _l_(575767)

    split_file_name = _c_(575770, _a_(575769, _n_(575768, "file_name", lambda: file_name), "split"), '-')
    _l_(575771)

    new_dir = _c_(575781, _a_(575774, _a_(575773, _n_(575772, "os", lambda: os), "path"), "join"), _n_(575775, "old_dir", lambda: old_dir),
                           _c_(575778, _a_(575776, '-', "join"), _n_(575777, "split_file_name", lambda: split_file_name)[:3]),
                           _n_(575779, "split_file_name", lambda: split_file_name)[5],
                           _n_(575780, "f", lambda: f))
    _l_(575782)

    _c_(575792, _a_(575784, _n_(575783, "os", lambda: os), "rename"), _c_(575790, _a_(575787, _a_(575786, _n_(575785, "os", lambda: os), "path"), "join"), _n_(575788, "old_dir", lambda: old_dir), _n_(575789, "f", lambda: f)), _n_(575791, "new_dir", lambda: new_dir))
    _l_(575793)