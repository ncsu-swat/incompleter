# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75518119/typeerror-restaurant-takes-no-arguments
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Restaurant():
    _l_(588592)


    def __int__(self, restaurant_name, cuisine_type):
        _l_(588577)

        _n_(588571, "self", lambda: self).restaurant_name = _n_(588572, "restaurant_name", lambda: restaurant_name)
        _l_(588573)
        _n_(588574, "self", lambda: self).cuisine_type = _n_(588575, "cuisine_type", lambda: cuisine_type)
        _l_(588576)

    def describe_restaurant(self):
        _l_(588585)

        _c_(588583, _n_(588578, "print", lambda: print), f"{_a_(588580, _n_(588579, 'self', lambda: self), 'restaurant_name')} {_a_(588582, _n_(588581, 'self', lambda: self), 'cuisine_type')}")
        _l_(588584)

    def open_restaurant(self):
        _l_(588591)

        _c_(588589, _n_(588586, "print", lambda: print), f"The {_a_(588588, _n_(588587, 'self', lambda: self), 'restaurant_name')} restaurant is opened.")
        _l_(588590)

restaurant = _c_(588594, _n_(588593, "Restaurant", lambda: Restaurant), 'monarch', 'russian cuisine')
_l_(588595)
_c_(588603, _n_(588596, "print", lambda: print), f"{_c_(588600, _a_(588599, _a_(588598, _n_(588597, 'restaurant', lambda: restaurant), 'restaurant_name'), 'title'))} is the best restaurant of {_a_(588602, _n_(588601, 'restaurant', lambda: restaurant), 'cuisine_type')} in Moscow.")
_l_(588604)
_c_(588607, _a_(588606, _n_(588605, "restaurant", lambda: restaurant), "describe_restaurant"))
_l_(588608)
_c_(588611, _a_(588610, _n_(588609, "restaurant", lambda: restaurant), "open_restaurant"))
_l_(588612)