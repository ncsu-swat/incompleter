# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(28864, "object", lambda: object)):
    _l_(28875)


    def __init__(self, value=None, next=None, prev=None):
        _l_(28874)

        _n_(28865, "self", lambda: self).value = _n_(28866, "value", lambda: value)
        _l_(28867)
        _n_(28868, "self", lambda: self).next = _n_(28869, "next", lambda: next)
        _l_(28870)
        _n_(28871, "self", lambda: self).prev = _n_(28872, "prev", lambda: prev)
        _l_(28873)

class doubly_linked_list(_n_(28876, "object", lambda: object)):
    _l_(29003)


    def __init__(self):
        _l_(28883)

        _n_(28877, "self", lambda: self).head = None
        _l_(28878)
        _n_(28879, "self", lambda: self).tail = None
        _l_(28880)
        _n_(28881, "self", lambda: self).count = 0
        _l_(28882)

    def append_item(self, value):
        _l_(28911)

        new_item = _c_(28886, _n_(28884, "Node", lambda: Node), _n_(28885, "value", lambda: value), None, None)
        _l_(28887)
        if _a_(28889, _n_(28888, "self", lambda: self), "head") is None:
            _l_(28908)

            _n_(28890, "self", lambda: self).head = _n_(28891, "new_item", lambda: new_item)
            _l_(28892)
            _n_(28893, "self", lambda: self).tail = _a_(28895, _n_(28894, "self", lambda: self), "head")
            _l_(28896)
        else:
            _n_(28897, "new_item", lambda: new_item).prev = _a_(28899, _n_(28898, "self", lambda: self), "tail")
            _l_(28900)
            _a_(28902, _n_(28901, "self", lambda: self), "tail").next = _n_(28903, "new_item", lambda: new_item)
            _l_(28904)
            _n_(28905, "self", lambda: self).tail = _n_(28906, "new_item", lambda: new_item)
            _l_(28907)
        _n_(28909, "self", lambda: self).count += 1
        _l_(28910)

    def iter(self):
        _l_(28925)

        current = _a_(28913, _n_(28912, "self", lambda: self), "head")
        _l_(28914)
        while _n_(28915, "current", lambda: current):
            _l_(28924)

            item_val = _a_(28917, _n_(28916, "current", lambda: current), "value")
            _l_(28918)
            current = _a_(28920, _n_(28919, "current", lambda: current), "next")
            _l_(28921)
            yield _n_(28922, "item_val", lambda: item_val)
            _l_(28923)

    def print_foward(self):
        _l_(28934)

        for node in _c_(28928, _a_(28927, _n_(28926, "self", lambda: self), "iter")):
            _l_(28933)

            _c_(28931, _n_(28929, "print", lambda: print), _n_(28930, "node", lambda: node))
            _l_(28932)

    def search_item(self, val):
        _l_(28944)

        for node in _c_(28937, _a_(28936, _n_(28935, "self", lambda: self), "iter")):
            _l_(28942)

            if _n_(28938, "val", lambda: val) == _n_(28939, "node", lambda: node):
                _l_(28941)

                aux = True
                _l_(28940)
                return aux
        aux = False
        _l_(28943)
        return aux

    def delete(self, value):
        _l_(29002)

        current = _a_(28946, _n_(28945, "self", lambda: self), "head")
        _l_(28947)
        node_deleted = False
        _l_(28948)
        if _n_(28949, "current", lambda: current) is None:
            _l_(28997)

            node_deleted = False
            _l_(28950)
        elif _a_(28952, _n_(28951, "current", lambda: current), "value") == _n_(28953, "value", lambda: value):
            _l_(28996)

            _n_(28954, "self", lambda: self).head = _a_(28956, _n_(28955, "current", lambda: current), "next")
            _l_(28957)
            _a_(28959, _n_(28958, "self", lambda: self), "head").prev = None
            _l_(28960)
            node_deleted = True
            _l_(28961)
        elif _a_(28964, _a_(28963, _n_(28962, "self", lambda: self), "tail"), "value") == _n_(28965, "value", lambda: value):
            _l_(28995)

            _n_(28966, "self", lambda: self).tail = _a_(28969, _a_(28968, _n_(28967, "self", lambda: self), "tail"), "prev")
            _l_(28970)
            _a_(28972, _n_(28971, "self", lambda: self), "tail").next = None
            _l_(28973)
            node_deleted = True
            _l_(28974)
        else:
            while _n_(28975, "current", lambda: current):
                _l_(28994)

                if _a_(28977, _n_(28976, "current", lambda: current), "value") == _n_(28978, "value", lambda: value):
                    _l_(28990)

                    _a_(28980, _n_(28979, "current", lambda: current), "prev").next = _a_(28982, _n_(28981, "current", lambda: current), "next")
                    _l_(28983)
                    _a_(28985, _n_(28984, "current", lambda: current), "next").prev = _a_(28987, _n_(28986, "current", lambda: current), "prev")
                    _l_(28988)
                    node_deleted = True
                    _l_(28989)
                current = _a_(28992, _n_(28991, "current", lambda: current), "next")
                _l_(28993)
        if _n_(28998, "node_deleted", lambda: node_deleted):
            _l_(29001)

            _n_(28999, "self", lambda: self).count -= 1
            _l_(29000)
_c_(29006, _a_(29005, _n_(29004, "items", lambda: items), "append_item"), 'PHP')
_l_(29007)
_c_(29010, _a_(29009, _n_(29008, "items", lambda: items), "append_item"), 'Python')
_l_(29011)
_c_(29014, _a_(29013, _n_(29012, "items", lambda: items), "append_item"), 'C#')
_l_(29015)
_c_(29018, _a_(29017, _n_(29016, "items", lambda: items), "append_item"), 'C++')
_l_(29019)
_c_(29022, _a_(29021, _n_(29020, "items", lambda: items), "append_item"), 'Java')
_l_(29023)
_c_(29026, _a_(29025, _n_(29024, "items", lambda: items), "append_item"), 'SQL')
_l_(29027)
_c_(29029, _n_(29028, "print", lambda: print), 'Original list:')
_l_(29030)
_c_(29033, _a_(29032, _n_(29031, "items", lambda: items), "print_foward"))
_l_(29034)
_c_(29037, _a_(29036, _n_(29035, "items", lambda: items), "delete"), 'Java')
_l_(29038)
_c_(29041, _a_(29040, _n_(29039, "items", lambda: items), "delete"), 'Python')
_l_(29042)
_c_(29044, _n_(29043, "print", lambda: print), '\nList after deleting two items:')
_l_(29045)
_c_(29048, _a_(29047, _n_(29046, "items", lambda: items), "print_foward"))
_l_(29049)