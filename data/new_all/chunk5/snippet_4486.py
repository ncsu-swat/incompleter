# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56776920/having-trouble-typeerror-string-indeces-must-be-an-integer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
numberString = 0
_l_(685586)
holder = 0
_l_(685587)
partOne = 0
_l_(685588)
partTwo = 0
_l_(685589)
counter = 0
_l_(685590)
num = 0
_l_(685591)

def isPalindrome(number):
    _l_(685640)


    if _n_(685592, "number", lambda: number) % 2 == 0:
        _l_(685639)

        numberString = _c_(685595, _n_(685593, "str", lambda: str), _n_(685594, "number", lambda: number))
        _l_(685596)
        holder = _c_(685599, _n_(685597, "len", lambda: len), _n_(685598, "numberString", lambda: numberString))
        _l_(685600)
        holder = _n_(685601, "holder", lambda: holder) // 2
        _l_(685602)
        holder = _c_(685605, _n_(685603, "int", lambda: int), _n_(685604, "holder", lambda: holder))
        _l_(685606)
        partTwo = _n_(685607, "numberString", lambda: numberString)[-_n_(685608, "holder", lambda: (holder)),-1]
        _l_(685609)
        partOne = _n_(685610, "numberString", lambda: numberString)[0,(_n_(685611, "holder", lambda: holder) - 1)]
        _l_(685612)
        if _n_(685613, "partOne", lambda: partOne) == _n_(685614, "partTwo", lambda: partTwo):
            _l_(685617)

            aux = True
            _l_(685615)
            return aux
        else:
            aux = False
            _l_(685616)
            return aux

    elif _n_(685618, "number", lambda: number) % 2 != 0:
        _l_(685638)

        numberString = _c_(685621, _n_(685619, "str", lambda: str), _n_(685620, "number", lambda: number))
        _l_(685622)
        holder = _c_(685625, _n_(685623, "len", lambda: len), _n_(685624, "numberString", lambda: numberString)) // 2
        _l_(685626)
        partTwo = _n_(685627, "numberString", lambda: numberString)[-_n_(685628, "holder", lambda: (holder)),-1]
        _l_(685629)
        partOne = _n_(685630, "numberString", lambda: numberString)[0, (_n_(685631, "holder", lambda: holder) - 1)]
        _l_(685632)
        if _n_(685633, "partOne", lambda: partOne) == _n_(685634, "PartTwo", lambda: PartTwo):
            _l_(685637)

            aux = True 
            _l_(685635) 
            return aux 
        else:
            aux = False
            _l_(685636)
            return aux

for first in _c_(685642, _n_(685641, "range", lambda: range), 100,1000):
    _l_(685657)

    for second in _c_(685644, _n_(685643, "range", lambda: range), 100,1000):
        _l_(685656)

        num = _n_(685645, "first", lambda: first) * _n_(685646, "second", lambda: second)
        _l_(685647)
        if _c_(685650, _n_(685648, "isPalindrome", lambda: isPalindrome), _n_(685649, "num", lambda: num)) == True:
            _l_(685655)

            _c_(685653, _n_(685651, "print", lambda: print), _n_(685652, "num", lambda: num),'is a palindrome.')
            _l_(685654)