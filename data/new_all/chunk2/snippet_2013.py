# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69817812/python-pickle-throws-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(464139)

except ImportError:
    pass
try:
    import pickle
    _l_(464141)

except ImportError:
    pass
try:
    from pickle import *
    _l_(464143)

except ImportError:
    pass
_c_(464146, _a_(464145, _n_(464144, "os", lambda: os), "chdir"), 'c:/Python26/progfiles/')
_l_(464147)

def storvars(vdict):
    _l_(464162)

    f = _c_(464149, _n_(464148, "open", lambda: open), 'varstor.txt','w')
    _l_(464150)
    _c_(464155, _a_(464152, _n_(464151, "pickle", lambda: pickle), "dump"), _n_(464153, "vdict", lambda: vdict),_n_(464154, "f", lambda: f),)
    _l_(464156)
    _c_(464159, _a_(464158, _n_(464157, "f", lambda: f), "close"))
    _l_(464160)
    aux = ""
    _l_(464161)
    return aux

mydict = {'name':'john','gender':'male','age':'45'}
_l_(464163)
_c_(464166, _n_(464164, "storvars", lambda: storvars), _n_(464165, "mydict", lambda: mydict))
_l_(464167)