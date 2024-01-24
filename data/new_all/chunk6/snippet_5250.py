# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43697088/typeerror-removeduplicates-missing-1-required-positional-argument-randlist
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from random import randrange
    _l_(363800)

except ImportError:
    pass

def createList():
    _l_(363814)

    _c_(363802, _n_(363801, "print", lambda: print), "A program that will generate a list of 50 random numbers then remove any duplicates.")
    _l_(363803)
    for i in _c_(363805, _n_(363804, "range", lambda: range), 50):
        _l_(363813)

        randList = _c_(363807, _n_(363806, "randrange", lambda: randrange), 101)
        _l_(363808)
        _c_(363811, _n_(363809, "print", lambda: print), _n_(363810, "randList", lambda: randList))
        _l_(363812)

def removeDuplicates(randList):
    _l_(363830)

    uniqueList = []
    _l_(363815)
    for i in _n_(363816, "randList", lambda: randList):
        _l_(363825)

        if _n_(363817, "i", lambda: i) not in _n_(363818, "uniqueList", lambda: uniqueList):
            _l_(363824)

            _c_(363822, _a_(363820, _n_(363819, "uniqueList", lambda: uniqueList), "append"), _n_(363821, "i", lambda: i))
            _l_(363823)
    _c_(363828, _n_(363826, "print", lambda: print), _n_(363827, "uniqueList", lambda: uniqueList))
    _l_(363829)

def main():
    _l_(363837)

    _c_(363832, _n_(363831, "createList", lambda: createList))
    _l_(363833)
    _c_(363835, _n_(363834, "removeDuplicates", lambda: removeDuplicates))
    _l_(363836)

if _n_(363838, "__name__", lambda: __name__) == "__main__":
    _l_(363841)

_c_(363840, _n_(363839, "main", lambda: main)