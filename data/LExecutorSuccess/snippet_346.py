# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/805066/how-do-i-call-a-parent-classs-method-from-a-child-class-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Dog(_n_(1539931, "object", lambda: object)):
    _l_(1539959)

    name = ''
    _l_(1539932)
    moves = []
    _l_(1539933)

    def __init__(self, name):
        _l_(1539937)

        _n_(1539934, "self", lambda: self).name = _n_(1539935, "name", lambda: name)
        _l_(1539936)

    def moves_setup(self,x):
        _l_(1539954)

        _c_(1539941, _a_(1539940, _a_(1539939, _n_(1539938, "self", lambda: self), "moves"), "append"), 'walk')
        _l_(1539942)
        _c_(1539946, _a_(1539945, _a_(1539944, _n_(1539943, "self", lambda: self), "moves"), "append"), 'run')
        _l_(1539947)
        _c_(1539952, _a_(1539950, _a_(1539949, _n_(1539948, "self", lambda: self), "moves"), "append"), _n_(1539951, "x", lambda: x))
        _l_(1539953)
    def get_moves(self):
        _l_(1539958)

        aux = _a_(1539956, _n_(1539955, "self", lambda: self), "moves")
        _l_(1539957)
        return aux

class Superdog(_n_(1539960, "Dog", lambda: Dog)):
    _l_(1539971)


    #Let's try to append new fly ability to our Superdog
    def moves_setup(self):
        _l_(1539970)

        #Set default moves by calling method of parent class
        _c_(1539963, _a_(1539962, _n_(1539961, "super", lambda: super)(), "moves_setup"), "hello world")
        _l_(1539964)
        _c_(1539968, _a_(1539967, _a_(1539966, _n_(1539965, "self", lambda: self), "moves"), "append"), 'fly')
        _l_(1539969)
dog = _c_(1539973, _n_(1539972, "Superdog", lambda: Superdog), 'Freddy')
_l_(1539974)
_c_(1539978, _n_(1539975, "print", lambda: print), _a_(1539977, _n_(1539976, "dog", lambda: dog), "name"))
_l_(1539979)
_c_(1539982, _a_(1539981, _n_(1539980, "dog", lambda: dog), "moves_setup"))
_l_(1539983)
_c_(1539988, _n_(1539984, "print", lambda: print), _c_(1539987, _a_(1539986, _n_(1539985, "dog", lambda: dog), "get_moves"))) 
_l_(1539989) 

