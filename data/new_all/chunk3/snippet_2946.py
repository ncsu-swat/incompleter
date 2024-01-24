# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57134703/why-this-reload-fails-with-nameerror-name-xxx-is-not-defined
#file: attempt1.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(545923)

except ImportError:
    pass
try:
    from time import sleep
    _l_(545925)

except ImportError:
    pass
try:
    from importlib import reload
    _l_(545927)

except ImportError:
    pass
try:
    import foo_module
    _l_(545929)

except ImportError:
    pass

_c_(545933, _n_(545930, "print", lambda: print), _a_(545932, _n_(545931, "sys", lambda: sys), "modules")['foo_module']) #Lets see if the module is loaded
_l_(545934) #Lets see if the module is loaded
while True:
    _l_(545946)

    _c_(545937, _a_(545936, _n_(545935, "foo_module", lambda: foo_module), "foo"))
    _l_(545938)

    #simulate a delay or a condition by when foo_module would have changed
    _c_(545940, _n_(545939, "sleep", lambda: sleep), 2)
    _l_(545941)

    #should reload foo_module to get the latest
    _c_(545944, _n_(545942, "reload", lambda: reload), _n_(545943, "foo_module", lambda: foo_module))
    _l_(545945)