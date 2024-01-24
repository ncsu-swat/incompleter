# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48459963/nameerror-name-x-is-not-defined-x-declared-in-for-loop
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
list_keywords=['DROP','CREATE','ALTER','COMMENT']
_l_(472717)
file=_c_(472720, _n_(472718, "open", lambda: open), _n_(472719, "filename", lambda: filename))
_l_(472721)
for line in _n_(472722, "file", lambda: file):
    _l_(472735)

    if _c_(472729, _n_(472723, "any", lambda: any), (_n_(472724, "x", lambda: x) in _c_(472727, _a_(472726, _n_(472725, "line", lambda: line), "upper")) for x in _n_(472728, "list_keywords", lambda: list_keywords))):
        _l_(472734)

        _c_(472732, _n_(472730, "print", lambda: print), _n_(472731, "line", lambda: line))
        _l_(472733)