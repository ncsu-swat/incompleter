# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5658369/how-to-input-a-regex-in-string-replace
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(64020)

except ImportError:
    pass
line = _c_(64024, _a_(64022, _n_(64021, "re", lambda: re), "sub"), r"</?\[\d+>", "", _n_(64023, "line", lambda: line))
_l_(64025)

line = _c_(64029, _a_(64027, _n_(64026, "re", lambda: re), "sub"), r"""
  (?x) # Use free-spacing mode.
  <    # Match a literal '<'
  /?   # Optionally match a '/'
  \[   # Match a literal '['
  \d+  # Match one or more digits
  >    # Match a literal '>'
  """, "", _n_(64028, "line", lambda: line))
_l_(64030)

