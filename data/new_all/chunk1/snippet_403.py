# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/30099542/mmap-typeerror-str-does-not-support-the-buffer-interface-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
f = _c_(407987, _n_(407986, "open", lambda: open), 'C:\Python33\File.doc')
_l_(407988)
s = _c_(407996, _a_(407990, _n_(407989, "mmap", lambda: mmap), "mmap"), _c_(407993, _a_(407992, _n_(407991, "f", lambda: f), "fileno")), 0, access=_a_(407995, _n_(407994, "mmap", lambda: mmap), "ACCESS_READ"))
_l_(407997)
if _c_(408000, _a_(407999, _n_(407998, "s", lambda: s), "find"), "blabla") != -1:
    _l_(408004)

    _c_(408002, _n_(408001, "print", lambda: print), "True")
    _l_(408003)