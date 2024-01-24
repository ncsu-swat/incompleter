# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53402504/cant-loop-the-distance-between-two-locations-typeerror-numpy-float64-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
coords_1 = (_n_(396907, "lat", lambda: lat)[0][3], _n_(396908, "lang", lambda: lang)[0][3])
_l_(396909)
coords_2 = (_n_(396910, "lat", lambda: lat)[0][5], _n_(396911, "lang", lambda: lang)[0][5])
_l_(396912)
_c_(396921, _n_(396913, "print", lambda: print), _a_(396920, _c_(396919, _a_(396916, _a_(396915, _n_(396914, "geopy", lambda: geopy), "distance"), "distance"), _n_(396917, "coords_1", lambda: coords_1), _n_(396918, "coords_2", lambda: coords_2)), "km"))
_l_(396922)