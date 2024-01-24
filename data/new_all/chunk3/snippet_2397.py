# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46610160/os-ftruncate-is-showing-some-error-while-execution-error-like-typeerror-a-byt
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os,sys
    _l_(573467)

except ImportError:
    pass

sr=_c_(573474, _a_(573469, _n_(573468, "os", lambda: os), "open"), "sri.txt",_a_(573471, _n_(573470, "os", lambda: os), "O_RDWR")|_a_(573473, _n_(573472, "os", lambda: os), "O_CREAT"))
_l_(573475)

_c_(573479, _a_(573477, _n_(573476, "os", lambda: os), "write"), _n_(573478, "sr", lambda: sr),"This is the test-This is test")
_l_(573480)

_c_(573484, _a_(573482, _n_(573481, "os", lambda: os), "ftruncate"), _n_(573483, "sr", lambda: sr),10)
_l_(573485)

_c_(573489, _a_(573487, _n_(573486, "os", lambda: os), "lseek"), _n_(573488, "sr", lambda: sr),0,0)
_l_(573490)

str=_c_(573494, _a_(573492, _n_(573491, "os", lambda: os), "read"), _n_(573493, "sr", lambda: sr),100)
_l_(573495)

_c_(573498, _n_(573496, "print", lambda: print), "Read string is:",_n_(573497, "str", lambda: str))
_l_(573499)

_c_(573503, _a_(573501, _n_(573500, "os", lambda: os), "close"), _n_(573502, "sr", lambda: sr))
_l_(573504)

_c_(573506, _n_(573505, "print", lambda: print), "closed the file successfully!!")
_l_(573507)