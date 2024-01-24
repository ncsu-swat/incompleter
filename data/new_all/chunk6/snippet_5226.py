# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55288202/adding-uuid-type-to-cerberus-leads-to-bad-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cerberus
    _l_(345968)

except ImportError:
    pass
try:
    import uuid
    _l_(345970)

except ImportError:
    pass


class Validator(_a_(345972, _n_(345971, "cerberus", lambda: cerberus), "Validator")):
    _l_(345982)

    types_mapping = {
        **_a_(345975, _a_(345974, _n_(345973, "cerberus", lambda: cerberus), "Validator"), "types_mapping"),
        'UUID': _c_(345980, _a_(345977, _n_(345976, "cerberus", lambda: cerberus), "TypeDefinition"), 'UUID', (_a_(345979, _n_(345978, "uuid", lambda: uuid), "UUID"),), ())
    }
    _l_(345981)