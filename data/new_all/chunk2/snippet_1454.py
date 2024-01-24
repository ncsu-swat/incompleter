# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56514847/attributeerror-module-math-has-no-attribute-name
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import math
    _l_(465234)

except ImportError:
    pass

tmpl="This {mod._name_} module defines the value of pie as  {mod.pi}"
_l_(465235)

_c_(465241, _n_(465236, "print", lambda: print), _c_(465240, _a_(465238, _n_(465237, "tmpl", lambda: tmpl), "format"), mod=_n_(465239, "math", lambda: math)))
_l_(465242)