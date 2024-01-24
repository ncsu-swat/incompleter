# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/36120585/attributeerror-int-object-has-no-attribute-fd
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import turtle
    _l_(642418)

except ImportError:
    pass

t = _c_(642421, _a_(642420, _n_(642419, "turtle", lambda: turtle), "Turtle"))
_l_(642422)
_c_(642425, _a_(642424, _n_(642423, "turtle", lambda: turtle), "mainloop"))
_l_(642426)

def draw(t, length, n):
    _l_(642470)

    if _n_(642427, "n", lambda: n) == 0:
        _l_(642429)

        aux = ""
        _l_(642428)
        return aux
    angle = 50
    _l_(642430)
    _c_(642435, _a_(642432, _n_(642431, "t", lambda: t), "fd"), _n_(642433, "length", lambda: length)*_n_(642434, "n", lambda: n))
    _l_(642436)
    _c_(642440, _a_(642438, _n_(642437, "t", lambda: t), "lt"), _n_(642439, "angle", lambda: angle))
    _l_(642441)
    _c_(642446, _n_(642442, "draw", lambda: draw), _n_(642443, "t", lambda: t), _n_(642444, "length", lambda: length), _n_(642445, "n", lambda: n)-1)
    _l_(642447)
    _c_(642451, _a_(642449, _n_(642448, "t", lambda: t), "rt"), 2*_n_(642450, "angle", lambda: angle))
    _l_(642452)
    _c_(642457, _n_(642453, "draw", lambda: draw), _n_(642454, "t", lambda: t), _n_(642455, "length", lambda: length), _n_(642456, "n", lambda: n)-1)
    _l_(642458)
    _c_(642462, _a_(642460, _n_(642459, "t", lambda: t), "lt"), _n_(642461, "angle", lambda: angle))
    _l_(642463)
    _c_(642468, _a_(642465, _n_(642464, "t", lambda: t), "bk"), _n_(642466, "length", lambda: length)*_n_(642467, "n", lambda: n))
    _l_(642469)

_c_(642472, _n_(642471, "draw", lambda: draw), 5, 10, 15)
_l_(642473)