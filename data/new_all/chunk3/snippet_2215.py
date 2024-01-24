# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57454762/how-to-fix-typeerror-in-python-when-comparing-values-of-two-nodes-of-a-linked-li
######## Definition of 'Node', 'LinkedList' #######
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(568441)

    def __init__(self, value):
        _l_(568434)

        _n_(568429, "self", lambda: self).value = _n_(568430, "value", lambda: value)
        _l_(568431)
        _n_(568432, "self", lambda: self).next = None
        _l_(568433)

    def __repr__(self):
        _l_(568440)

        aux = _c_(568438, _n_(568435, "str", lambda: str), _a_(568437, _n_(568436, "self", lambda: self), "value"))
        _l_(568439)
        return aux

class LinkedList:
    _l_(568470)

    def __init__(self, head):
        _l_(568445)

        _n_(568442, "self", lambda: self).head = _n_(568443, "head", lambda: head)
        _l_(568444)

    def append(self, value):
        _l_(568469)

        if _a_(568447, _n_(568446, "self", lambda: self), "head") is None:
            _l_(568454)

            _n_(568448, "self", lambda: self).head = _c_(568451, _n_(568449, "Node", lambda: Node), _n_(568450, "value", lambda: value))
            _l_(568452)
            aux = ""
            _l_(568453)
            return aux
        node = _a_(568456, _n_(568455, "self", lambda: self), "head")
        _l_(568457)
        while _a_(568459, _n_(568458, "node", lambda: node), "next") is not None:
            _l_(568463)

            node = _a_(568461, _n_(568460, "node", lambda: node), "next")
            _l_(568462)
        _n_(568464, "node", lambda: node).next = _c_(568467, _n_(568465, "Node", lambda: Node), _n_(568466, "value", lambda: value))
        _l_(568468)

#### Where I need help #####
def merge(list1, list2):
    _l_(568534)

    """
    Merge and sort two linked lists

    Args:
       list1, list2: two linked lists that need to be merged. They need to be pre-sorted before being passed as a argument.
    Returns:
       linked-list: Merged and sorted linked-list, a combination of list1 and list2
    """
    merged = _c_(568472, _n_(568471, "LinkedList", lambda: LinkedList), None) # create an empty linked list
    _l_(568473) # create an empty linked list
    if _n_(568474, "list1", lambda: list1) is None:
        _l_(568477)

        aux = _n_(568475, "list2", lambda: list2)
        _l_(568476)
        return aux
    if _n_(568478, "list2", lambda: list2) is None:
        _l_(568481)

        aux = _n_(568479, "list1", lambda: list1)
        _l_(568480)
        return aux

    list1_elt = _a_(568483, _n_(568482, "list1", lambda: list1), "head")  # start with heads of the two lists
    _l_(568484)  # start with heads of the two lists
    list2_elt = _a_(568486, _n_(568485, "list2", lambda: list2), "head")
    _l_(568487)

    while _n_(568488, "list1_elt", lambda: list1_elt) is not None or _n_(568489, "list2_elt", lambda: list2_elt) is not None:
        _l_(568531)

        # val1 = int(str(list1_elt.value))
        # val2 = int(str(list2_elt.value))
        # condition = val1 < val2
        # print("List1 value: {} and List2 value: {}".format(list1_elt.value, list2_elt.value))
        if _n_(568490, "list1_elt", lambda: list1_elt) is None:
            _l_(568530)

            # print("List2 value: {}".format(list2_elt.value))
            _c_(568494, _a_(568492, _n_(568491, "merged", lambda: merged), "append"), _n_(568493, "list2_elt", lambda: list2_elt))
            _l_(568495)
            list2_elt = _a_(568497, _n_(568496, "list2_elt", lambda: list2_elt), "next")
            _l_(568498)
        elif _n_(568499, "list2_elt", lambda: list2_elt) is None:
            _l_(568529)

            # print("List1 value: {}".format(list1_elt.value))
            _c_(568503, _a_(568501, _n_(568500, "merged", lambda: merged), "append"), _n_(568502, "list1_elt", lambda: list1_elt))
            _l_(568504)
            list1_elt = _a_(568506, _n_(568505, "list1_elt", lambda: list1_elt), "next")
            _l_(568507)
        elif _a_(568509, _n_(568508, "list1_elt", lambda: list1_elt), "value") <= _a_(568511, _n_(568510, "list2_elt", lambda: list2_elt), "value"):
            _l_(568528)

        # elif val1 <= val2:
        # elif condition:
            # print("List1 value: {}".format(list1_elt.value))
            _c_(568515, _a_(568513, _n_(568512, "merged", lambda: merged), "append"), _n_(568514, "list1_elt", lambda: list1_elt))
            _l_(568516)
            list1_elt = _a_(568518, _n_(568517, "list1_elt", lambda: list1_elt), "next")
            _l_(568519)
        else:
            # print("List2 value: {}".format(list2_elt.value))
            _c_(568523, _a_(568521, _n_(568520, "merged", lambda: merged), "append"), _n_(568522, "list2_elt", lambda: list2_elt))
            _l_(568524)
            list2_elt = _a_(568526, _n_(568525, "list2_elt", lambda: list2_elt), "next")
            _l_(568527)
    aux = _n_(568532, "merged", lambda: merged)
    _l_(568533)
    return aux


##### TEST CODE TO CHECK #######

# First Test scenario
linked_list = _c_(568538, _n_(568535, "LinkedList", lambda: LinkedList), _c_(568537, _n_(568536, "Node", lambda: Node), 1))
_l_(568539)
_c_(568544, _a_(568541, _n_(568540, "linked_list", lambda: linked_list), "append"), _c_(568543, _n_(568542, "Node", lambda: Node), 3))
_l_(568545)
_c_(568550, _a_(568547, _n_(568546, "linked_list", lambda: linked_list), "append"), _c_(568549, _n_(568548, "Node", lambda: Node), 5))
_l_(568551)

second_linked_list = _c_(568555, _n_(568552, "LinkedList", lambda: LinkedList), _c_(568554, _n_(568553, "Node", lambda: Node), 2))
_l_(568556)
_c_(568559, _a_(568558, _n_(568557, "second_linked_list", lambda: second_linked_list), "append"), 4)
_l_(568560)

merged = _c_(568564, _n_(568561, "merge", lambda: merge), _n_(568562, "linked_list", lambda: linked_list), _n_(568563, "second_linked_list", lambda: second_linked_list))
_l_(568565)
node = _a_(568567, _n_(568566, "merged", lambda: merged), "head")
_l_(568568)
while _n_(568569, "node", lambda: node) is not None:
    _l_(568578)

    #This should print 1 2 3 4 5
    _c_(568573, _n_(568570, "print", lambda: print), _a_(568572, _n_(568571, "node", lambda: node), "value"))
    _l_(568574)
    node = _a_(568576, _n_(568575, "node", lambda: node), "next")
    _l_(568577)