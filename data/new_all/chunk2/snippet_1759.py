# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57877513/attributeerror-tuple-object-has-no-attribute-replace-for-brackets
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(450809)

except ImportError:
    pass
_c_(450812, _a_(450811, _n_(450810, "os", lambda: os), "chdir"), "/home/ubuntu/Desktop")
_l_(450813)
nfiles=_c_(450819, _a_(450815, _n_(450814, "os", lambda: os), "listdir"), _c_(450818, _a_(450817, _n_(450816, "os", lambda: os), "getcwd")))
_l_(450820)
new_files = [_n_(450821, "nfile", lambda: nfile) for nfile in _n_(450822, "nfiles", lambda: nfiles) if _c_(450825, _a_(450824, _n_(450823, "nfile", lambda: nfile)[-4:], "lower"))=='.txt']
_l_(450826)

for file in _n_(450827, "new_files", lambda: new_files):
    _l_(450838)


    name = _n_(450828, "file", lambda: file)
    _l_(450829)
    name=_n_(450830, "name", lambda: name).replace=(")","")
    _l_(450831)
    name=_n_(450832, "name", lambda: name).replace=(",","_")
    _l_(450833)
    _c_(450836, _n_(450834, "print", lambda: print), _n_(450835, "name", lambda: name))
    _l_(450837)