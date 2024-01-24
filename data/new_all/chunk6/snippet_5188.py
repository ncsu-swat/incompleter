# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64098471/typeerror-for-dictionaries-unsupported-operand-types-for-int-and-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
ds = {'A': ['1', '3', '2', '5', '6'], 'B': ['1', '3', '2', '5'], 'C': ['3', '6', '8', '9', '7']} 
_l_(344953) 

def analysis():
  _l_(344976)

  lists = _n_(344954, "ds", lambda: ds)["A"]
  _l_(344955)
  length = _c_(344958, _n_(344956, "len", lambda: len), _n_(344957, "lists", lambda: lists))
  _l_(344959)
  _c_(344962, _n_(344960, "print", lambda: print), _n_(344961, "lists", lambda: lists))
  _l_(344963)
  _c_(344966, _n_(344964, "print", lambda: print), _n_(344965, "length", lambda: length))
  _l_(344967)
  total = _c_(344970, _n_(344968, "sum", lambda: sum), _n_(344969, "lists", lambda: lists))
  _l_(344971)
  _c_(344974, _n_(344972, "print", lambda: print), _n_(344973, "total", lambda: total))
  _l_(344975)
 
_c_(344978, _n_(344977, "analysis", lambda: analysis))
_l_(344979)