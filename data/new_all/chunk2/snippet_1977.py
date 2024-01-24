# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73985803/i-was-trying-to-add-elements-in-a-linked-list-in-python-but-i-am-getting-typeer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(421690)

    def __init__(self, data=None, next=None):
        _l_(421689)

        _n_(421683, "self", lambda: self).data = _n_(421684, "data", lambda: data)
        _l_(421685)
        _n_(421686, "self", lambda: self).next = _n_(421687, "next", lambda: next)
        _l_(421688)


class linked_list:
    _l_(421810)

    def __init__(self):
        _l_(421693)

        _n_(421691, "self", lambda: self).head = None
        _l_(421692)

    def insert_at_begining(self, data):
        _l_(421703)

        node = _c_(421698, _n_(421694, "Node", lambda: Node), _n_(421695, "data", lambda: data), _a_(421697, _n_(421696, "self", lambda: self), "head"))
        _l_(421699)
        _n_(421700, "self", lambda: self).head = _n_(421701, "node", lambda: node)
        _l_(421702)

    def print(self):
        _l_(421728)

        itr = _a_(421705, _n_(421704, "self", lambda: self), "head")
        _l_(421706)
        llstr = ''
        _l_(421707)
        while _n_(421708, "itr", lambda: itr):
            _l_(421723)

            suffix = ''
            _l_(421709)
            if _a_(421711, _n_(421710, "itr", lambda: itr), "next"):
                _l_(421713)

                suffix = '-->'
                _l_(421712)
            llstr += _c_(421717, _n_(421714, "str", lambda: str), _a_(421716, _n_(421715, "itr", lambda: itr), "data")) + _n_(421718, "suffix", lambda: suffix)
            _l_(421719)
            itr = _a_(421721, _n_(421720, "itr", lambda: itr), "next")
            _l_(421722)
        _c_(421726, _n_(421724, "print", lambda: print), _n_(421725, "llstr", lambda: llstr))
        _l_(421727)

    def get_length(self):
        _l_(421744)

        count = 0
        _l_(421729)
        itr = _a_(421731, _n_(421730, "self", lambda: self), "head")
        _l_(421732)
        while _n_(421733, "itr", lambda: itr):
            _l_(421739)

            count = _n_(421734, "count", lambda: count)+1
            _l_(421735)
            itr = _a_(421737, _n_(421736, "itr", lambda: itr), "next")
            _l_(421738)
        _c_(421742, _n_(421740, "print", lambda: print), _n_(421741, "count", lambda: count))
        _l_(421743)
    
    def insert_at_end(self, data):
        _l_(421768)

        if _a_(421746, _n_(421745, "self", lambda: self), "head") is None:
            _l_(421753)

            _n_(421747, "self", lambda: self).head = _c_(421750, _n_(421748, "Node", lambda: Node), _n_(421749, "data", lambda: data), None)
            _l_(421751)
            aux = ""
            _l_(421752)
            return aux
        
        itr = _a_(421755, _n_(421754, "self", lambda: self), "head")
        _l_(421756)
        while _a_(421758, _n_(421757, "itr", lambda: itr), "next"):
            _l_(421762)

            itr = _a_(421760, _n_(421759, "itr", lambda: itr), "next")
            _l_(421761)
        _n_(421763, "itr", lambda: itr).next = _c_(421766, _n_(421764, "Node", lambda: Node), _n_(421765, "data", lambda: data), None)
        _l_(421767)

    def insert_at(self, index, data):
        _l_(421809)

        if _n_(421769, "index", lambda: index) < 0 or _n_(421770, "index", lambda: index) > _c_(421773, _a_(421772, _n_(421771, "self", lambda: self), "get_length")):
            _l_(421777)

            raise _c_(421775, _n_(421774, "Exception", lambda: Exception), "Invalid Index")
            _l_(421776)
        
        if _n_(421778, "index", lambda: index) == 0:
            _l_(421785)

            _c_(421782, _a_(421780, _n_(421779, "self", lambda: self), "insert_at_begining"), _n_(421781, "data", lambda: data))
            _l_(421783)
            aux = ""
            _l_(421784)
            return aux

        itr = _a_(421787, _n_(421786, "self", lambda: self), "head")
        _l_(421788)
        count = 0
        _l_(421789)
        while _n_(421790, "itr", lambda: itr):
            _l_(421808)

            if _n_(421791, "count", lambda: count) == _n_(421792, "index", lambda: index)-1:
                _l_(421803)

                node = _c_(421797, _n_(421793, "Node", lambda: Node), _n_(421794, "data", lambda: data), _a_(421796, _n_(421795, "itr", lambda: itr), "next"))
                _l_(421798)
                _n_(421799, "itr", lambda: itr).next = _n_(421800, "node", lambda: node)
                _l_(421801)
                break
                _l_(421802)
            
            itr = _a_(421805, _n_(421804, "itr", lambda: itr), "next")
            _l_(421806)
            count += 1
            _l_(421807)

if _n_(421811, "__name__", lambda: __name__) == '__main__':
    _l_(421847)

    root = _c_(421813, _n_(421812, "linked_list", lambda: linked_list)) 
    _l_(421814) 
    _c_(421817, _a_(421816, _n_(421815, "root", lambda: root), "insert_at_begining"), 5)
    _l_(421818)
    _c_(421821, _a_(421820, _n_(421819, "root", lambda: root), "insert_at_begining"), 15)
    _l_(421822)
    _c_(421825, _a_(421824, _n_(421823, "root", lambda: root), "insert_at_begining"), 10)
    _l_(421826)
    _c_(421829, _a_(421828, _n_(421827, "root", lambda: root), "insert_at_end"), 34)
    _l_(421830)
    _c_(421833, _a_(421832, _n_(421831, "root", lambda: root), "insert_at"), 2, 31)
    _l_(421834)
    _c_(421837, _a_(421836, _n_(421835, "root", lambda: root), "insert_at_end"), 45)
    _l_(421838)
    _c_(421841, _a_(421840, _n_(421839, "root", lambda: root), "print"))
    _l_(421842)
    _c_(421845, _a_(421844, _n_(421843, "root", lambda: root), "get_length"))
    _l_(421846)