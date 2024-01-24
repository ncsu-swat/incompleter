# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54472631/getting-typeerror-trying-to-sum-the-contents-of-a-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
ctn =0
_l_(368561)
myfile = _c_(368563, _n_(368562, "open", lambda: open), "lab3.txt")
_l_(368564)
lines = _a_(368566, _n_(368565, "myfile", lambda: myfile), "readlines")
_l_(368567)
for item in _n_(368568, "myfile", lambda: myfile):
        _l_(368571)

        ctn += _n_(368569, "item", lambda: item)
        _l_(368570)
_c_(368576, _n_(368572, "print", lambda: print), _c_(368575, _n_(368573, "int", lambda: int), _n_(368574, "ctn", lambda: ctn)))
_l_(368577)