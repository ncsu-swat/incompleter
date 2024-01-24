# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53933467/program-shows-typeerror-while-passing-a-dictionary-into-a-function-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def f(**kwargs):
   _l_(438414)

   _c_(438412, _n_(438410, "print", lambda: print), _n_(438411, "kwargs", lambda: kwargs))
   _l_(438413)

d = {'0': 'a', '1': 'b', '2': 'c', '3': 'd'}   
_l_(438415)   
_c_(438418, _n_(438416, "f", lambda: f), **_n_(438417, "d", lambda: d))   # {'0': 'a', '1': 'b', '2': 'c', '3': 'd'}
_l_(438419)   # {'0': 'a', '1': 'b', '2': 'c', '3': 'd'}

d = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}   
_l_(438420)   
_c_(438423, _n_(438421, "f", lambda: f), **_n_(438422, "d", lambda: d))   # TypeError: f() keywords must be strings
_l_(438424)   # TypeError: f() keywords must be strings