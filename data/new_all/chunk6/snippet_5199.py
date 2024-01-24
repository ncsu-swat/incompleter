# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61303661/typeerror-list-indices-must-be-integers-or-slices-not-str-error-while-iterati
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
list1 = ['Ganga', 'Narmada', 'Kaveri', 'Tapi', 'Yamuna']
_l_(336777)
sum1 = 0
_l_(336778)
for i in _n_(336779, "list1", lambda: list1):
  _l_(336795)

  for j in _n_(336780, "list1", lambda: list1)[_n_(336781, "i", lambda: i)]:
    _l_(336794)

    sum1 += _c_(336786, _n_(336782, "ord", lambda: ord), _c_(336785, _n_(336783, "int", lambda: int), _n_(336784, "j", lambda: j)))
    _l_(336787)
    _c_(336792, _a_(336789, _n_(336788, "list1", lambda: list1), "replace"), _n_(336790, "i", lambda: i), _n_(336791, "sum1", lambda: sum1))
    _l_(336793)
_c_(336798, _n_(336796, "print", lambda: print), _n_(336797, "list1", lambda: list1))
_l_(336799)