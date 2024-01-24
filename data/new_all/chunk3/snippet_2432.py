# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40110816/attributeerror-nonetype-object-has-no-attribute-recv
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sys import argv
    _l_(549183)

except ImportError:
    pass
try:
    from src.bot import *
    _l_(549185)

except ImportError:
    pass
try:
    from src.config.config import *
    _l_(549187)

except ImportError:
    pass

bot = _c_(549192, _a_(549191, _c_(549190, _n_(549188, "PartyMachine", lambda: PartyMachine), _n_(549189, "config", lambda: config)), "sock"))
_l_(549193)