# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49933153/how-can-i-fix-this-typeerror-int-object-is-not-iterable-when-counting-the-alp
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x=0
_l_(568651)
f=_c_(568653, _n_(568652, "open", lambda: open), 'in_a.txt',encoding='utf-8')
_l_(568654)
for line in _n_(568655, "f", lambda: f):
    _l_(568667)

    h = _c_(568658, _n_(568656, "len", lambda: len), _n_(568657, "line", lambda: line))
    _l_(568659)
    for i in _n_(568660, "h", lambda: h):
        _l_(568666)

        if _n_(568661, "line", lambda: line) =="a"or _n_(568662, "line", lambda: line) == "A":
            _l_(568665)

            x+=1
            _l_(568663)
            continue
            _l_(568664)
_c_(568670, _n_(568668, "print", lambda: print), "this documents have%d A or a characters"  %_n_(568669, "x", lambda: (x)))
_l_(568671)