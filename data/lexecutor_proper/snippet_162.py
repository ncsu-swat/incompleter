# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists
# Search for entry.
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for x in _n_(61851, "y", lambda: y):
  _l_(61856)

  if _n_(61852, "x", lambda: x) == 3:
    _l_(61855)

    found = _n_(61853, "x", lambda: x)
    _l_(61854)

# Work with found entry.
try:
  _l_(61869)

  _c_(61861, _n_(61857, "print", lambda: print), _c_(61860, _a_(61858, 'Found: {0}', "format"), _n_(61859, "found", lambda: found)))
  _l_(61862)
except _n_(61863, "NameError", lambda: NameError):
  _l_(61867)

  _c_(61865, _n_(61864, "print", lambda: print), 'Not found')
  _l_(61866)
else:
  # Handle rest of Found case here
  ...
  _l_(61868)

