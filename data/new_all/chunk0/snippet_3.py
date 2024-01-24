# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/13906623/using-pickle-dump-typeerror-must-be-str-not-bytes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(48373)

except ImportError:
    pass
try:
    import pickle
    _l_(48375)

except ImportError:
    pass
try:
    from pickle import *
    _l_(48377)

except ImportError:
    pass
_c_(48380, _a_(48379, _n_(48378, "os", lambda: os), "chdir"), 'c:/Python26/progfiles/')
_l_(48381)

def storvars(vdict):
    _l_(48396)

    f = _c_(48383, _n_(48382, "open", lambda: open), 'varstor.txt','w')
    _l_(48384)
    _c_(48389, _a_(48386, _n_(48385, "pickle", lambda: pickle), "dump"), _n_(48387, "vdict", lambda: vdict),_n_(48388, "f", lambda: f),)
    _l_(48390)
    _c_(48393, _a_(48392, _n_(48391, "f", lambda: f), "close"))
    _l_(48394)
    aux = ""
    _l_(48395)
    return aux

mydict = {'name':'john','gender':'male','age':'45'}
_l_(48397)
_c_(48400, _n_(48398, "storvars", lambda: storvars), _n_(48399, "mydict", lambda: mydict))
_l_(48401)