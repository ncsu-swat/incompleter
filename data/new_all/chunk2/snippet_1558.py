# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/18872502/tarfile-addfile-gives-error-typeerror-str-does-not-support-the-buffer-interf
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from io import StringIO
    _l_(445959)

except ImportError:
    pass
try:
    import tarfile
    _l_(445961)

except ImportError:
    pass

archive_files = []
_l_(445962)

data = ["DATA1 "]
_l_(445963)
_c_(445966, _a_(445965, _n_(445964, "data", lambda: data), "append"), "DATA2 ")
_l_(445967)
_c_(445973, _a_(445969, _n_(445968, "archive_files", lambda: archive_files), "append"), ("FILE.txt", _c_(445972, _a_(445970, "\n", "join"), _n_(445971, "data", lambda: data))))
_l_(445974)

tar = _c_(445977, _a_(445976, _n_(445975, "tarfile", lambda: tarfile), "open"), "file.tar", "w:tar")
_l_(445978)
for name, data in _n_(445979, "archive_files", lambda: archive_files):
    _l_(445998)

    info = _c_(445983, _a_(445981, _n_(445980, "tarfile", lambda: tarfile), "TarInfo"), _n_(445982, "name", lambda: name))
    _l_(445984)
    _n_(445985, "info", lambda: info).size = _c_(445988, _n_(445986, "len", lambda: len), _n_(445987, "data", lambda: data))
    _l_(445989)
    _c_(445996, _a_(445991, _n_(445990, "tar", lambda: tar), "addfile"), _n_(445992, "info", lambda: info), _c_(445995, _n_(445993, "StringIO", lambda: StringIO), _n_(445994, "data", lambda: data)))
    _l_(445997)
_c_(446001, _a_(446000, _n_(445999, "tar", lambda: tar), "close"))
_l_(446002)