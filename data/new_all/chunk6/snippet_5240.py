# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47618186/python-class-init-override-typeerror-init-takes-5-positional-argumen
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Dog(_n_(362320, "Animal", lambda: Animal)):
    _l_(362336)

    __owner = ""
    _l_(362321)

    def __init(self, name, height, weight, sound, owner):
        _l_(362335)

        _n_(362322, "self", lambda: self).__owner = _n_(362323, "owner", lambda: owner)
        _l_(362324)
        _c_(362333, _a_(362328, _n_(362325, "super", lambda: super)(_n_(362326, "Dog", lambda: Dog), _n_(362327, "self", lambda: self)), "__init__"), _n_(362329, "name", lambda: name), _n_(362330, "height", lambda: height), _n_(362331, "weight", lambda: weight), _n_(362332, "sound", lambda: sound))
        _l_(362334)

dog = _c_(362338, _n_(362337, "Dog", lambda: Dog), 'Max', 120, 50, 'Woff', 'Tom') #<==== HERE ERROR OCCURES
_l_(362339) #<==== HERE ERROR OCCURES