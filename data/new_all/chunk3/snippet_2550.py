# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65279235/attributeerror-fileinput-object-has-no-attribute-read
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import fileinput
    _l_(566198)

except ImportError:
    pass
try:
    import json
    _l_(566200)

except ImportError:
    pass

with _c_(566203, _a_(566202, _n_(566201, "fileinput", lambda: fileinput), "input"), files=('bot_details.json')) as f:
    _l_(566211)

    my_load = _c_(566207, _a_(566205, _n_(566204, "json", lambda: json), "load"), _n_(566206, "f", lambda: f))
    _l_(566208)
    TOKEN=_n_(566209, "my_load", lambda: my_load)["TOKEN"]
    _l_(566210)