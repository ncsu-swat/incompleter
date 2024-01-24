# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64991199/attributeerror-on-python-with-an-encapsulation-object-hasn%c2%b4t-got-an-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Car():
    _l_(643169)


    def __init__(self):
        _l_(643149)


        _n_(643141, "self", lambda: self).__doors=4
        _l_(643142)
        _n_(643143, "self", lambda: self).sizeChasis=250
        _l_(643144)
        _n_(643145, "self", lambda: self).colorChasis=120
        _l_(643146)
        _n_(643147, "self", lambda: self).running=False
        _l_(643148)

    def start(self,letsgo):
        _l_(643158)

        _n_(643150, "self", lambda: self).running=_n_(643151, "letsgo", lambda: letsgo)
        _l_(643152)

        if_a_(643154, _n_(643153, "self", lambda: self), "running"):
            _l_(643157)

            aux = "Car is on"
            _l_(643155)
            return aux
        else:
            aux = "Car is off"
            _l_(643156)
            return aux

    def state(self):
        _l_(643168)

        _c_(643166, _n_(643159, "print", lambda: print), "The car has ", _a_(643161, _n_(643160, "self", lambda: self), "__doors"), "doors. And ", _a_(643163, _n_(643162, "self", lambda: self), "sizeChasis"), "and ", _a_(643165, _n_(643164, "self", lambda: self), "colorChasis"))
        _l_(643167)

myCar=_c_(643171, _n_(643170, "Car", lambda: Car))
_l_(643172)

_c_(643176, _n_(643173, "print", lambda: print), "A: ",_a_(643175, _n_(643174, "myCar", lambda: myCar), "sizeChasis"))
_l_(643177)
_c_(643181, _n_(643178, "print", lambda: print), "B: ", _a_(643180, _n_(643179, "myCar", lambda: myCar), "__doors"), "doors")
_l_(643182)

_c_(643187, _n_(643183, "print", lambda: print), _c_(643186, _a_(643185, _n_(643184, "myCar", lambda: myCar), "start"), True))
_l_(643188)
_c_(643191, _a_(643190, _n_(643189, "myCar", lambda: myCar), "state"))
_l_(643192)