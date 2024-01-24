# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53861239/getting-no-attribute-error-attribute-seems-to-be-there
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from random import choice
    _l_(368434)

except ImportError:
    pass

class RandomWalk():
    _l_(368493)

    """A class to generate random walks."""

    def _init_(self, num_points=5000):
        _l_(368442)

        """ Initialize attributes of a walk."""
        _n_(368435, "self", lambda: self).num_points = _n_(368436, "num_points", lambda: num_points)
        _l_(368437)

        _n_(368438, "self", lambda: self).x_values = [0]
        _l_(368439)
        _n_(368440, "self", lambda: self).y_values = [0]
        _l_(368441)


    def fill_walk(self):
        _l_(368492)

        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length
        while _c_(368446, _n_(368443, "len", lambda: len), _a_(368445, _n_(368444, "self", lambda: self), "x_values")) < _a_(368448, _n_(368447, "self", lambda: self), "num_points"):
            _l_(368491)

            # Decide which direction to go and how far to go in that direction
            x_direction = _c_(368450, _n_(368449, "choice", lambda: choice), [1,-1])
            _l_(368451)
            x_distance = _c_(368453, _n_(368452, "choice", lambda: choice), [0, 1, 2, 3, 4])
            _l_(368454)
            x_step = _n_(368455, "x_direction", lambda: x_direction) * _n_(368456, "x_distance", lambda: x_distance)
            _l_(368457)

            y_direction = _c_(368459, _n_(368458, "choice", lambda: choice), [1,-1])
            _l_(368460)
            y_distance = _c_(368462, _n_(368461, "choice", lambda: choice), [0, 1, 2, 3, 4])
            _l_(368463)
            y_step = _n_(368464, "y_direction", lambda: y_direction) * _n_(368465, "y_distance", lambda: y_distance)
            _l_(368466)

            # Reject moves that go nowhere
            if _n_(368467, "x_step", lambda: x_step) == 0 and _n_(368468, "y_step", lambda: y_step) == 0:
                _l_(368470)

                continue
                _l_(368469)

            # Calculate the next x and y values
            next_x = _a_(368472, _n_(368471, "self", lambda: self), "x_values")[-1] + _n_(368473, "x_step", lambda: x_step)
            _l_(368474)
            next_y = _a_(368476, _n_(368475, "self", lambda: self), "y_values")[-1] + _n_(368477, "y_step", lambda: y_step)
            _l_(368478)

            _c_(368483, _a_(368481, _a_(368480, _n_(368479, "self", lambda: self), "x_values"), "append"), _n_(368482, "next_x", lambda: next_x))
            _l_(368484)
            _c_(368489, _a_(368487, _a_(368486, _n_(368485, "self", lambda: self), "y_values"), "append"), _n_(368488, "next_y", lambda: next_y))
            _l_(368490)
try:
    import matplotlib.pyplot as plt
    _l_(368495)

except ImportError:
    pass
try:
    from random_walk import RandomWalk
    _l_(368497)

except ImportError:
    pass

# Make a random walk, and plot the pointsself.

rw = _c_(368499, _n_(368498, "RandomWalk", lambda: RandomWalk))
_l_(368500)
_c_(368503, _a_(368502, _n_(368501, "rw", lambda: rw), "fill_walk"))
_l_(368504)

_c_(368511, _a_(368506, _n_(368505, "plt", lambda: plt), "scatter"), _a_(368508, _n_(368507, "rw", lambda: rw), "x_values"), _a_(368510, _n_(368509, "rw", lambda: rw), "y_values"), s=15)
_l_(368512)
_c_(368515, _a_(368514, _n_(368513, "plt", lambda: plt), "show"))
_l_(368516)