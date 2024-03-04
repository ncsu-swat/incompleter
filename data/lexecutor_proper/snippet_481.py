# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/10840533/most-pythonic-way-to-delete-a-file-which-may-not-exist
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    _l_(63246)

    _c_(63241, _a_(63239, _n_(63238, "os", lambda: os), "remove"), _n_(63240, "filename", lambda: filename))
    _l_(63242)
except _n_(63243, "FileNotFoundError", lambda: FileNotFoundError):
    _l_(63245)

    pass
    _l_(63244)

