# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58156230/filenotfounderror-winerror-3-the-system-cannot-find-the-path-specified
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(538461)

except ImportError:
    pass
try:
    from os import listdir
    _l_(538463)

except ImportError:
    pass

for i in _c_(538465, _n_(538464, "range", lambda: range), 9):
    _l_(538494)

    for fld in _n_(538466, "folders", lambda: folders):
        _l_(538492)

        index = _c_(538470, _a_(538468, _n_(538467, "folders", lambda: folders), "index"), _n_(538469, "fld", lambda: fld))
        _l_(538471)
        _c_(538477, _n_(538472, "print", lambda: print), _c_(538476, _a_(538473, 'Load folders {} (Index: {})', "format"), _n_(538474, "fld", lambda: fld), _n_(538475, "index", lambda: index)))
        _l_(538478)
        path = _c_(538483, _a_(538481, _a_(538480, _n_(538479, "os", lambda: os), "path"), "join"), 'Users', 'USER' , 'Desktop','ncfm' 'train', _n_(538482, "fld", lambda: fld), '*.jpg')
        _l_(538484)
        _c_(538490, _a_(538486, _n_(538485, "L", lambda: L), "append"), _c_(538489, _n_(538487, "len", lambda: len), _n_(538488, "path", lambda: path)))
        _l_(538491)


    break
    _l_(538493)