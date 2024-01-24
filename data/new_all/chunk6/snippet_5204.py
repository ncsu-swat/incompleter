# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61303661/typeerror-list-indices-must-be-integers-or-slices-not-str-error-while-iterati
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
list1 = ['Ganga', 'Narmada', 'Kaveri', 'Tapi', 'Yamuna']
_l_(359076)
sum1 = 0
_l_(359077)
for i in _n_(359078, "list1", lambda: list1):
  _l_(359094)

  for j in _n_(359079, "list1", lambda: list1)[_n_(359080, "i", lambda: i)]:
    _l_(359093)

    sum1 += _c_(359085, _n_(359081, "ord", lambda: ord), _c_(359084, _n_(359082, "int", lambda: int), _n_(359083, "j", lambda: j)))
    _l_(359086)
    _c_(359091, _a_(359088, _n_(359087, "list1", lambda: list1), "replace"), _n_(359089, "i", lambda: i), _n_(359090, "sum1", lambda: sum1))
    _l_(359092)
_c_(359097, _n_(359095, "print", lambda: print), _n_(359096, "list1", lambda: list1))
_l_(359098)