# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/30021368/python-typeerror-not-all-arguments-converted-during-string-formatting-while-rea
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import rnumb
    _l_(438254)

except ImportError:
    pass
try:
    import file
    _l_(438256)

except ImportError:
    pass

def create():
    _l_(438292)

    name    = _c_(438258, _n_(438257, "input", lambda: input), "What is your name? ")
    _l_(438259)
    attack  = _c_(438262, _a_(438261, _n_(438260, "rnumb", lambda: rnumb), "randn"), 1,3)
    _l_(438263)
    defense = _c_(438266, _a_(438265, _n_(438264, "rnumb", lambda: rnumb), "randn"), 1,3)
    _l_(438267)
    agility = _c_(438270, _a_(438269, _n_(438268, "rnumb", lambda: rnumb), "randn"), 1,3)
    _l_(438271)

    _c_(438275, _a_(438273, _n_(438272, "file", lambda: file), "write"), "name",_n_(438274, "name", lambda: name))
    _l_(438276)
    _c_(438280, _a_(438278, _n_(438277, "file", lambda: file), "write"), "attack",_n_(438279, "attack", lambda: attack))
    _l_(438281)
    _c_(438285, _a_(438283, _n_(438282, "file", lambda: file), "write"), "defense",_n_(438284, "defense", lambda: defense))
    _l_(438286)
    _c_(438290, _a_(438288, _n_(438287, "file", lambda: file), "write"), "agility",_n_(438289, "agility", lambda: agility))
    _l_(438291)