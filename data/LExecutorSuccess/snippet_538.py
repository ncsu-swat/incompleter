# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6886493/get-all-object-attributes-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class MyObj(_n_(1539070, "object", lambda: object)):
  _l_(1539076)

  def __init__(self):
    _l_(1539075)

    _n_(1539071, "self", lambda: self).name = 'Chuck Norris'
    _l_(1539072)
    _n_(1539073, "self", lambda: self).phone = '+6661'
    _l_(1539074)

obj = _c_(1539078, _n_(1539077, "MyObj", lambda: MyObj))
_l_(1539079)
_c_(1539083, _n_(1539080, "print", lambda: print), _a_(1539082, _n_(1539081, "obj", lambda: obj), "__dict__"))
_l_(1539084)
_c_(1539089, _n_(1539085, "print", lambda: print), _c_(1539088, _n_(1539086, "dir", lambda: dir), _n_(1539087, "obj", lambda: obj)))
_l_(1539090)

# Output:  
# obj.__dict__ --> {'phone': '+6661', 'name': 'Chuck Norris'}
#
# dir(obj)     --> ['__class__', '__delattr__', '__dict__', '__doc__',
#               '__format__', '__getattribute__', '__hash__', 
#               '__init__', '__module__', '__new__', '__reduce__', 
#               '__reduce_ex__', '__repr__', '__setattr__', 
#               '__sizeof__', '__str__', '__subclasshook__', 
#               '__weakref__', 'name', 'phone']

