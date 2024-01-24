# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66487695/getting-nameerror-while-i-already-have-defined-the-name-classes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Restaurants():
    _l_(591946)

    """Practicing classes."""
    def __init__(self,name,cuisine):
        _l_(591925)

        _n_(591919, "self", lambda: self).name = _n_(591920, "name", lambda: name)
        _l_(591921)
        _n_(591922, "self", lambda: self).cuisine = _n_(591923, "cuisine", lambda: cuisine)
        _l_(591924)

    def restaurantInfo(self):
        _l_(591938)

        _c_(591930, _n_(591926, "print", lambda: print), "The restaurant's name is: "+_c_(591929, _a_(591928, _n_(591927, "name", lambda: name), "title"))+".")
        _l_(591931)
        _c_(591936, _n_(591932, "print", lambda: print), "The restaurant's cuisine type is: "+_c_(591935, _a_(591934, _n_(591933, "cuisine", lambda: cuisine), "title"))+".")
        _l_(591937)
    
    def rOpen(self):
        _l_(591945)

        _c_(591943, _n_(591939, "print", lambda: print), _c_(591942, _a_(591941, _n_(591940, "name", lambda: name), "title"))+" is open 24/7.")
        _l_(591944)

restaurant = _c_(591948, _n_(591947, "Restaurants", lambda: Restaurants), 'habibi','fast food')
_l_(591949)
_c_(591955, _n_(591950, "print", lambda: print), _c_(591954, _a_(591953, _a_(591952, _n_(591951, "restaurant", lambda: restaurant), "name"), "title"))+" is the name of our Restaurant.")
_l_(591956)
_c_(591962, _n_(591957, "print", lambda: print), "We serve "+_c_(591961, _a_(591960, _a_(591959, _n_(591958, "restaurant", lambda: restaurant), "cuisine"), "title"))+".")
_l_(591963)
_c_(591966, _a_(591965, _n_(591964, "restaurant", lambda: restaurant), "rOpen"))
_l_(591967)