# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/10458437/what-is-the-difference-between-dict-items-and-dict-iteritems-in-python2
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
dict = {_n_(62430, "i", lambda: i): _n_(62431, "i", lambda: i) * 2 for i in _c_(62433, _n_(62432, "xrange", lambda: xrange), 10000000)}  
_l_(62434)  
# Slow and memory hungry.
for key, value in _c_(62437, _a_(62436, _n_(62435, "dict", lambda: dict), "items")):
    _l_(62443)

    _c_(62441, _n_(62438, "print", lambda: print), _n_(62439, "key", lambda: key),":",_n_(62440, "value", lambda: value))
    _l_(62442)

dict = {_n_(62444, "i", lambda: i): _n_(62445, "i", lambda: i) * 2 for i in _c_(62447, _n_(62446, "xrange", lambda: xrange), 10000000)}  
_l_(62448)  
# More memory efficient.
for key, value in _c_(62451, _a_(62450, _n_(62449, "dict", lambda: dict), "iteritems")):
    _l_(62457)

    _c_(62455, _n_(62452, "print", lambda: print), _n_(62453, "key", lambda: key),":",_n_(62454, "value", lambda: value))
    _l_(62456)

