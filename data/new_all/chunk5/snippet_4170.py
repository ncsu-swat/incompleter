# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62095650/python-3-x-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(650170)

except ImportError:
    pass




def coinFlip(p):
    _l_(650179)

    #perform the binomial distribution (returns 1 or 0)
    result = _c_(650175, _a_(650173, _a_(650172, _n_(650171, "np", lambda: np), "random"), "binomial"), 1 , _n_(650174, "p", lambda: p))
    _l_(650176)
    aux = _n_(650177, "result", lambda: result)
    _l_(650178)
    #return flip to be added to numpy array
    return aux



'''Main Area'''
_l_(650180)
#probability of heads vs. tails. this can be changed
p = .5
_l_(650181)
#num of flips required. this can be changed
n = 10
_l_(650182)

#initiate array
FullResults = _c_(650186, _a_(650184, _n_(650183, "np", lambda: np), "arrange"), _n_(650185, "n", lambda: n))
_l_(650187)

#perform the desired number of flips required probability set above
for i in _c_(650190, _n_(650188, "range", lambda: range), 0, _n_(650189, "n", lambda: n)):
    _l_(650198)

    _n_(650191, "fullResults", lambda: fullResults)[_n_(650192, "i", lambda: i)] = _c_(650195, _n_(650193, "coinFlip", lambda: coinFlip), _n_(650194, "p", lambda: p))
    _l_(650196)
    i+=1
    _l_(650197)

#print results
_c_(650201, _n_(650199, "print", lambda: print), "probability is set to ", _n_(650200, "p", lambda: p))
_l_(650202)
_c_(650205, _n_(650203, "print", lambda: print), "Tails = 0, Heads = 1: ", _n_(650204, "fullResults", lambda: fullResults))
_l_(650206)
#Total up heads and tails for easy user experience
_c_(650212, _n_(650207, "print", lambda: print), "head count: ", _c_(650211, _a_(650209, _n_(650208, "np", lambda: np), "count_nonzero"), _n_(650210, "fullResults", lambda: fullResults) == 1))
_l_(650213)
_c_(650219, _n_(650214, "print", lambda: print), "Tail count: ", _c_(650218, _a_(650216, _n_(650215, "np", lambda: np), "count_nonzero"), _n_(650217, "fullResults", lambda: fullResults) == 0))
_l_(650220)