# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/251464/how-to-get-a-function-name-as-a-string
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
   import inspect
   _l_(1545497)

except ImportError:
   pass

def foo():
   _l_(1545504)

   _c_(1545502, _n_(1545498, "print", lambda: print), _c_(1545501, _a_(1545500, _n_(1545499, "inspect", lambda: inspect), "stack"))[0][3])
   _l_(1545503)

