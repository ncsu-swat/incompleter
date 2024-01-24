# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/36190476/attributeerror-nonetype-object-has-no-attribute-title
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(340995)

except ImportError:
    pass
try:
    import sys
    _l_(340997)

except ImportError:
    pass

_c_(340999, _n_(340998, "print", lambda: print), "Welcome to my quiz")
_l_(341000)
_c_(341003, _a_(341002, _n_(341001, "time", lambda: time), "sleep"), 2)
_l_(341004)
_c_(341006, _n_(341005, "input", lambda: input), 'Press enter to continue')
_l_(341007)

score = _c_(341009, _n_(341008, "int", lambda: int), 0)
_l_(341010)
failed = _c_(341012, _n_(341011, "int", lambda: int), 0)
_l_(341013)

def points():
    _l_(341020)

    _c_(341015, _n_(341014, "print", lambda: print), "Correct! Well done!")
    _l_(341016)
    global score
    _l_(341017)
    score = _n_(341018, "score", lambda: score) + 1
    _l_(341019)

def fail():
    _l_(341027)

    _c_(341022, _n_(341021, "print", lambda: print), "Oh no, that is incorrect")
    _l_(341023)
    global failed
    _l_(341024)
    failed = _n_(341025, "failed", lambda: failed) + 1
    _l_(341026)

def printtotal():
    _l_(341035)

    global score
    _l_(341028)
    global failed
    _l_(341029)
    _c_(341033, _n_(341030, "print", lambda: print), "You have ",_n_(341031, "score", lambda: score),"points, and ",_n_(341032, "failed", lambda: failed),"/3 lives used.")
    _l_(341034)

if _n_(341036, "failed", lambda: failed) == 5:
    _l_(341041)

    _c_(341039, _a_(341038, _n_(341037, "sys", lambda: sys), "exit"), 'Program terminated.')
    _l_(341040)

_c_(341043, _n_(341042, "print", lambda: print), 'You will have 5 seconds to answer each question \nIf you fail 5 times or more, the program will exit')
_l_(341044)
_c_(341047, _a_(341046, _n_(341045, "time", lambda: time), "sleep"), 3)
_l_(341048)
_c_(341050, _n_(341049, "print", lambda: print), 'Good luck!')
_l_(341051)
_c_(341054, _a_(341053, _n_(341052, "time", lambda: time), "sleep"), 2)
_l_(341055)

q1 = _a_(341060, _c_(341059, _n_(341056, "print", lambda: print), _c_(341058, _n_(341057, "input", lambda: input), "What is the capital of England?")), "title")
_l_(341061)
if _n_(341062, "q1", lambda: q1) == 'London':
    _l_(341069)

    _c_(341064, _n_(341063, "points", lambda: points))
    _l_(341065)
else:
    _c_(341067, _n_(341066, "fail", lambda: fail))
    _l_(341068)
_c_(341071, _n_(341070, "printtotal", lambda: printtotal))
_l_(341072)

q2 = _a_(341077, _c_(341076, _n_(341073, "print", lambda: print), _c_(341075, _n_(341074, "input", lambda: input), "Who is the prime minister's wife?")), "title")
_l_(341078)
if _n_(341079, "q2", lambda: q2) == 'Samantha' or 'Samantha Cameron':
    _l_(341086)

    _c_(341081, _n_(341080, "points", lambda: points))
    _l_(341082)
else: 
   _c_(341084, _n_(341083, "fail", lambda: fail))
   _l_(341085)
_c_(341088, _n_(341087, "printtotal", lambda: printtotal))
_l_(341089)

_c_(341091, _n_(341090, "print", lambda: print), 'How would you say \'I came, I saw, I conquered\' in latin?')
_l_(341092)
_c_(341094, _n_(341093, "print", lambda: print), 'a) veni, vidi, vici')
_l_(341095)
_c_(341097, _n_(341096, "print", lambda: print), 'b) veni, vedi, vici')
_l_(341098)
_c_(341100, _n_(341099, "print", lambda: print), 'c) vini, vedi, vici')
_l_(341101)
q3 = _c_(341105, _n_(341102, "print", lambda: print), _c_(341104, _n_(341103, "input", lambda: input), 'Type the letter here:'))
_l_(341106)
if _n_(341107, "q3", lambda: q3) == 'a)' or 'a':
    _l_(341114)

    _c_(341109, _n_(341108, "points", lambda: points))
    _l_(341110)
else:
    _c_(341112, _n_(341111, "fail", lambda: fail))
    _l_(341113)
_c_(341116, _n_(341115, "printtotal", lambda: printtotal))
_l_(341117)