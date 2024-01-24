# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57118363/why-is-this-for-loop-throwing-a-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Image:
    _l_(565341)


    def drawCircle(self, centerX, centerY, radius):
        _l_(565340)

        sin45 = 0.70710678118                                               
        _l_(565278)                                               
        distance = _n_(565279, "radius", lambda: radius)/(2*_n_(565280, "sin45", lambda: sin45))
        _l_(565281)
        for i in _c_(565285, _n_(565282, "range", lambda: range), _n_(565283, "radius", lambda: radius),_n_(565284, "distance", lambda: distance),-1.0):
            _l_(565339)

            j = _c_(565292, _a_(565287, _n_(565286, "math", lambda: math), "sqrt"), _n_(565288, "r", lambda: r)*_n_(565289, "r", lambda: r) - _n_(565290, "i", lambda: i)*_n_(565291, "i", lambda: i))
            _l_(565293)
            for k in _c_(565297, _n_(565294, "range", lambda: range), -_n_(565295, "j", lambda: j), _n_(565296, "j", lambda: j), 1):
                _l_(565338)

                _c_(565306, _a_(565299, _n_(565298, "self", lambda: self), "writePixel"), _a_(565301, _n_(565300, "self", lambda: self), "centerX") - _n_(565302, "k", lambda: k), _a_(565304, _n_(565303, "self", lambda: self), "enterY") + _n_(565305, "i", lambda: i))
                _l_(565307)
                _c_(565316, _a_(565309, _n_(565308, "self", lambda: self), "writePixel"), _a_(565311, _n_(565310, "self", lambda: self), "centerX") - _n_(565312, "k", lambda: k), _a_(565314, _n_(565313, "self", lambda: self), "enterY") - _n_(565315, "i", lambda: i))
                _l_(565317)
                _c_(565326, _a_(565319, _n_(565318, "self", lambda: self), "writePixel"), _a_(565321, _n_(565320, "self", lambda: self), "centerX") + _n_(565322, "i", lambda: i), _a_(565324, _n_(565323, "self", lambda: self), "enterY") + _n_(565325, "i", lambda: i))
                _l_(565327)
                _c_(565336, _a_(565329, _n_(565328, "self", lambda: self), "writePixel"), _a_(565331, _n_(565330, "self", lambda: self), "centerX") - _n_(565332, "i", lambda: i), _a_(565334, _n_(565333, "self", lambda: self), "enterY") - _n_(565335, "i", lambda: i))
                _l_(565337)

'''Testing the code'''
_l_(565342)
obj = _c_(565344, _n_(565343, "Image", lambda: Image))
_l_(565345)
_c_(565348, _a_(565347, _n_(565346, "obj", lambda: obj), "drawCircle"), 35.0, 35.0, 35.0)
_l_(565349)