# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/28121499/typeerror-function-object-is-not-subscriptable-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def scorekeeper():
    _l_(453825)

    Scorekeeper = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    _l_(453822)
    aux = _n_(453823, "Scorekeeper", lambda: Scorekeeper)
    _l_(453824)
    return aux

def addscore(Scorekeeper):
    _l_(453840)

    Addscore = _c_(453829, _n_(453826, "int", lambda: int), _c_(453828, _n_(453827, "input", lambda: input), "what player scored a goal?"))
    _l_(453830)
    Addscore = _n_(453831, "Addscore", lambda: Addscore) - 1 
    _l_(453832) 
    (_n_(453833, "Scorekeeper", lambda: Scorekeeper)[_n_(453834, "Addscore", lambda: Addscore)]) = ((_n_(453835, "Scorekeeper", lambda: Scorekeeper)[_n_(453836, "Addscore", lambda: Addscore)]) + 1) 
    _l_(453837) 
    aux = _n_(453838, "Scorekeeper", lambda: Scorekeeper)
    _l_(453839)
    return aux
def histogram(Scorekeeper):
    _l_(453861)

    _c_(453842, _n_(453841, "print", lambda: print), "\nCreating a histogram from values: ")
    _l_(453843)
    _c_(453845, _n_(453844, "print", lambda: print), "%s %10s %10s" %("Element", "Ranking", "Histogram"))
    _l_(453846)
    for i in _c_(453851, _n_(453847, "range", lambda: range), _c_(453850, _n_(453848, "len", lambda: len), _n_(453849, "Scorekeeper", lambda: Scorekeeper))):
        _l_(453860)

        _c_(453858, _n_(453852, "print", lambda: print), "%7d%5d %-s" % (_n_(453853, "i", lambda: i) +1, _n_(453854, "Scorekeeper", lambda: Scorekeeper)[_n_(453855, "i", lambda: i)], "*" * _n_(453856, "Scorekeeper", lambda: Scorekeeper)[_n_(453857, "i", lambda: i)])) 
        _l_(453859) 
def main():
    _l_(453879)

    Scorekeeper = _c_(453863, _n_(453862, "scorekeeper", lambda: scorekeeper))
    _l_(453864)
    endgame = 'n'
    _l_(453865)
    while _n_(453866, "endgame", lambda: endgame) == 'n':
        _l_(453874)

        Addscore = _c_(453869, _n_(453867, "addscore", lambda: addscore), _n_(453868, "scorekeeper", lambda: scorekeeper))
        _l_(453870)
        endgame = _c_(453872, _n_(453871, "input", lambda: input), "Has the game ended? y/n")
        _l_(453873)

    _c_(453877, _n_(453875, "histogram", lambda: histogram), _n_(453876, "scorekeeper", lambda: scorekeeper))
    _l_(453878)

_c_(453881, _n_(453880, "main", lambda: main))
_l_(453882)