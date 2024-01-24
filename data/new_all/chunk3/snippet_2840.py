# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61292013/matplotlib-doucmentation-example-code-giving-attribute-error-on-axis-plot
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(555723)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(555725)

except ImportError:
    pass
try:
    import matplotlib.animation as animation
    _l_(555727)

except ImportError:
    pass

# Fixing random state for reproducibility
_c_(555731, _a_(555730, _a_(555729, _n_(555728, "np", lambda: np), "random"), "seed"), 19680801)
_l_(555732)


def gen_rand_line(length, dims=2):
    _l_(555764)

    """
    Create a line using a random walk algorithm.

    Parameters
    ----------
    length : int
        The number of points of the line.
    dims : int
        The number of dimensions of the line.
    """
    line_data = _c_(555737, _a_(555734, _n_(555733, "np", lambda: np), "empty"), (_n_(555735, "dims", lambda: dims), _n_(555736, "length", lambda: length)))
    _l_(555738)
    _n_(555739, "line_data", lambda: line_data)[:, 0] = _c_(555744, _a_(555742, _a_(555741, _n_(555740, "np", lambda: np), "random"), "rand"), _n_(555743, "dims", lambda: dims))
    _l_(555745)
    for index in _c_(555748, _n_(555746, "range", lambda: range), 1, _n_(555747, "length", lambda: length)):
        _l_(555761)

        # scaling the random numbers by 0.1 so
        # movement is small compared to position.
        # subtraction by 0.5 is to change the range to [-0.5, 0.5]
        # to allow a line to move backwards.
        step = (_c_(555753, _a_(555751, _a_(555750, _n_(555749, "np", lambda: np), "random"), "rand"), _n_(555752, "dims", lambda: dims)) - 0.5) * 0.1
        _l_(555754)
        _n_(555755, "line_data", lambda: line_data)[:, _n_(555756, "index", lambda: index)] = _n_(555757, "line_data", lambda: line_data)[:, _n_(555758, "index", lambda: index) - 1] + _n_(555759, "step", lambda: step)
        _l_(555760)
    aux = _n_(555762, "line_data", lambda: line_data)
    _l_(555763)
    return aux


def update_lines(num, dataLines, lines):
    _l_(555784)

    for line, data in _c_(555768, _n_(555765, "zip", lambda: zip), _n_(555766, "lines", lambda: lines), _n_(555767, "dataLines", lambda: dataLines)):
        _l_(555781)

        # NOTE: there is no .set_data() for 3 dim data...
        _c_(555773, _a_(555770, _n_(555769, "line", lambda: line), "set_data"), _n_(555771, "data", lambda: data)[0:2, :_n_(555772, "num", lambda: num)])
        _l_(555774)
        _c_(555779, _a_(555776, _n_(555775, "line", lambda: line), "set_3d_properties"), _n_(555777, "data", lambda: data)[2, :_n_(555778, "num", lambda: num)])
        _l_(555780)
    aux = _n_(555782, "lines", lambda: lines)
    _l_(555783)
    return aux


# Attaching 3D axis to the figure
fig = _c_(555787, _a_(555786, _n_(555785, "plt", lambda: plt), "figure"))
_l_(555788)
ax = _c_(555791, _a_(555790, _n_(555789, "fig", lambda: fig), "add_subplot"), projection="3d")
_l_(555792)

# Fifty lines of random 3-D lines
data = [_c_(555794, _n_(555793, "gen_rand_line", lambda: gen_rand_line), 25, 3) for index in _c_(555796, _n_(555795, "range", lambda: range), 50)]
_l_(555797)


# Creating fifty line objects.
# NOTE: Can't pass empty arrays into 3d version of plot()
lines = [_c_(555803, _a_(555799, _n_(555798, "ax", lambda: ax), "plot"), _n_(555800, "dat", lambda: dat)[0, 0:1], _n_(555801, "dat", lambda: dat)[1, 0:1], _n_(555802, "dat", lambda: dat)[2, 0:1])[0] for dat in _n_(555804, "data", lambda: data)]
_l_(555805)

# Setting the axes properties
_c_(555808, _a_(555807, _n_(555806, "ax", lambda: ax), "set_xlim3d"), [0.0, 1.0])
_l_(555809)
_c_(555812, _a_(555811, _n_(555810, "ax", lambda: ax), "set_xlabel"), 'X')
_l_(555813)

_c_(555816, _a_(555815, _n_(555814, "ax", lambda: ax), "set_ylim3d"), [0.0, 1.0])
_l_(555817)
_c_(555820, _a_(555819, _n_(555818, "ax", lambda: ax), "set_ylabel"), 'Y')
_l_(555821)

_c_(555824, _a_(555823, _n_(555822, "ax", lambda: ax), "set_zlim3d"), [0.0, 1.0])
_l_(555825)
_c_(555828, _a_(555827, _n_(555826, "ax", lambda: ax), "set_zlabel"), 'Z')
_l_(555829)

_c_(555832, _a_(555831, _n_(555830, "ax", lambda: ax), "set_title"), '3D Test')
_l_(555833)

# Creating the Animation object
line_ani = _c_(555840, _a_(555835, _n_(555834, "animation", lambda: animation), "FuncAnimation"), _n_(555836, "fig", lambda: fig), _n_(555837, "update_lines", lambda: update_lines), 25, fargs=(_n_(555838, "data", lambda: data), _n_(555839, "lines", lambda: lines)), interval=50)
_l_(555841)

_c_(555844, _a_(555843, _n_(555842, "plt", lambda: plt), "show"))
_l_(555845)