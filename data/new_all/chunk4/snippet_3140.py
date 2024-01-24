# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41372601/program-error-typeerror-not-all-arguments-converted-during-string-formatting
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
num = _c_(609058, _n_(609057, "input", lambda: input), 'Please choose a number between 2 and 9:')
_l_(609059)
prime = True 
_l_(609060) 

for test in _c_(609062, _n_(609061, "range", lambda: range), 2,10):
    _l_(609076)


    if _n_(609063, "num", lambda: num) % _n_(609064, "test", lambda: test) == 0 and _n_(609065, "num", lambda: num) != _n_(609066, "test", lambda: test):
        _l_(609075)

        _c_(609072, _n_(609067, "print", lambda: print), _n_(609068, "num", lambda: num),'equals',_n_(609069, "test", lambda: test), 'x', _n_(609070, "num", lambda: num)/_n_(609071, "test", lambda: test))
        _l_(609073)
        prime = False
        _l_(609074)

if _n_(609077, "prime", lambda: prime):
    _l_(609086)

    _c_(609080, _n_(609078, "print", lambda: print), _n_(609079, "num", lambda: num), 'is a prime number!')
    _l_(609081)
else:
    _c_(609084, _n_(609082, "print", lambda: print), _n_(609083, "num", lambda: num), 'is not a prime number!')
    _l_(609085)