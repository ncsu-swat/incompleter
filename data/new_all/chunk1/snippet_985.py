# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59098355/got-attributeerror-module-faker-providers-en-us-has-no-attribute-provider
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from faker import Faker
    _l_(401049)

except ImportError:
    pass
fake = _c_(401051, _n_(401050, "Faker", lambda: Faker))
_l_(401052)