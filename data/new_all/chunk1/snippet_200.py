# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43274942/falcon-attributeerror-api-object-has-no-attribute-create
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import falcon
    _l_(377539)

except ImportError:
    pass
try:
    from resources.static import StaticResource
    _l_(377541)

except ImportError:
    pass


api = _c_(377544, _a_(377543, _n_(377542, "falcon", lambda: falcon), "API"))
_l_(377545)
_c_(377550, _a_(377547, _n_(377546, "api", lambda: api), "add_route"), '/', _c_(377549, _n_(377548, "StaticResource", lambda: StaticResource)))
_l_(377551)