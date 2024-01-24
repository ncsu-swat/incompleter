# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64043109/getting-typeerror-write-argument-must-be-str-not-list-when-trying-to-add-tex
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(564615, _n_(564614, "open", lambda: open), "text1.txt", "r") as f1:
    _l_(564620)

    t1 = _c_(564618, _a_(564617, _n_(564616, "f1", lambda: f1), "readlines"))
    _l_(564619)
with _c_(564622, _n_(564621, "open", lambda: open), "text2.txt", "r") as f2:
    _l_(564627)

    t2 = _c_(564625, _a_(564624, _n_(564623, "f2", lambda: f2), "readlines"))
    _l_(564626)
_c_(564631, _a_(564629, _n_(564628, "t2", lambda: t2), "insert"), 2, _n_(564630, "t1", lambda: t1))
_l_(564632)
with _c_(564634, _n_(564633, "open", lambda: open), "text2.txt", "w") as f2:
    _l_(564640)

    _c_(564638, _a_(564636, _n_(564635, "f2", lambda: f2), "writelines"), _n_(564637, "t2", lambda: t2))
    _l_(564639)