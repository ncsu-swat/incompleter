# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57134703/why-this-reload-fails-with-nameerror-name-xxx-is-not-defined
#file: attempt2.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(542223)

except ImportError:
    pass
try:
    from time import sleep
    _l_(542225)

except ImportError:
    pass
try:
    from importlib import reload
    _l_(542227)

except ImportError:
    pass
try:
    from foo_module import foo
    _l_(542229)

except ImportError:
    pass

#Lets see if the module is loaded
_c_(542233, _n_(542230, "print", lambda: print), _a_(542232, _n_(542231, "sys", lambda: sys), "modules")['foo_module']) 
_l_(542234) 

while True:
    _l_(542245)

    _c_(542236, _n_(542235, "foo", lambda: foo))
    _l_(542237)

    #simulate a delay or a condition by when foo_module would have changed
    _c_(542239, _n_(542238, "sleep", lambda: sleep), 2)
    _l_(542240)

    #try to reload foo_module to get the latest
    _c_(542243, _n_(542241, "reload", lambda: reload), _n_(542242, "foo_module", lambda: foo_module)) #FAILS !
    _l_(542244) #FAILS !