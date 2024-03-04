# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1373164/how-do-i-create-variable-variables
# using dictionary
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
variables = {}
_l_(63793)
_n_(63794, "variables", lambda: variables)["first"] = 34
_l_(63795)
_n_(63796, "variables", lambda: variables)["second"] = 45
_l_(63797)
_c_(63801, _n_(63798, "print", lambda: print), _n_(63799, "variables", lambda: variables)["first"], _n_(63800, "variables", lambda: variables)["second"])
_l_(63802)

# using namedtuple
Variables = _c_(63804, _n_(63803, "namedtuple", lambda: namedtuple), 'Variables', ['first', 'second'])
_l_(63805)
vars = _c_(63807, _n_(63806, "Variables", lambda: Variables), 34, 45)
_l_(63808)
_c_(63814, _n_(63809, "print", lambda: print), _a_(63811, _n_(63810, "vars", lambda: vars), "first"), _a_(63813, _n_(63812, "vars", lambda: vars), "second"))
_l_(63815)

