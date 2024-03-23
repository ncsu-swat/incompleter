# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(7739)


    def __init__(self, data=None):
        _l_(7738)

        _n_(7733, "self", lambda: self).data = _n_(7734, "data", lambda: data)
        _l_(7735)
        _n_(7736, "self", lambda: self).next = None
        _l_(7737)

class singly_linked_list:
    _l_(7815)


    def __init__(self):
        _l_(7744)

        _n_(7740, "self", lambda: self).tail = None
        _l_(7741)
        _n_(7742, "self", lambda: self).head = None
        _l_(7743)

    def append_item(self, data):
        _l_(7767)

        node = _c_(7747, _n_(7745, "Node", lambda: Node), _n_(7746, "data", lambda: data))
        _l_(7748)
        if _a_(7750, _n_(7749, "self", lambda: self), "head"):
            _l_(7764)

            _a_(7752, _n_(7751, "self", lambda: self), "head").next = _n_(7753, "node", lambda: node)
            _l_(7754)
            _n_(7755, "self", lambda: self).head = _n_(7756, "node", lambda: node)
            _l_(7757)
        else:
            _n_(7758, "self", lambda: self).tail = _n_(7759, "node", lambda: node)
            _l_(7760)
            _n_(7761, "self", lambda: self).head = _n_(7762, "node", lambda: node)
            _l_(7763)
        _n_(7765, "self", lambda: self).count += 1
        _l_(7766)

    def delete_item(self, data):
        _l_(7800)

        current = _a_(7769, _n_(7768, "self", lambda: self), "tail")
        _l_(7770)
        prev = _a_(7772, _n_(7771, "self", lambda: self), "tail")
        _l_(7773)
        while _n_(7774, "current", lambda: current):
            _l_(7799)

            if _a_(7776, _n_(7775, "current", lambda: current), "data") == _n_(7777, "data", lambda: data):
                _l_(7793)

                if _n_(7778, "current", lambda: current) == _a_(7780, _n_(7779, "self", lambda: self), "tail"):
                    _l_(7789)

                    _n_(7781, "self", lambda: self).tail = _a_(7783, _n_(7782, "current", lambda: current), "next")
                    _l_(7784)
                else:
                    _n_(7785, "prev", lambda: prev).next = _a_(7787, _n_(7786, "current", lambda: current), "next")
                    _l_(7788)
                _n_(7790, "self", lambda: self).count -= 1
                _l_(7791)
                aux = ""
                _l_(7792)
                return aux
            prev = _n_(7794, "current", lambda: current)
            _l_(7795)
            current = _a_(7797, _n_(7796, "current", lambda: current), "next")
            _l_(7798)

    def iterate_item(self):
        _l_(7814)

        current_item = _a_(7802, _n_(7801, "self", lambda: self), "tail")
        _l_(7803)
        while _n_(7804, "current_item", lambda: current_item):
            _l_(7813)

            val = _a_(7806, _n_(7805, "current_item", lambda: current_item), "data")
            _l_(7807)
            current_item = _a_(7809, _n_(7808, "current_item", lambda: current_item), "next")
            _l_(7810)
            yield _n_(7811, "val", lambda: val)
            _l_(7812)
items = _c_(7817, _n_(7816, "singly_linked_list", lambda: singly_linked_list))
_l_(7818)
_c_(7821, _a_(7820, _n_(7819, "items", lambda: items), "append_item"), 'PHP')
_l_(7822)
_c_(7825, _a_(7824, _n_(7823, "items", lambda: items), "append_item"), 'Python')
_l_(7826)
_c_(7829, _a_(7828, _n_(7827, "items", lambda: items), "append_item"), 'C#')
_l_(7830)
_c_(7833, _a_(7832, _n_(7831, "items", lambda: items), "append_item"), 'C++')
_l_(7834)
_c_(7837, _a_(7836, _n_(7835, "items", lambda: items), "append_item"), 'Java')
_l_(7838)
_c_(7840, _n_(7839, "print", lambda: print), 'Original list:')
_l_(7841)
for val in _c_(7844, _a_(7843, _n_(7842, "items", lambda: items), "iterate_item")):
    _l_(7849)

    _c_(7847, _n_(7845, "print", lambda: print), _n_(7846, "val", lambda: val))
    _l_(7848)
_c_(7851, _n_(7850, "print", lambda: print), '\nAfter removing the first item from the list:')
_l_(7852)
_c_(7855, _a_(7854, _n_(7853, "items", lambda: items), "delete_item"), 'PHP')
_l_(7856)
for val in _c_(7859, _a_(7858, _n_(7857, "items", lambda: items), "iterate_item")):
    _l_(7864)

    _c_(7862, _n_(7860, "print", lambda: print), _n_(7861, "val", lambda: val))
    _l_(7863)