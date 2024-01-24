# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74394682/why-am-i-getting-this-error-attributeerror-type-object-bubblesort-has-no-att
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from random import randint
    _l_(526366)

except ImportError:
    pass

class bubbleSort:
    _l_(526452)

    def __init__(self, size):
        _l_(526407)

        _n_(526367, "self", lambda: self).size = _n_(526368, "size", lambda: size) # Array size
        _l_(526369) # Array size
        _n_(526370, "self", lambda: self).array = [] # Random array
        _l_(526371) # Random array
        _n_(526372, "self", lambda: self).sorted = _a_(526374, _n_(526373, "self", lambda: self), "array") # Sorted array
        _l_(526375) # Sorted array
        _n_(526376, "self", lambda: self).random = 0 # Random number
        _l_(526377) # Random number

        _n_(526378, "self", lambda: self).count = 0
        _l_(526379)
        _n_(526380, "self", lambda: self).done = False
        _l_(526381)
        _n_(526382, "self", lambda: self).equal = 0
        _l_(526383)
        while _a_(526385, _n_(526384, "self", lambda: self), "count") != _a_(526387, _n_(526386, "self", lambda: self), "size"):
            _l_(526406)

            random = _c_(526391, _n_(526388, "randint", lambda: randint), 1, _a_(526390, _n_(526389, "self", lambda: self), "size"))
            _l_(526392)
            if _n_(526393, "random", lambda: random) in _a_(526395, _n_(526394, "self", lambda: self), "array"):
                _l_(526405)

                pass
                _l_(526396)
            else:
                _c_(526401, _a_(526399, _a_(526398, _n_(526397, "self", lambda: self), "array"), "append"), _n_(526400, "random", lambda: random))
                _l_(526402)
                _n_(526403, "self", lambda: self).count += 1
                _l_(526404)

    def sort(self):
        _l_(526451)

        while _a_(526409, _n_(526408, "self", lambda: self), "done") != True:
            _l_(526450)

            _n_(526410, "self", lambda: self).equal = False
            _l_(526411)
            for i in _c_(526415, _n_(526412, "range", lambda: range), _a_(526414, _n_(526413, "self", lambda: self), "size")):
                _l_(526449)

                if _n_(526416, "i", lambda: i) == _a_(526418, _n_(526417, "self", lambda: self), "size"):
                    _l_(526448)

                    pass
                    _l_(526419)
                else:
                    if _a_(526421, _n_(526420, "self", lambda: self), "sorted")[_n_(526422, "i", lambda: i)] > [_a_(526424, _n_(526423, "self", lambda: self), "tmp")]:
                        _l_(526447)

                        _n_(526425, "self", lambda: self).equal += 1
                        _l_(526426)
                        if _a_(526428, _n_(526427, "self", lambda: self), "equal") == _a_(526430, _n_(526429, "self", lambda: self), "size"):
                            _l_(526433)

                            _n_(526431, "self", lambda: self).done = True
                            _l_(526432)
                    else:
                        _a_(526435, _n_(526434, "self", lambda: self), "sorted")[_n_(526436, "i", lambda: i)], _a_(526438, _n_(526437, "self", lambda: self), "sorted")[_n_(526439, "i", lambda: i) + 1] = _a_(526441, _n_(526440, "self", lambda: self), "sorted")[_n_(526442, "i", lambda: i)+1], _a_(526444, _n_(526443, "self", lambda: self), "sorted")[_n_(526445, "i", lambda: i)]
                        _l_(526446)


new = _c_(526454, _n_(526453, "bubbleSort", lambda: bubbleSort), 10)
_l_(526455)
_c_(526459, _n_(526456, "print", lambda: print), _a_(526458, _n_(526457, "bubbleSort", lambda: bubbleSort), "array"))
_l_(526460)