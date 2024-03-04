# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5574702/how-do-i-print-to-stderr-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(65268, "print", lambda: print) >> _a_(65270, _n_(65269, "sys", lambda: sys), "stderr"), 'spam' 
_l_(65271) 

_c_(65275, _n_(65272, "print", lambda: print), "spam", file=_a_(65274, _n_(65273, "sys", lambda: sys), "stderr")) 
_l_(65276) 

