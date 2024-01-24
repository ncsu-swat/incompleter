# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/13906623/using-pickle-dump-typeerror-must-be-str-not-bytes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(396647)

except ImportError:
    pass
try:
    import pickle
    _l_(396649)

except ImportError:
    pass
try:
    from pickle import *
    _l_(396651)

except ImportError:
    pass
_c_(396654, _a_(396653, _n_(396652, "os", lambda: os), "chdir"), 'c:/Python26/progfiles/')
_l_(396655)

def storvars(vdict):
    _l_(396670)

    f = _c_(396657, _n_(396656, "open", lambda: open), 'varstor.txt','w')
    _l_(396658)
    _c_(396663, _a_(396660, _n_(396659, "pickle", lambda: pickle), "dump"), _n_(396661, "vdict", lambda: vdict),_n_(396662, "f", lambda: f),)
    _l_(396664)
    _c_(396667, _a_(396666, _n_(396665, "f", lambda: f), "close"))
    _l_(396668)
    aux = ""
    _l_(396669)
    return aux

mydict = {'name':'john','gender':'male','age':'45'}
_l_(396671)
_c_(396674, _n_(396672, "storvars", lambda: storvars), _n_(396673, "mydict", lambda: mydict))
_l_(396675)