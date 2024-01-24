# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61573953/attributeerror-list-object-has-no-attribute-startswith
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
_l_(459524)

for city_m in _n_(459525, "cities", lambda: cities):
    _l_(459537)

    if _c_(459528, _a_(459527, _n_(459526, "cities", lambda: cities), "startswith"), "M"):
        _l_(459536)

        _c_(459531, _n_(459529, "print", lambda: print), "Cities that start with M:", _n_(459530, "cities", lambda: cities))
        _l_(459532)
    else:
        _c_(459534, _n_(459533, "print", lambda: print), "No cities start with M.")
        _l_(459535)