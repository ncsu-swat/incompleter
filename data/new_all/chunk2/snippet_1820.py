# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51813378/attributeerror-worker-object-has-no-attribute-idf
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
w_dist = {} 
_l_(475142) 
for w in _n_(475143, "workers", lambda: workers):
  _l_(475168)

  f_dist = {} 
  _l_(475144) 
  for f in _n_(475145, "fences", lambda: fences):
    _l_(475162)

    if _n_(475146, "f", lambda: f) != _n_(475147, "self", lambda: self):
      _l_(475161)

      distance = _c_(475154, _a_(475149, _n_(475148, "self", lambda: self), "rect_distance"), _a_(475151, _n_(475150, "w", lambda: w), "rect"), _a_(475153, _n_(475152, "f", lambda: f), "rect")) 
      _l_(475155) 
      _n_(475156, "f_dist", lambda: f_dist)[_a_(475158, _n_(475157, "f", lambda: f), "idf")] = _n_(475159, "distance", lambda: distance) 
      _l_(475160) 
  _n_(475163, "w_dist", lambda: w_dist)[_a_(475165, _n_(475164, "w", lambda: w), "idw")] = _n_(475166, "f_dist", lambda: f_dist) 
  _l_(475167) 