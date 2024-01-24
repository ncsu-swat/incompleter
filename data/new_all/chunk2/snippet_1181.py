# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56838221/filenotfounderror-when-trying-to-use-os-rename
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(454546)

except ImportError:
    pass
n = 2000
_l_(454547)

folder = r"Z:/AAA/BBB/"
_l_(454548)
_c_(454552, _a_(454550, _n_(454549, "os", lambda: os), "chdir"), _n_(454551, "folder", lambda: folder))
_l_(454553)

saved_path = _c_(454556, _a_(454555, _n_(454554, "os", lambda: os), "getcwd"))
_l_(454557)
_c_(454560, _n_(454558, "print", lambda: print), "CWD is" + _n_(454559, "saved_path", lambda: saved_path))
_l_(454561)

for i in _c_(454564, _n_(454562, "range", lambda: range), 1,_n_(454563, "n", lambda: n)):
    _l_(454589)

    old_file = _c_(454572, _a_(454567, _a_(454566, _n_(454565, "os", lambda: os), "path"), "join"), _n_(454568, "folder", lambda: folder), "xxx_(" + _c_(454571, _n_(454569, "str", lambda: str), _n_(454570, "i", lambda: i)) + ").bmp")
    _l_(454573)
    new_file = _c_(454581, _a_(454576, _a_(454575, _n_(454574, "os", lambda: os), "path"), "join"), _n_(454577, "folder", lambda: folder), "xxx_" +_c_(454580, _n_(454578, "str", lambda: str), _n_(454579, "i", lambda: i))+ ".bmp")
    _l_(454582)
    _c_(454587, _a_(454584, _n_(454583, "os", lambda: os), "rename"), _n_(454585, "old_file", lambda: old_file), _n_(454586, "new_file", lambda: new_file))
    _l_(454588)
_c_(454591, _n_(454590, "print", lambda: print), 'renamed files')
_l_(454592)