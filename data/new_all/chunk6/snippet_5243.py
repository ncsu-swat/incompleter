# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43697088/typeerror-removeduplicates-missing-1-required-positional-argument-randlist
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from random import randrange
    _l_(346192)

except ImportError:
    pass

def createList():
    _l_(346206)

    _c_(346194, _n_(346193, "print", lambda: print), "A program that will generate a list of 50 random numbers then remove any duplicates.")
    _l_(346195)
    for i in _c_(346197, _n_(346196, "range", lambda: range), 50):
        _l_(346205)

        randList = _c_(346199, _n_(346198, "randrange", lambda: randrange), 101)
        _l_(346200)
        _c_(346203, _n_(346201, "print", lambda: print), _n_(346202, "randList", lambda: randList))
        _l_(346204)

def removeDuplicates(randList):
    _l_(346222)

    uniqueList = []
    _l_(346207)
    for i in _n_(346208, "randList", lambda: randList):
        _l_(346217)

        if _n_(346209, "i", lambda: i) not in _n_(346210, "uniqueList", lambda: uniqueList):
            _l_(346216)

            _c_(346214, _a_(346212, _n_(346211, "uniqueList", lambda: uniqueList), "append"), _n_(346213, "i", lambda: i))
            _l_(346215)
    _c_(346220, _n_(346218, "print", lambda: print), _n_(346219, "uniqueList", lambda: uniqueList))
    _l_(346221)

def main():
    _l_(346229)

    _c_(346224, _n_(346223, "createList", lambda: createList))
    _l_(346225)
    _c_(346227, _n_(346226, "removeDuplicates", lambda: removeDuplicates))
    _l_(346228)

if _n_(346230, "__name__", lambda: __name__) == "__main__":
    _l_(346233)

_c_(346232, _n_(346231, "main", lambda: main)