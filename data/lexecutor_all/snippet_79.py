# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4706499/how-do-i-append-to-a-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(1548785, _n_(1548784, "open", lambda: open), "foo", "a") as f:
    _l_(1548790)

    _c_(1548788, _a_(1548787, _n_(1548786, "f", lambda: f), "write"), "cool beans...")
    _l_(1548789)

