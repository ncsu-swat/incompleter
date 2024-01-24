# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67413780/error-while-rewriting-repr-typeerror-expected-0-arguments-got-1
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class node(_n_(444829, "object", lambda: object)):
    _l_(444860)

    def __init__(self, value):
        _l_(444835)

        _n_(444830, "self", lambda: self).value = _n_(444831, "value", lambda: value)
        _l_(444832)
        _n_(444833, "self", lambda: self).children = []
        _l_(444834)
    def __repr__(self, level=0):
        _l_(444852)

        ret = "\t"*_n_(444836, "level", lambda: level)+_c_(444840, _n_(444837, "repr", lambda: repr), _a_(444839, _n_(444838, "self", lambda: self), "value"))+"\n"
        _l_(444841)
        for child in _a_(444843, _n_(444842, "self", lambda: self), "children"):
            _l_(444849)

            ret += _c_(444847, _a_(444845, _n_(444844, "child", lambda: child), "__repr__"), _n_(444846, "level", lambda: level)+1)
            _l_(444848)
        aux = _n_(444850, "ret", lambda: ret)
        _l_(444851)
        return aux
    def add(self, nod):
        _l_(444859)

        _c_(444857, _a_(444855, _a_(444854, _n_(444853, "self", lambda: self), "children"), "append"), _n_(444856, "nod", lambda: nod))
        _l_(444858)
leaf_1 = [1,4,3]
_l_(444861)
leaf_2 = [2,5,3]
_l_(444862)
leaf_3 = [4,4,3]
_l_(444863)
leaf_4 = [5,5,5]
_l_(444864)
tree = parent = _c_(444867, _n_(444865, "node", lambda: node), _n_(444866, "leaf_1", lambda: leaf_1))
_l_(444868)
_c_(444872, _a_(444870, _n_(444869, "parent", lambda: parent), "add"), _n_(444871, "leaf_2", lambda: leaf_2))
_l_(444873)
_c_(444877, _a_(444875, _n_(444874, "parent", lambda: parent), "add"), _n_(444876, "leaf_3", lambda: leaf_3))
_l_(444878)
_c_(444882, _a_(444880, _n_(444879, "parent", lambda: parent), "add"), _n_(444881, "leaf_4", lambda: leaf_4)) 
_l_(444883) 
_c_(444886, _n_(444884, "print", lambda: print), _n_(444885, "tree", lambda: tree)) # no error without this line
_l_(444887) # no error without this line