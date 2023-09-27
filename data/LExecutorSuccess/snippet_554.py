# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(1543144)

except ImportError:
    pass

_c_(1543148, _a_(1543147, _a_(1543146, _n_(1543145, "sys", lambda: sys), "stdout"), "write"), "-") # prints a dash for each iteration of loop
_l_(1543149) # prints a dash for each iteration of loop
_c_(1543153, _a_(1543152, _a_(1543151, _n_(1543150, "sys", lambda: sys), "stdout"), "flush")) # ensures bar is displayed incrementally
_l_(1543154) # ensures bar is displayed incrementally

