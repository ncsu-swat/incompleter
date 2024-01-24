# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71946233/typeerror-textiowrapper-seek-takes-no-keyword-arguments
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(386569, _n_(386568, "open", lambda: open), "t.txt",'a+') as f:
    _l_(386588)

    _c_(386572, _a_(386571, _n_(386570, "f", lambda: f), "seek"), 0,)
    _l_(386573)
    _c_(386578, _n_(386574, "print", lambda: print), _c_(386577, _a_(386576, _n_(386575, "f", lambda: f), "readlines")))
    _l_(386579)
    _c_(386582, _a_(386581, _n_(386580, "f", lambda: f), "seek"), 0,whence=0)
    _l_(386583)
    _c_(386586, _a_(386585, _n_(386584, "f", lambda: f), "write"), "12\n23\n32")
    _l_(386587)