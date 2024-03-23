# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(26819, "object", lambda: object)):
    _l_(26827)


    def __init__(self, value=None, next=None, prev=None):
        _l_(26826)

        _n_(26820, "self", lambda: self).value = _n_(26821, "value", lambda: value)
        _l_(26822)
        _n_(26823, "self", lambda: self).prev = _n_(26824, "prev", lambda: prev)
        _l_(26825)

class doubly_linked_list(_n_(26828, "object", lambda: object)):
    _l_(26955)


    def __init__(self):
        _l_(26835)

        _n_(26829, "self", lambda: self).head = None
        _l_(26830)
        _n_(26831, "self", lambda: self).tail = None
        _l_(26832)
        _n_(26833, "self", lambda: self).count = 0
        _l_(26834)

    def append_item(self, value):
        _l_(26863)

        new_item = _c_(26838, _n_(26836, "Node", lambda: Node), _n_(26837, "value", lambda: value), None, None)
        _l_(26839)
        if _a_(26841, _n_(26840, "self", lambda: self), "head") is None:
            _l_(26860)

            _n_(26842, "self", lambda: self).head = _n_(26843, "new_item", lambda: new_item)
            _l_(26844)
            _n_(26845, "self", lambda: self).tail = _a_(26847, _n_(26846, "self", lambda: self), "head")
            _l_(26848)
        else:
            _n_(26849, "new_item", lambda: new_item).prev = _a_(26851, _n_(26850, "self", lambda: self), "tail")
            _l_(26852)
            _a_(26854, _n_(26853, "self", lambda: self), "tail").next = _n_(26855, "new_item", lambda: new_item)
            _l_(26856)
            _n_(26857, "self", lambda: self).tail = _n_(26858, "new_item", lambda: new_item)
            _l_(26859)
        _n_(26861, "self", lambda: self).count += 1
        _l_(26862)

    def iter(self):
        _l_(26877)

        current = _a_(26865, _n_(26864, "self", lambda: self), "head")
        _l_(26866)
        while _n_(26867, "current", lambda: current):
            _l_(26876)

            item_val = _a_(26869, _n_(26868, "current", lambda: current), "value")
            _l_(26870)
            current = _a_(26872, _n_(26871, "current", lambda: current), "next")
            _l_(26873)
            yield _n_(26874, "item_val", lambda: item_val)
            _l_(26875)

    def print_foward(self):
        _l_(26886)

        for node in _c_(26880, _a_(26879, _n_(26878, "self", lambda: self), "iter")):
            _l_(26885)

            _c_(26883, _n_(26881, "print", lambda: print), _n_(26882, "node", lambda: node))
            _l_(26884)

    def search_item(self, val):
        _l_(26896)

        for node in _c_(26889, _a_(26888, _n_(26887, "self", lambda: self), "iter")):
            _l_(26894)

            if _n_(26890, "val", lambda: val) == _n_(26891, "node", lambda: node):
                _l_(26893)

                aux = True
                _l_(26892)
                return aux
        aux = False
        _l_(26895)
        return aux

    def delete(self, value):
        _l_(26954)

        current = _a_(26898, _n_(26897, "self", lambda: self), "head")
        _l_(26899)
        node_deleted = False
        _l_(26900)
        if _n_(26901, "current", lambda: current) is None:
            _l_(26949)

            node_deleted = False
            _l_(26902)
        elif _a_(26904, _n_(26903, "current", lambda: current), "value") == _n_(26905, "value", lambda: value):
            _l_(26948)

            _n_(26906, "self", lambda: self).head = _a_(26908, _n_(26907, "current", lambda: current), "next")
            _l_(26909)
            _a_(26911, _n_(26910, "self", lambda: self), "head").prev = None
            _l_(26912)
            node_deleted = True
            _l_(26913)
        elif _a_(26916, _a_(26915, _n_(26914, "self", lambda: self), "tail"), "value") == _n_(26917, "value", lambda: value):
            _l_(26947)

            _n_(26918, "self", lambda: self).tail = _a_(26921, _a_(26920, _n_(26919, "self", lambda: self), "tail"), "prev")
            _l_(26922)
            _a_(26924, _n_(26923, "self", lambda: self), "tail").next = None
            _l_(26925)
            node_deleted = True
            _l_(26926)
        else:
            while _n_(26927, "current", lambda: current):
                _l_(26946)

                if _a_(26929, _n_(26928, "current", lambda: current), "value") == _n_(26930, "value", lambda: value):
                    _l_(26942)

                    _a_(26932, _n_(26931, "current", lambda: current), "prev").next = _a_(26934, _n_(26933, "current", lambda: current), "next")
                    _l_(26935)
                    _a_(26937, _n_(26936, "current", lambda: current), "next").prev = _a_(26939, _n_(26938, "current", lambda: current), "prev")
                    _l_(26940)
                    node_deleted = True
                    _l_(26941)
                current = _a_(26944, _n_(26943, "current", lambda: current), "next")
                _l_(26945)
        if _n_(26950, "node_deleted", lambda: node_deleted):
            _l_(26953)

            _n_(26951, "self", lambda: self).count -= 1
            _l_(26952)
items = _c_(26957, _n_(26956, "doubly_linked_list", lambda: doubly_linked_list))
_l_(26958)
_c_(26961, _a_(26960, _n_(26959, "items", lambda: items), "append_item"), 'PHP')
_l_(26962)
_c_(26965, _a_(26964, _n_(26963, "items", lambda: items), "append_item"), 'Python')
_l_(26966)
_c_(26969, _a_(26968, _n_(26967, "items", lambda: items), "append_item"), 'C#')
_l_(26970)
_c_(26973, _a_(26972, _n_(26971, "items", lambda: items), "append_item"), 'C++')
_l_(26974)
_c_(26977, _a_(26976, _n_(26975, "items", lambda: items), "append_item"), 'Java')
_l_(26978)
_c_(26981, _a_(26980, _n_(26979, "items", lambda: items), "append_item"), 'SQL')
_l_(26982)
_c_(26984, _n_(26983, "print", lambda: print), 'Original list:')
_l_(26985)
_c_(26988, _a_(26987, _n_(26986, "items", lambda: items), "print_foward"))
_l_(26989)
_c_(26992, _a_(26991, _n_(26990, "items", lambda: items), "delete"), 'Java')
_l_(26993)
_c_(26996, _a_(26995, _n_(26994, "items", lambda: items), "delete"), 'Python')
_l_(26997)
_c_(26999, _n_(26998, "print", lambda: print), '\nList after deleting two items:')
_l_(27000)
_c_(27003, _a_(27002, _n_(27001, "items", lambda: items), "print_foward"))
_l_(27004)