# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57982592/attributeerror-event-object-has-no-attribute-setevent
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from event import *
    _l_(374320)

except ImportError:
    pass
#First Try:
_c_(374324, _a_(374323, _c_(374322, _n_(374321, "Event", lambda: Event)), "setEvent"), "error","This is an error")
_l_(374325)
#Second Try:
a=_c_(374327, _n_(374326, "Event", lambda: Event))
_l_(374328)
_c_(374331, _a_(374330, _n_(374329, "a", lambda: a), "setEvent"), "error","This is an error")
_l_(374332)