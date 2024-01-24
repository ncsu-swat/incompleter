# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/39481039/typeerror-unsupported-operand-types-for-float-and-nonetype-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import turtle as t
    _l_(602276)

except ImportError:
    pass
try:
    import math as m
    _l_(602278)

except ImportError:
    pass
try:
    import random as r
    _l_(602280)

except ImportError:
    pass

raindrops = _c_(602284, _n_(602281, "int", lambda: int), _c_(602283, _n_(602282, "input", lambda: input), "Enter the number of raindrops: "))
_l_(602285)

def drawSquare():
    _l_(602330)

    _c_(602288, _a_(602287, _n_(602286, "t", lambda: t), "up"))
    _l_(602289)
    _c_(602292, _a_(602291, _n_(602290, "t", lambda: t), "goto"), -300,-300)
    _l_(602293)
    _c_(602296, _a_(602295, _n_(602294, "t", lambda: t), "down"))
    _l_(602297)
    _c_(602300, _a_(602299, _n_(602298, "t", lambda: t), "fd"), 600)
    _l_(602301)
    _c_(602304, _a_(602303, _n_(602302, "t", lambda: t), "lt"), 90)
    _l_(602305)
    _c_(602308, _a_(602307, _n_(602306, "t", lambda: t), "fd"), 600)
    _l_(602309)
    _c_(602312, _a_(602311, _n_(602310, "t", lambda: t), "lt"), 90)
    _l_(602313)
    _c_(602316, _a_(602315, _n_(602314, "t", lambda: t), "fd"), 600)
    _l_(602317)
    _c_(602320, _a_(602319, _n_(602318, "t", lambda: t), "lt"), 90)
    _l_(602321)
    _c_(602324, _a_(602323, _n_(602322, "t", lambda: t), "fd"), 600)
    _l_(602325)
    _c_(602328, _a_(602327, _n_(602326, "t", lambda: t), "lt"), 90)
    _l_(602329)

def location():
    _l_(602352)

    x = _c_(602333, _a_(602332, _n_(602331, "r", lambda: r), "randint"), -300, 300)
    _l_(602334)
    y = _c_(602337, _a_(602336, _n_(602335, "r", lambda: r), "randint"), -300, 300)
    _l_(602338)
    _c_(602341, _a_(602340, _n_(602339, "t", lambda: t), "up"))
    _l_(602342)
    _c_(602347, _a_(602344, _n_(602343, "t", lambda: t), "goto"), _n_(602345, "x", lambda: x), _n_(602346, "y", lambda: y))
    _l_(602348)
    aux = _n_(602349, "x", lambda: x), _n_(602350, "y", lambda: y)
    _l_(602351)
    return aux

def drawRaindrops(x, y):
    _l_(602493)

    _c_(602364, _a_(602354, _n_(602353, "t", lambda: t), "fillcolor"), _c_(602357, _a_(602356, _n_(602355, "r", lambda: r), "random")), _c_(602360, _a_(602359, _n_(602358, "r", lambda: r), "random")), _c_(602363, _a_(602362, _n_(602361, "r", lambda: r), "random")))
    _l_(602365)
    circles = _c_(602368, _a_(602367, _n_(602366, "r", lambda: r), "randint"), 3, 8)
    _l_(602369)
    radius = _c_(602372, _a_(602371, _n_(602370, "r", lambda: r), "randint"), 1, 20)
    _l_(602373)
    newradius = _n_(602374, "radius", lambda: radius)
    _l_(602375)
    area = 0
    _l_(602376)
    _c_(602379, _a_(602378, _n_(602377, "t", lambda: t), "up"))
    _l_(602380)
    _c_(602383, _a_(602382, _n_(602381, "t", lambda: t), "rt"), 90)
    _l_(602384)
    _c_(602388, _a_(602386, _n_(602385, "t", lambda: t), "fd"), _n_(602387, "newradius", lambda: newradius))
    _l_(602389)
    _c_(602392, _a_(602391, _n_(602390, "t", lambda: t), "lt"), 90)
    _l_(602393)
    _c_(602396, _a_(602395, _n_(602394, "t", lambda: t), "down"))
    _l_(602397)
    _c_(602400, _a_(602399, _n_(602398, "t", lambda: t), "begin_fill"))
    _l_(602401)
    _c_(602405, _a_(602403, _n_(602402, "t", lambda: t), "circle"), _n_(602404, "newradius", lambda: newradius))
    _l_(602406)
    _c_(602409, _a_(602408, _n_(602407, "t", lambda: t), "end_fill"))
    _l_(602410)
    _c_(602413, _a_(602412, _n_(602411, "t", lambda: t), "up"))
    _l_(602414)
    _c_(602417, _a_(602416, _n_(602415, "t", lambda: t), "lt"), 90)
    _l_(602418)
    _c_(602422, _a_(602420, _n_(602419, "t", lambda: t), "fd"), _n_(602421, "newradius", lambda: newradius))
    _l_(602423)
    _c_(602426, _a_(602425, _n_(602424, "t", lambda: t), "rt"), 90)
    _l_(602427)
    while _n_(602428, "circles", lambda: circles) > 0:
        _l_(602490)

        if _n_(602429, "x", lambda: x) + _n_(602430, "newradius", lambda: newradius) < 300 and _n_(602431, "x", lambda: x) - _n_(602432, "newradius", lambda: newradius) > -300 and _n_(602433, "y", lambda: y) + _n_(602434, "newradius", lambda: newradius) < 300 and _n_(602435, "y", lambda: y) - _n_(602436, "newradius", lambda: newradius) > -300:
            _l_(602489)

            _c_(602439, _a_(602438, _n_(602437, "t", lambda: t), "up"))
            _l_(602440)
            _c_(602443, _a_(602442, _n_(602441, "t", lambda: t), "rt"), 90)
            _l_(602444)
            _c_(602448, _a_(602446, _n_(602445, "t", lambda: t), "fd"), _n_(602447, "newradius", lambda: newradius))
            _l_(602449)
            _c_(602452, _a_(602451, _n_(602450, "t", lambda: t), "lt"), 90)
            _l_(602453)
            _c_(602456, _a_(602455, _n_(602454, "t", lambda: t), "down"))
            _l_(602457)
            _c_(602461, _a_(602459, _n_(602458, "t", lambda: t), "circle"), _n_(602460, "newradius", lambda: newradius))
            _l_(602462)
            _c_(602465, _a_(602464, _n_(602463, "t", lambda: t), "up"))
            _l_(602466)
            _c_(602469, _a_(602468, _n_(602467, "t", lambda: t), "lt"), 90)
            _l_(602470)
            _c_(602474, _a_(602472, _n_(602471, "t", lambda: t), "fd"), _n_(602473, "newradius", lambda: newradius))
            _l_(602475)
            _c_(602478, _a_(602477, _n_(602476, "t", lambda: t), "rt"), 90)
            _l_(602479)
            newradius += _n_(602480, "radius", lambda: radius)
            _l_(602481)
            circles -= 1
            _l_(602482)
            area += _a_(602484, _n_(602483, "m", lambda: m), "pi") * _n_(602485, "radius", lambda: radius) * _n_(602486, "radius", lambda: radius)
            _l_(602487)
        else:
            circles -= 1
            _l_(602488)
    aux = _n_(602491, "area", lambda: area)
    _l_(602492)
    return aux

def promptRaindrops(raindrops):
    _l_(602519)

    if _n_(602494, "raindrops", lambda: raindrops) < 1 or _n_(602495, "raindrops", lambda: raindrops) > 100:
        _l_(602499)

        _c_(602497, _n_(602496, "print", lambda: print), "Raindrops must be between 1 and 100 inclusive.")
        _l_(602498)
    if _n_(602500, "raindrops", lambda: raindrops) >= 1 and _n_(602501, "raindrops", lambda: raindrops) <= 100:
        _l_(602518)

        x, y = _c_(602503, _n_(602502, "location", lambda: location))
        _l_(602504)
        area = _c_(602508, _n_(602505, "drawRaindrops", lambda: drawRaindrops), _n_(602506, "x", lambda: x), _n_(602507, "y", lambda: y))
        _l_(602509)
        area += _c_(602512, _n_(602510, "promptRaindrops", lambda: promptRaindrops), _n_(602511, "raindrops", lambda: raindrops) - 1)
        _l_(602513)
        aux = _n_(602514, "x", lambda: x), _n_(602515, "y", lambda: y), _n_(602516, "area", lambda: area)
        _l_(602517)
        return aux

def main():
    _l_(602535)

    _c_(602522, _a_(602521, _n_(602520, "t", lambda: t), "speed"), 0)
    _l_(602523)
    _c_(602525, _n_(602524, "drawSquare", lambda: drawSquare))
    _l_(602526)
    x, y, area = _c_(602529, _n_(602527, "promptRaindrops", lambda: promptRaindrops), _n_(602528, "raindrops", lambda: raindrops))
    _l_(602530)
    _c_(602533, _n_(602531, "print", lambda: print), 'The area is:', _n_(602532, "area", lambda: area), 'square units.')
    _l_(602534)

_c_(602537, _n_(602536, "main", lambda: main))
_l_(602538)
_c_(602541, _a_(602540, _n_(602539, "t", lambda: t), "done"))
_l_(602542)