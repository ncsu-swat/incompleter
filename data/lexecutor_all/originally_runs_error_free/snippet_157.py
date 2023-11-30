# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6159900/correct-way-to-write-line-to-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
filehandle = _c_(1541895, _n_(1541894, "open", lambda: open), "text.txt", "w")
_l_(1541896)
filebuffer = ["hi","welcome","yes yes welcome"]
_l_(1541897)
_c_(1541901, _a_(1541899, _n_(1541898, "filehandle", lambda: filehandle), "writelines"), _n_(1541900, "filebuffer", lambda: filebuffer))
_l_(1541902)
_c_(1541905, _a_(1541904, _n_(1541903, "filehandle", lambda: filehandle), "close"))
_l_(1541906)

