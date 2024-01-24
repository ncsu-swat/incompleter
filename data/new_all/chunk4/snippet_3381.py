# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72136240/how-to-fix-colorred-nameerror-name-color-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import turtle
    _l_(610128)

except ImportError:
    pass
_c_(610130, _n_(610129, "color", lambda: color), 'red')
_l_(610131)
_c_(610133, _n_(610132, "bgcolor", lambda: bgcolor), 'black')
_l_(610134)
_c_(610136, _n_(610135, "speed", lambda: speed), 20)
_l_(610137)
b = 200
_l_(610138)
while _n_(610139, "b", lambda: b) > 0:
    _l_(610149)

    _c_(610142, _n_(610140, "left", lambda: left), _n_(610141, "b", lambda: b))
    _l_(610143)
    _c_(610146, _n_(610144, "forward", lambda: forward), _n_(610145, "b", lambda: b)+3)
    _l_(610147)
    b -= 1
    _l_(610148)