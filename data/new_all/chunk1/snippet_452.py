# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54719893/why-unbound-local-error-is-showing-up-where-i-expect-nameerror-should-be-raised
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def func():
    _l_(408050)

    x=10
    _l_(408044)
    del x
    _l_(408045)
    _c_(408048, _n_(408046, "print", lambda: print), _n_(408047, "x", lambda: x))
    _l_(408049)
_c_(408052, _n_(408051, "func", lambda: func)) #this will cause UnboundLocal Error
_l_(408053) #this will cause UnboundLocal Error

#But if i copy the same code and execute it without using the function call then NameError shows up

x=10
_l_(408054)
del x
_l_(408055)
_c_(408058, _n_(408056, "print", lambda: print), _n_(408057, "x", lambda: x)) #this will raise NameError as x does not exist
_l_(408059) #this will raise NameError as x does not exist