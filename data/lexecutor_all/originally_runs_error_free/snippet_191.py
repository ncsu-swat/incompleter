# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import timeit
    _l_(1539820)

except ImportError:
    pass
_c_(1539825, _n_(1539821, "print", lambda: print), _c_(1539824, _a_(1539823, _n_(1539822, "timeit", lambda: timeit), "timeit"), stmt='[1,2,3,4,5,6,7,8,9,10]', number=1000000)) #created list
_l_(1539826) #created list
_c_(1539831, _n_(1539827, "print", lambda: print), _c_(1539830, _a_(1539829, _n_(1539828, "timeit", lambda: timeit), "timeit"), stmt='(1,2,3,4,5,6,7,8,9,10)', number=1000000)) # created tuple 
_l_(1539832) # created tuple 

0.136621
_l_(1539833)
0.013722200000000018
_l_(1539834)

