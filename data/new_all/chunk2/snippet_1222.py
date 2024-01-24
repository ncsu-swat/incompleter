# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75872760/problem-in-class-to-identify-the-gender-of-a-word-attributeerror-gender-obje
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
variable1 = "Pedro"
_l_(445279)

class Gender:
    _l_(445292)

    def __eq__(self, male, female):
        _l_(445291)

        x= _c_(445282, _a_(445281, _n_(445280, "male", lambda: male), "startswith"), "o")
        _l_(445283)
        y= _c_(445286, _a_(445285, _n_(445284, "female", lambda: female), "startswith"), "a")
        _l_(445287)
        aux = _n_(445288, "x", lambda: x),_n_(445289, "y", lambda: y)
        _l_(445290)
        return aux

gender = _c_(445294, _n_(445293, "Gender", lambda: Gender))
_l_(445295)


if _n_(445296, "variable1", lambda: variable1) == _a_(445298, _n_(445297, "gender", lambda: gender), "male"):
    _l_(445307)

    _c_(445301, _n_(445299, "print", lambda: print), _n_(445300, "variable1", lambda: variable1), " is male")
    _l_(445302)
else:
    _c_(445305, _n_(445303, "print", lambda: print), _n_(445304, "variable1", lambda: variable1), " is female")
    _l_(445306)