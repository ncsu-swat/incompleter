# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64098471/typeerror-for-dictionaries-unsupported-operand-types-for-int-and-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
ds = {'A': ['1', '3', '2', '5', '6'], 'B': ['1', '3', '2', '5'], 'C': ['3', '6', '8', '9', '7']} 
_l_(364028) 

def analysis():
  _l_(364051)

  lists = _n_(364029, "ds", lambda: ds)["A"]
  _l_(364030)
  length = _c_(364033, _n_(364031, "len", lambda: len), _n_(364032, "lists", lambda: lists))
  _l_(364034)
  _c_(364037, _n_(364035, "print", lambda: print), _n_(364036, "lists", lambda: lists))
  _l_(364038)
  _c_(364041, _n_(364039, "print", lambda: print), _n_(364040, "length", lambda: length))
  _l_(364042)
  total = _c_(364045, _n_(364043, "sum", lambda: sum), _n_(364044, "lists", lambda: lists))
  _l_(364046)
  _c_(364049, _n_(364047, "print", lambda: print), _n_(364048, "total", lambda: total))
  _l_(364050)
 
_c_(364053, _n_(364052, "analysis", lambda: analysis))
_l_(364054)