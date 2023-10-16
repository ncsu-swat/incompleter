# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1894269/how-to-convert-string-representation-of-list-to-a-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x = '[ "A","B","C" , " D"]'
_l_(1539210)
[_c_(1539213, _a_(1539212, _n_(1539211, "i", lambda: i), "strip")) for i in _c_(1539216, _a_(1539215, _n_(1539214, "x", lambda: x), "split"), '"') if _c_(1539227, _n_(1539217, "len", lambda: len), _c_(1539226, _a_(1539225, _c_(1539224, _a_(1539223, _c_(1539222, _a_(1539221, _c_(1539220, _a_(1539219, _n_(1539218, "i", lambda: i), "strip")), "strip"), ','), "strip"), ']'), "strip"), '['))>0]
_l_(1539228)

['A', 'B', 'C', 'D']
_l_(1539229)

