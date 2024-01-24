# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57486229/why-is-there-an-attribute-error-inside-the-condition-of-the-while-loop-but-no
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ListNode:
     _l_(576528)

     def __init__(self, x):
          _l_(576527)

          _n_(576522, "self", lambda: self).val = _n_(576523, "x", lambda: x)
          _l_(576524)
          _n_(576525, "self", lambda: self).next = None
          _l_(576526)

class Solution:
     _l_(576591)

     def mergeTwoLists(self, l1: _n_(576529, "ListNode", lambda: ListNode), l2: _n_(576530, "ListNode", lambda: ListNode)) -> _n_(576531, "ListNode", lambda: ListNode):
          _l_(576590)

          result = []
          _l_(576532)
          while _a_(576534, _n_(576533, "l1", lambda: l1), "val") != None and _a_(576536, _n_(576535, "l2", lambda: l2), "val") != None:
               _l_(576560)

               if _a_(576538, _n_(576537, "l1", lambda: l1), "val") >= _a_(576540, _n_(576539, "l2", lambda: l2), "val"):
                    _l_(576559)

                    _c_(576545, _a_(576542, _n_(576541, "result", lambda: result), "append"), _a_(576544, _n_(576543, "l2", lambda: l2), "val"))
                    _l_(576546)
                    l2 = _a_(576548, _n_(576547, "l2", lambda: l2), "next")
                    _l_(576549)
               else:
                   _c_(576554, _a_(576551, _n_(576550, "result", lambda: result), "append"), _a_(576553, _n_(576552, "l1", lambda: l1), "val"))
                   _l_(576555)
                   l1 = _a_(576557, _n_(576556, "l1", lambda: l1), "next")
                   _l_(576558)
          if _a_(576562, _n_(576561, "l1", lambda: l1), "val") != None:
               _l_(576587)

               while _a_(576564, _n_(576563, "l1", lambda: l1), "val") != None:
                    _l_(576574)

                    _c_(576569, _a_(576566, _n_(576565, "result", lambda: result), "append"), _a_(576568, _n_(576567, "l1", lambda: l1), "val"))
                    _l_(576570)
                    l1 = _a_(576572, _n_(576571, "l1", lambda: l1), "next")
                    _l_(576573)
          else:
              while _a_(576576, _n_(576575, "l2", lambda: l2), "val") != None:
                   _l_(576586)

                   _c_(576581, _a_(576578, _n_(576577, "result", lambda: result), "append"), _a_(576580, _n_(576579, "l2", lambda: l2), "val"))
                   _l_(576582)
                   l2 = _a_(576584, _n_(576583, "l2", lambda: l2), "next")
                   _l_(576585)
          aux = _n_(576588, "result", lambda: result)
          _l_(576589)
          return aux