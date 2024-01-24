# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56551423/attributeerror-int-object-has-no-attribute-data
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(535219)

    def __init__(self, data):
        _l_(535138)

        _n_(535131, "self", lambda: self).data = _n_(535132, "data", lambda: data)
        _l_(535133)
        _n_(535134, "self", lambda: self).leftChild = None
        _l_(535135)
        _n_(535136, "self", lambda: self).rightChild = None
        _l_(535137)

    def insert(self, data):
        _l_(535181)

        if _a_(535140, _n_(535139, "self", lambda: self), "data") is not None:
            _l_(535180)

            if _n_(535141, "data", lambda: data) < _a_(535143, _n_(535142, "self", lambda: self), "data"):
                _l_(535176)

                if _a_(535145, _n_(535144, "self", lambda: self), "leftChild") is None:
                    _l_(535157)

                    _n_(535146, "self", lambda: self).leftChild = _c_(535149, _n_(535147, "Node", lambda: Node), _n_(535148, "data", lambda: data))
                    _l_(535150)
                else:
                    _c_(535155, _a_(535153, _a_(535152, _n_(535151, "self", lambda: self), "leftChild"), "insert"), _n_(535154, "data", lambda: data))
                    _l_(535156)
            elif _n_(535158, "data", lambda: data) > _a_(535160, _n_(535159, "self", lambda: self), "data"):
                _l_(535175)

                if _a_(535162, _n_(535161, "self", lambda: self), "rightChild") is None:
                    _l_(535174)

                    _n_(535163, "self", lambda: self).rightChild = _c_(535166, _n_(535164, "Node", lambda: Node), _n_(535165, "data", lambda: data))
                    _l_(535167)
                else:
                    _c_(535172, _a_(535170, _a_(535169, _n_(535168, "self", lambda: self), "rightChild"), "insert"), _n_(535171, "data", lambda: data))
                    _l_(535173)
        else:
            _n_(535177, "self", lambda: self).data = _n_(535178, "data", lambda: data)
            _l_(535179)

    def traverseLevelOrder(self):
        _l_(535218)

        queue = []
        _l_(535182)
        _c_(535187, _a_(535184, _n_(535183, "queue", lambda: queue), "append"), _a_(535186, _n_(535185, "self", lambda: self), "data"))
        _l_(535188)
        while _n_(535189, "queue", lambda: queue):
            _l_(535217)

            # Print front of queue and remove it from queue
            _c_(535193, _n_(535190, "print", lambda: print), _a_(535192, _n_(535191, "queue", lambda: queue)[0], "data"))
            _l_(535194)
            temp = _c_(535197, _a_(535196, _n_(535195, "queue", lambda: queue), "pop"), 0)
            _l_(535198)

            # Enqueue left child
            if _a_(535200, _n_(535199, "temp", lambda: temp), "leftChild") is not None:
                _l_(535207)

                _c_(535205, _a_(535202, _n_(535201, "queue", lambda: queue), "append"), _a_(535204, _n_(535203, "temp", lambda: temp), "leftChild"))
                _l_(535206)

            # Enqueue right child
            if _a_(535209, _n_(535208, "temp", lambda: temp), "rightChild") is not None:
                _l_(535216)

                _c_(535214, _a_(535211, _n_(535210, "queue", lambda: queue), "append"), _a_(535213, _n_(535212, "temp", lambda: temp), "rightChild"))
                _l_(535215)


class BST:
    _l_(535248)

    def __init__(self):
        _l_(535222)

        _n_(535220, "self", lambda: self).rootNode = None
        _l_(535221)

    def insert(self, data):
        _l_(535237)

        if _a_(535224, _n_(535223, "self", lambda: self), "rootNode") is None:
            _l_(535236)

            _n_(535225, "self", lambda: self).rootNode = _c_(535228, _n_(535226, "Node", lambda: Node), _n_(535227, "data", lambda: data))
            _l_(535229)
        else:
            _c_(535234, _a_(535232, _a_(535231, _n_(535230, "self", lambda: self), "rootNode"), "insert"), _n_(535233, "data", lambda: data))
            _l_(535235)

    def traverseLevelOrder(self):
        _l_(535247)

        if _a_(535239, _n_(535238, "self", lambda: self), "rootNode") is None:
            _l_(535246)

            aux = ""
            _l_(535240)
            return aux
        else:
            _c_(535244, _a_(535243, _a_(535242, _n_(535241, "self", lambda: self), "rootNode"), "traverseLevelOrder"))
            _l_(535245)


bst = _c_(535250, _n_(535249, "BST", lambda: BST))
_l_(535251)
_c_(535254, _a_(535253, _n_(535252, "bst", lambda: bst), "insert"), 2)
_l_(535255)
_c_(535258, _a_(535257, _n_(535256, "bst", lambda: bst), "insert"), 4)
_l_(535259)
_c_(535262, _a_(535261, _n_(535260, "bst", lambda: bst), "insert"), 1)
_l_(535263)
_c_(535266, _a_(535265, _n_(535264, "bst", lambda: bst), "insert"), 3)
_l_(535267)
_c_(535270, _a_(535269, _n_(535268, "bst", lambda: bst), "traverseLevelOrder"))
_l_(535271)