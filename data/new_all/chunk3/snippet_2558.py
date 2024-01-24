# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71710269/reading-data-from-a-csv-file-yields-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(530905)

except ImportError:
    pass
uncov_users = _c_(530908, _a_(530907, _n_(530906, "np", lambda: np), "genfromtxt"), 'ucov_users.csv', delimiter=',')
_l_(530909)
for i,j in _n_(530910, "uncov_users", lambda: uncov_users):
    _l_(530920)

    ux_coor = _n_(530911, "i", lambda: i)  
    _l_(530912)  
    uy_coor = _n_(530913, "j", lambda: j)  
    _l_(530914)  
    _c_(530918, _n_(530915, "print", lambda: print), _n_(530916, "ux_coor", lambda: ux_coor),_n_(530917, "uy_coor", lambda: uy_coor))
    _l_(530919)