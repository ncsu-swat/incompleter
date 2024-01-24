# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42992240/name-error-in-python-3-6
#!/usr/bin/env python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys; 
    _l_(463049)

except ImportError:
    pass
try:
    import random
    _l_(463051)

except ImportError:
    pass

##Creates values to use to make random equation.

x = _c_(463054, _a_(463053, _n_(463052, "random", lambda: random), "randint"), 1,11)
_l_(463055)
y = _c_(463058, _a_(463057, _n_(463056, "random", lambda: random), "randint"), 1,11)
_l_(463059)
if _n_(463060, "x", lambda: x) > _n_(463061, "y", lambda: y):
    _l_(463072)

    total = _c_(463065, _a_(463063, _n_(463062, "random", lambda: random), "randint"), _n_(463064, "x", lambda: x), 20)
    _l_(463066)
else:
    total = _c_(463070, _a_(463068, _n_(463067, "random", lambda: random), "randint"), _n_(463069, "y", lambda: y), 20)
    _l_(463071)

##Creates actual values for A,B,C, and D in equation A+B=C+D

a = _n_(463073, "x", lambda: x)
_l_(463074)
b = _n_(463075, "total", lambda: total) - _n_(463076, "a", lambda: a)
_l_(463077)
c = _n_(463078, "y", lambda: y)
_l_(463079)
d = _n_(463080, "total", lambda: total) - _n_(463081, "y", lambda: y)
_l_(463082)

##Prints option choices and asks for user input

def start_game_message():
    _l_(463104)

    _c_(463084, _n_(463083, "print", lambda: print), "Please fill in the blanks to make the following equation true:")
    _l_(463085)
    _c_(463087, _n_(463086, "print", lambda: print), "__+__=__+__")
    _l_(463088)
    _c_(463102, _n_(463089, "print", lambda: print), "The option choices are:" + _c_(463092, _n_(463090, "str", lambda: str), _n_(463091, "a", lambda: a)) + ", " + _c_(463095, _n_(463093, "str", lambda: str), _n_(463094, "b", lambda: b)) + ", "  + _c_(463098, _n_(463096, "str", lambda: str), _n_(463097, "c", lambda: c)) + ", " + _c_(463101, _n_(463099, "str", lambda: str), _n_(463100, "d", lambda: d)))
    _l_(463103)
def ask_for_input():
    _l_(463117)

    blank1 = _c_(463106, _n_(463105, "input", lambda: input), "What is the value of the first blank?")
    _l_(463107)
    blank2 = _c_(463109, _n_(463108, "input", lambda: input), "What is the value of the second blank?")
    _l_(463110)
    blank3 = _c_(463112, _n_(463111, "input", lambda: input), "What is the value of the third blank?")
    _l_(463113)
    blank4 = _c_(463115, _n_(463114, "input", lambda: input), "What is the value of the fourth blank?")
    _l_(463116)
_c_(463119, _n_(463118, "start_game_message", lambda: start_game_message))
_l_(463120)
##Check if user input is correct
def check_answer():
    _l_(463150)

    _c_(463122, _n_(463121, "ask_for_input", lambda: ask_for_input))
    _l_(463123)
    _c_(463126, _n_(463124, "print", lambda: print), _n_(463125, "blank1", lambda: blank1))
    _l_(463127)
    if _c_(463130, _n_(463128, "int", lambda: int), _n_(463129, "blank1", lambda: blank1))+ _c_(463133, _n_(463131, "int", lambda: int), _n_(463132, "blank2", lambda: blank2)) == _c_(463136, _n_(463134, "int", lambda: int), _n_(463135, "blank3", lambda: blank3)) + _c_(463139, _n_(463137, "int", lambda: int), _n_(463138, "blank4", lambda: blank4)):
        _l_(463149)

        _c_(463141, _n_(463140, "print", lambda: print), "That is correct!")
        _l_(463142)
    else:
        _c_(463144, _n_(463143, "print", lambda: print), "That is incorrect. Please try again.")
        _l_(463145)
        _c_(463147, _n_(463146, "ask_for_input", lambda: ask_for_input))
        _l_(463148)
_c_(463152, _n_(463151, "check_answer", lambda: check_answer))
_l_(463153)