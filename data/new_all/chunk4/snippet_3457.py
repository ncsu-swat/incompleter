# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73979950/attribute-error-in-linkedlist-implementation
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node():
 _l_(591341)


 def __init__(self, value):
  _l_(591340)

  _n_(591335, "self", lambda: self).value = _n_(591336, "value", lambda: value)
  _l_(591337)
  _n_(591338, "self", lambda: self).next = None
  _l_(591339)

class LinkedList():
 _l_(591479)


 def __init__(self):
  _l_(591346)

  _n_(591342, "self", lambda: self).head = None
  _l_(591343)
  _n_(591344, "self", lambda: self).tail = None
  _l_(591345)

 def append(self, value):
  _l_(591372)

  new_node = _c_(591349, _n_(591347, "Node", lambda: Node), _n_(591348, "value", lambda: value))
  _l_(591350)
  if _a_(591352, _n_(591351, "self", lambda: self), "head") == None:
   _l_(591371)

   _n_(591353, "self", lambda: self).head = _n_(591354, "new_node", lambda: new_node)
   _l_(591355)
   _n_(591356, "self", lambda: self).tail = _a_(591358, _n_(591357, "self", lambda: self), "head")
   _l_(591359)
   _n_(591360, "self", lambda: self).length = 1
   _l_(591361)
  else:
   _a_(591363, _n_(591362, "self", lambda: self), "tail").next = _n_(591364, "new_node", lambda: new_node)
   _l_(591365)
   _n_(591366, "self", lambda: self).tail = _n_(591367, "new_node", lambda: new_node) 
   _l_(591368) 
   _n_(591369, "self", lambda: self).length += 1
   _l_(591370)

 def prepend(self,value):
  _l_(591398)

  new_node = _c_(591375, _n_(591373, "Node", lambda: Node), _n_(591374, "value", lambda: value))
  _l_(591376)
  if _a_(591378, _n_(591377, "self", lambda: self), "head") == None:
   _l_(591397)

   _n_(591379, "self", lambda: self).head = _n_(591380, "new_node", lambda: new_node)
   _l_(591381)
   _n_(591382, "self", lambda: self).tail = _a_(591384, _n_(591383, "self", lambda: self), "head")
   _l_(591385)
   _n_(591386, "self", lambda: self).length += 1
   _l_(591387)
  else:
   _n_(591388, "new_node", lambda: new_node).next = _a_(591390, _n_(591389, "self", lambda: self), "head") 
   _l_(591391) 
   _n_(591392, "self", lambda: self).head = _n_(591393, "new_node", lambda: new_node)
   _l_(591394)
   _n_(591395, "self", lambda: self).length += 1
   _l_(591396)

 def insert(self, index, value):
  _l_(591440)

  new_node = _c_(591401, _n_(591399, "Node", lambda: Node), _n_(591400, "value", lambda: value))
  _l_(591402)
  if _n_(591403, "index", lambda: index)>=_a_(591405, _n_(591404, "self", lambda: self), "length"):
   _l_(591439)

   _c_(591409, _a_(591407, _n_(591406, "self", lambda: self), "append"), _n_(591408, "value", lambda: value))
   _l_(591410)
   aux = ""
   _l_(591411)
   return aux
  elif _n_(591412, "index", lambda: index) < 1:
   _l_(591438)

   _c_(591416, _a_(591414, _n_(591413, "self", lambda: self), "prepend"), _n_(591415, "value", lambda: value))
   _l_(591417)
   aux = ""
   _l_(591418)
   return aux
  else:
   header = _c_(591422, _a_(591420, _n_(591419, "self", lambda: self), "traverseToIndex"), _n_(591421, "index", lambda: index)-1)
   _l_(591423)
   pointer= _a_(591428, _c_(591427, _a_(591425, _n_(591424, "self", lambda: self), "traverseToIndex"), _n_(591426, "index", lambda: index)-1), "next") 
   _l_(591429) 
   _n_(591430, "header", lambda: header).next = _n_(591431, "new_node", lambda: new_node) 
   _l_(591432) 
   _n_(591433, "new_node", lambda: new_node).next = _n_(591434, "pointer", lambda: pointer) 
   _l_(591435) 
   _n_(591436, "self", lambda: self).length += 1
   _l_(591437)

 def traverseToIndex(self, index):
  _l_(591454)

  counter = 0
  _l_(591441)
  current_node = _a_(591443, _n_(591442, "self", lambda: self), "head")
  _l_(591444)
  while _n_(591445, "counter", lambda: counter)<=_n_(591446, "index", lambda: index):
   _l_(591451)

   current_node = _a_(591448, _n_(591447, "self", lambda: self), "next") 
   _l_(591449) 
   counter += 1
   _l_(591450)
  aux = _n_(591452, "current_node", lambda: current_node) 
  _l_(591453) 
  return aux 
 
 def printl(self):
  _l_(591478)

  temp = _a_(591456, _n_(591455, "self", lambda: self), "head")
  _l_(591457)
  while _n_(591458, "temp", lambda: temp) != None:
   _l_(591470)

   _c_(591462, _n_(591459, "print", lambda: print), _a_(591461, _n_(591460, "temp", lambda: temp), "value") , end = ' ')
   _l_(591463)
   temp = _a_(591465, _n_(591464, "temp", lambda: temp), "next")
   _l_(591466)
   _c_(591468, _n_(591467, "print", lambda: print))
   _l_(591469)
  _c_(591476, _n_(591471, "print", lambda: print), 'Length = '+_c_(591475, _n_(591472, "str", lambda: str), _a_(591474, _n_(591473, "self", lambda: self), "length"))) 
  _l_(591477) 

l = _c_(591481, _n_(591480, "LinkedList", lambda: LinkedList))
_l_(591482)
_c_(591485, _a_(591484, _n_(591483, "l", lambda: l), "append"), 10)
_l_(591486)
_c_(591489, _a_(591488, _n_(591487, "l", lambda: l), "append"), 5)
_l_(591490)
_c_(591493, _a_(591492, _n_(591491, "l", lambda: l), "append"), 6)
_l_(591494)
_c_(591497, _a_(591496, _n_(591495, "l", lambda: l), "prepend"), 1)
_l_(591498)
_c_(591501, _a_(591500, _n_(591499, "l", lambda: l), "insert"), 3,99)
_l_(591502)