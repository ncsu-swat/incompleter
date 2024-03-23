# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(90816)


    def __init__(self, data=None):
        _l_(90815)

        _n_(90810, "self", lambda: self).data = _n_(90811, "data", lambda: data)
        _l_(90812)
        _n_(90813, "self", lambda: self).next = None
        _l_(90814)

class singly_linked_list:
    _l_(90892)


    def __init__(self):
        _l_(90823)

        _n_(90817, "self", lambda: self).tail = None
        _l_(90818)
        _n_(90819, "self", lambda: self).head = None
        _l_(90820)
        _n_(90821, "self", lambda: self).count = 0
        _l_(90822)

    def append_item(self, data):
        _l_(90846)

        node = _c_(90826, _n_(90824, "Node", lambda: Node), _n_(90825, "data", lambda: data))
        _l_(90827)
        if _a_(90829, _n_(90828, "self", lambda: self), "head"):
            _l_(90843)

            _a_(90831, _n_(90830, "self", lambda: self), "head").next = _n_(90832, "node", lambda: node)
            _l_(90833)
            _n_(90834, "self", lambda: self).head = _n_(90835, "node", lambda: node)
            _l_(90836)
        else:
            _n_(90837, "self", lambda: self).tail = _n_(90838, "node", lambda: node)
            _l_(90839)
            _n_(90840, "self", lambda: self).head = _n_(90841, "node", lambda: node)
            _l_(90842)
        _n_(90844, "self", lambda: self).count += 1
        _l_(90845)

    def delete_item(self, data):
        _l_(90877)

        current = _a_(90848, _n_(90847, "self", lambda: self), "tail")
        _l_(90849)
        prev = _a_(90851, _n_(90850, "self", lambda: self), "tail")
        _l_(90852)
        while _n_(90853, "current", lambda: current):
            _l_(90876)

            if _a_(90855, _n_(90854, "current", lambda: current), "data") == _n_(90856, "data", lambda: data):
                _l_(90872)

                if _n_(90857, "current", lambda: current) == _a_(90859, _n_(90858, "self", lambda: self), "tail"):
                    _l_(90868)

                    _n_(90860, "self", lambda: self).tail = _a_(90862, _n_(90861, "current", lambda: current), "next")
                    _l_(90863)
                else:
                    _n_(90864, "prev", lambda: prev).next = _a_(90866, _n_(90865, "current", lambda: current), "next")
                    _l_(90867)
                _n_(90869, "self", lambda: self).count -= 1
                _l_(90870)
                aux = ""
                _l_(90871)
                return aux
            current = _a_(90874, _n_(90873, "current", lambda: current), "next")
            _l_(90875)

    def iterate_item(self):
        _l_(90891)

        current_item = _a_(90879, _n_(90878, "self", lambda: self), "tail")
        _l_(90880)
        while _n_(90881, "current_item", lambda: current_item):
            _l_(90890)

            val = _a_(90883, _n_(90882, "current_item", lambda: current_item), "data")
            _l_(90884)
            current_item = _a_(90886, _n_(90885, "current_item", lambda: current_item), "next")
            _l_(90887)
            yield _n_(90888, "val", lambda: val)
            _l_(90889)
items = _c_(90894, _n_(90893, "singly_linked_list", lambda: singly_linked_list))
_l_(90895)
_c_(90898, _a_(90897, _n_(90896, "items", lambda: items), "append_item"), 'PHP')
_l_(90899)
_c_(90902, _a_(90901, _n_(90900, "items", lambda: items), "append_item"), 'Python')
_l_(90903)
_c_(90906, _a_(90905, _n_(90904, "items", lambda: items), "append_item"), 'C#')
_l_(90907)
_c_(90910, _a_(90909, _n_(90908, "items", lambda: items), "append_item"), 'C++')
_l_(90911)
_c_(90914, _a_(90913, _n_(90912, "items", lambda: items), "append_item"), 'Java')
_l_(90915)
_c_(90917, _n_(90916, "print", lambda: print), 'Original list:')
_l_(90918)
for val in _c_(90921, _a_(90920, _n_(90919, "items", lambda: items), "iterate_item")):
    _l_(90926)

    _c_(90924, _n_(90922, "print", lambda: print), _n_(90923, "val", lambda: val))
    _l_(90925)
_c_(90928, _n_(90927, "print", lambda: print), '\nAfter removing the last item from the list:')
_l_(90929)
_c_(90932, _a_(90931, _n_(90930, "items", lambda: items), "delete_item"), 'Java')
_l_(90933)
for val in _c_(90936, _a_(90935, _n_(90934, "items", lambda: items), "iterate_item")):
    _l_(90941)

    _c_(90939, _n_(90937, "print", lambda: print), _n_(90938, "val", lambda: val))
    _l_(90940)