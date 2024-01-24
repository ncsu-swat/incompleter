# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65224915/why-am-i-unable-to-use-list-object-syntax-and-am-met-with-attributeerror-when-r
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
 import csv
 _l_(632352)

except ImportError:
 pass

class Volunteer:
 _l_(632366)

 def __init__(self,name,coin_type,weight_of_bag,true_count):
  _l_(632365)

  _n_(632353, "self", lambda: self).name = _n_(632354, "name", lambda: name)
  _l_(632355)
  _n_(632356, "self", lambda: self).coin_type = _n_(632357, "coin_type", lambda: coin_type)        #a function allowing me to class the data
  _l_(632358)        #a function allowing me to class the data
  _n_(632359, "self", lambda: self).weight_of_bag = _n_(632360, "weight_of_bag", lambda: weight_of_bag)
  _l_(632361)
  _n_(632362, "self", lambda: self).TrueCount = _n_(632363, "true_count", lambda: true_count)
  _l_(632364)

with _c_(632368, _n_(632367, "open", lambda: open), "CoinCount.txt","r+") as csvfile:
 _l_(632383)

 volunteers = []
 _l_(632369)
 for line in _n_(632370, "csvfile", lambda: csvfile):
  _l_(632382)

  _c_(632380, _a_(632372, _n_(632371, "volunteers", lambda: volunteers), "append"), _c_(632379, _n_(632373, "Volunteer", lambda: Volunteer), *_c_(632378, _a_(632377, _c_(632376, _a_(632375, _n_(632374, "line", lambda: line), "strip")), "split"), ',')))
  _l_(632381)