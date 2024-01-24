# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51711655/python-typeerror-init-got-an-unexpected-keyword-argument-serialized-opti
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
init = _c_(428966, _a_(428965, _n_(428964, "tf", lambda: tf), "global_variables_initializer"))
_l_(428967)
sess = _c_(428970, _a_(428969, _n_(428968, "tf", lambda: tf), "Session"))
_l_(428971)
writer = _c_(428977, _a_(428974, _a_(428973, _n_(428972, "tf", lambda: tf), "summary"), "FileWriter"), "logs/",_a_(428976, _n_(428975, "sess", lambda: sess), "graph")) 
_l_(428978) 
_c_(428982, _a_(428980, _n_(428979, "sess", lambda: sess), "run"), _n_(428981, "init", lambda: init))
_l_(428983)