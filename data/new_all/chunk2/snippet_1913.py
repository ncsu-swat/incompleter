# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/35251749/nameerror-name-age-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def main():
    _l_(434720)

    age = 0;
    _l_(434705)
    weight = 0;
    _l_(434706)
    birthMonth = " ";
    _l_(434707)
    _c_(434709, _n_(434708, "getAge", lambda: getAge));
    _l_(434710)
    _c_(434712, _n_(434711, "getWeight", lambda: getWeight));
    _l_(434713)
    _c_(434715, _n_(434714, "getBirth", lambda: getBirth));
    _l_(434716)
    _c_(434718, _n_(434717, "correct", lambda: correct));
    _l_(434719)

def getAge():
    _l_(434726)

    age = _c_(434722, _n_(434721, "input", lambda: input), "Guess the age.\t")
    _l_(434723)
    aux = _n_(434724, "age", lambda: age)
    _l_(434725)
    return aux
def getWeight():
    _l_(434732)

    weight = _c_(434728, _n_(434727, "input", lambda: input), "Guess the weight.\t")
    _l_(434729)
    aux = _n_(434730, "weight", lambda: weight)
    _l_(434731)
    return aux
def getBirth():
    _l_(434738)

    birthMonth = _c_(434734, _n_(434733, "input", lambda: input), "Guess the month.\t")
    _l_(434735)
    aux = _n_(434736, "birthMonth", lambda: birthMonth)
    _l_(434737)
    return aux
def correct():
    _l_(434763)

    if (_n_(434739, "age", lambda: age) <= 25):
        _l_(434746)

        _c_(434741, _n_(434740, "print", lambda: print), "Congratulations, the age is 25 or less")
        _l_(434742)
    else:
        _c_(434744, _n_(434743, "print", lambda: print), "You did not correctly guess the age");
        _l_(434745)
    if (_n_(434747, "weight", lambda: weight) <= 128):
        _l_(434754)

        _c_(434749, _n_(434748, "print", lambda: print), "Congratulations, the weight is 128 or more")
        _l_(434750)
    else:
        _c_(434752, _n_(434751, "print", lambda: print), "You did not correctly guess the weight");
        _l_(434753)
    if (_n_(434755, "birthMonth", lambda: birthMonth) == 25):
        _l_(434762)

        _c_(434757, _n_(434756, "print", lambda: print), "Congratulations, the month is April")
        _l_(434758)
    else:
        _c_(434760, _n_(434759, "print", lambda: print), "You did not correctly guess the month");
        _l_(434761)
_c_(434765, _n_(434764, "main", lambda: main));
_l_(434766)