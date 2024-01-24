# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66775462/error-typeerror-a-bytes-like-object-is-required-not-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
oldfile = _c_(407489, _n_(407488, "open", lambda: open), "buscrash_diversion.uexp", "rb")
_l_(407490)
l = _c_(407495, _n_(407491, "list", lambda: list), _c_(407494, _a_(407493, _n_(407492, "oldfile", lambda: oldfile), "read")))
_l_(407496)
out = _c_(407498, _n_(407497, "open", lambda: open), "1", "wb")
_l_(407499)
for i in _n_(407500, "l", lambda: l):
    _l_(407506)

    _c_(407504, _a_(407502, _n_(407501, "out", lambda: out), "write"), _n_(407503, "i", lambda: i))
    _l_(407505)