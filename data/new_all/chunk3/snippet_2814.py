# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62237600/how-do-i-get-around-typeerror-input-expected-at-most-1-argument-got-2-in-line
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(565140, _n_(565139, "print", lambda: print), "Hello")
_l_(565141)
name = _c_(565143, _n_(565142, "input", lambda: input), "What is your name?")
_l_(565144)
age = _c_(565149, _n_(565145, "int", lambda: int), _c_(565148, _n_(565146, "input", lambda: input), "What is your age?",_n_(565147, "name", lambda: name))) 
_l_(565150) 
_c_(565156, _n_(565151, "print", lambda: print), "Thank you",_n_(565152, "name", lambda: name), "you have been registered an age of",_c_(565155, _n_(565153, "int", lambda: int), _n_(565154, "age", lambda: age)))
_l_(565157)