# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61808747/filenotfounderror-winerror-3-when-using-two-concatenated-strings
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
DIR = r"D:/My/Directory"
_l_(421667)
classes = ['itemA', 'itemB']
_l_(421668)


for item in _n_(421669, "classes", lambda: classes):
    _l_(421682)

    for scope in ["training/", "testing/"]:
        _l_(421681)

        _c_(421679, _a_(421671, _n_(421670, "os", lambda: os), "mkdir"), _c_(421678, _a_(421674, _a_(421673, _n_(421672, "os", lambda: os), "path"), "join"), _n_(421675, "DIR", lambda: DIR), _n_(421676, "scope", lambda: scope) + _n_(421677, "item", lambda: item)))
        _l_(421680)