# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/26985054/python-3-type-error-object-new-takes-no-parameters
#create the car class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Car:
    _l_(680252)


    #create the initiator function
    def __init__carStats(self, year, model):
        _l_(680221)

        _n_(680213, "self", lambda: self).__speed = 0
        _l_(680214)
        _n_(680215, "self", lambda: self).__year = _n_(680216, "year", lambda: year)
        _l_(680217)
        _n_(680218, "self", lambda: self).__model = _n_(680219, "model", lambda: model)
        _l_(680220)

    def setModel(self, model):
        _l_(680225)

        _n_(680222, "self", lambda: self).__model = _n_(680223, "model", lambda: model)
        _l_(680224)

    def setYear(self, year):
        _l_(680229)

        _n_(680226, "self", lambda: self).__year = _n_(680227, "year", lambda: year)
        _l_(680228)

    #create speed increase function
    def speedUp(self):
        _l_(680235)

        _c_(680231, _n_(680230, "print", lambda: print), 'Calling speed up function.')
        _l_(680232)
        _n_(680233, "self", lambda: self).__speed += 5
        _l_(680234)

    #create slowdown function
    def slowDown(self):
        _l_(680241)

        _c_(680237, _n_(680236, "print", lambda: print), 'Calling slow down function.')
        _l_(680238)
        _n_(680239, "self", lambda: self).__speed -= 5
        _l_(680240)

    #create show speed function
    def showSpeed(self):
        _l_(680251)

        _c_(680249, _n_(680242, "print", lambda: print), 'The', _a_(680244, _n_(680243, "self", lambda: self), "__year"), _a_(680246, _n_(680245, "self", lambda: self), "__model"), '\'s current speed is', _a_(680248, _n_(680247, "self", lambda: self), "__speed"),'miles per houer')
        _l_(680250)

#create main function
def Main():
    _l_(680266)

    year = ''
    _l_(680253)
    make = ''
    _l_(680254)
    #get car year and make
    make = _c_(680256, _n_(680255, "input", lambda: input), 'What model is the car? \n')
    _l_(680257)
    year = _c_(680259, _n_(680258, "input", lambda: input), 'What year is the car?" \n')
    _l_(680260)

    myCar = _c_(680264, _n_(680261, "Car", lambda: Car), _n_(680262, "year", lambda: year), _n_(680263, "make", lambda: make))
    _l_(680265)

_c_(680268, _n_(680267, "Main", lambda: Main))
_l_(680269)