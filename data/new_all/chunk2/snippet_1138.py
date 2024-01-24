# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59481545/add-two-numbers-problem-linked-list-python-leetcode-attributeerror
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Solution:
  _l_(464624)

  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    _l_(464623)

    a = _n_(464540, "l1", lambda: l1) #pointers
    _l_(464541) #pointers
    b = _n_(464542, "l2", lambda: l2) #pointers
    _l_(464543) #pointers
    arr1 = []
    _l_(464544)
    arr2 = []
    _l_(464545)

    while _a_(464547, _n_(464546, "a", lambda: a), "next") is not None:
      _l_(464557)

      _c_(464552, _a_(464549, _n_(464548, "arr1", lambda: arr1), "append"), _a_(464551, _n_(464550, "a", lambda: a), "val"))
      _l_(464553)
      a = _a_(464555, _n_(464554, "a", lambda: a), "next")
      _l_(464556)
    _c_(464562, _a_(464559, _n_(464558, "arr1", lambda: arr1), "append"), _a_(464561, _n_(464560, "a", lambda: a), "val")) #storing the values of linked lists in arrays/lists
    _l_(464563) #storing the values of linked lists in arrays/lists

    while _a_(464565, _n_(464564, "b", lambda: b), "next") is not None:
      _l_(464575)

      _c_(464570, _a_(464567, _n_(464566, "arr2", lambda: arr2), "append"), _a_(464569, _n_(464568, "b", lambda: b), "val"))
      _l_(464571)
      b = _a_(464573, _n_(464572, "b", lambda: b), "next")
      _l_(464574)
    _c_(464580, _a_(464577, _n_(464576, "arr2", lambda: arr2), "append"), _a_(464579, _n_(464578, "b", lambda: b), "val")) #storing the values of linked lists in arrays/lists
    _l_(464581) #storing the values of linked lists in arrays/lists

    rev1 = _c_(464584, _n_(464582, "reversed", lambda: reversed), _n_(464583, "arr1", lambda: arr1)) #reversed list
    _l_(464585) #reversed list
    rev2 = _c_(464588, _n_(464586, "reversed", lambda: reversed), _n_(464587, "arr2", lambda: arr2)) #reversed list
    _l_(464589) #reversed list

    inta = _c_(464594, _a_(464590, "", "join"), _c_(464593, _n_(464591, "str", lambda: str), _n_(464592, "rev1", lambda: rev1))) #converting list to strings
    _l_(464595) #converting list to strings
    intb = _c_(464600, _a_(464596, "", "join"), _c_(464599, _n_(464597, "str", lambda: str), _n_(464598, "rev2", lambda: rev2)))
    _l_(464601)

    c = _c_(464605, _n_(464602, "str", lambda: str), _n_(464603, "inta", lambda: inta) + _n_(464604, "intb", lambda: intb)) #performing addition - the answer we wanted
    _l_(464606) #performing addition - the answer we wanted
    revc = _c_(464609, _n_(464607, "reversed", lambda: reversed), _n_(464608, "c", lambda: c)) #answer in string form - reversed (output in string at present)
    _l_(464610) #answer in string form - reversed (output in string at present)

    #trying to convert into linked list and return it
    q = _n_(464611, "l1", lambda: l1)
    _l_(464612)
    for i in _n_(464613, "revc", lambda: revc):
      _l_(464620)

      _n_(464614, "q", lambda: q).val = _n_(464615, "i", lambda: i)
      _l_(464616)
      q = _a_(464618, _n_(464617, "q", lambda: q), "next")
      _l_(464619)
    aux = _n_(464621, "l1", lambda: l1)
    _l_(464622)
    return aux