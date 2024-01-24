# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53861239/getting-no-attribute-error-attribute-seems-to-be-there
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from random import choice
    _l_(337497)

except ImportError:
    pass

class RandomWalk():
    _l_(337556)

    """A class to generate random walks."""

    def _init_(self, num_points=5000):
        _l_(337505)

        """ Initialize attributes of a walk."""
        _n_(337498, "self", lambda: self).num_points = _n_(337499, "num_points", lambda: num_points)
        _l_(337500)

        _n_(337501, "self", lambda: self).x_values = [0]
        _l_(337502)
        _n_(337503, "self", lambda: self).y_values = [0]
        _l_(337504)


    def fill_walk(self):
        _l_(337555)

        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length
        while _c_(337509, _n_(337506, "len", lambda: len), _a_(337508, _n_(337507, "self", lambda: self), "x_values")) < _a_(337511, _n_(337510, "self", lambda: self), "num_points"):
            _l_(337554)

            # Decide which direction to go and how far to go in that direction
            x_direction = _c_(337513, _n_(337512, "choice", lambda: choice), [1,-1])
            _l_(337514)
            x_distance = _c_(337516, _n_(337515, "choice", lambda: choice), [0, 1, 2, 3, 4])
            _l_(337517)
            x_step = _n_(337518, "x_direction", lambda: x_direction) * _n_(337519, "x_distance", lambda: x_distance)
            _l_(337520)

            y_direction = _c_(337522, _n_(337521, "choice", lambda: choice), [1,-1])
            _l_(337523)
            y_distance = _c_(337525, _n_(337524, "choice", lambda: choice), [0, 1, 2, 3, 4])
            _l_(337526)
            y_step = _n_(337527, "y_direction", lambda: y_direction) * _n_(337528, "y_distance", lambda: y_distance)
            _l_(337529)

            # Reject moves that go nowhere
            if _n_(337530, "x_step", lambda: x_step) == 0 and _n_(337531, "y_step", lambda: y_step) == 0:
                _l_(337533)

                continue
                _l_(337532)

            # Calculate the next x and y values
            next_x = _a_(337535, _n_(337534, "self", lambda: self), "x_values")[-1] + _n_(337536, "x_step", lambda: x_step)
            _l_(337537)
            next_y = _a_(337539, _n_(337538, "self", lambda: self), "y_values")[-1] + _n_(337540, "y_step", lambda: y_step)
            _l_(337541)

            _c_(337546, _a_(337544, _a_(337543, _n_(337542, "self", lambda: self), "x_values"), "append"), _n_(337545, "next_x", lambda: next_x))
            _l_(337547)
            _c_(337552, _a_(337550, _a_(337549, _n_(337548, "self", lambda: self), "y_values"), "append"), _n_(337551, "next_y", lambda: next_y))
            _l_(337553)
try:
    import matplotlib.pyplot as plt
    _l_(337558)

except ImportError:
    pass
try:
    from random_walk import RandomWalk
    _l_(337560)

except ImportError:
    pass

# Make a random walk, and plot the pointsself.

rw = _c_(337562, _n_(337561, "RandomWalk", lambda: RandomWalk))
_l_(337563)
_c_(337566, _a_(337565, _n_(337564, "rw", lambda: rw), "fill_walk"))
_l_(337567)

_c_(337574, _a_(337569, _n_(337568, "plt", lambda: plt), "scatter"), _a_(337571, _n_(337570, "rw", lambda: rw), "x_values"), _a_(337573, _n_(337572, "rw", lambda: rw), "y_values"), s=15)
_l_(337575)
_c_(337578, _a_(337577, _n_(337576, "plt", lambda: plt), "show"))
_l_(337579)