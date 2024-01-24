# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56976222/typeerror-tuple-indices-must-be-integers-or-slices-not-dict
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
tax_rates = {
  'AB' : .05,
  'BC' : .12,
  'MN' : .13,
  'NB' : .15,
  'NL' : .15,
  'NT' : .05,
  'NS' : .15,
  'ON' : .13,
  'PE' : .15,
  'QC' : .1475,
  'ST' : .11,
  'YK' : .05
},
_l_(692421)

for key in _n_(692422, "tax_rates", lambda: tax_rates):
  _l_(692428)

  _c_(692426, _n_(692423, "print", lambda: print), _n_(692424, "tax_rates", lambda: tax_rates)[_n_(692425, "key", lambda: key)])
  _l_(692427)

for key in _c_(692431, _a_(692430, _n_(692429, "tax_rates", lambda: tax_rates), "items")):
  _l_(692436)

  _c_(692434, _n_(692432, "print", lambda: print), _n_(692433, "key", lambda: key))
  _l_(692435)

for value in _c_(692439, _a_(692438, _n_(692437, "tax_rates", lambda: tax_rates), "items")):
  _l_(692444)

  _c_(692442, _n_(692440, "print", lambda: print), _n_(692441, "value", lambda: value))
  _l_(692443)

for key,value in _c_(692447, _a_(692446, _n_(692445, "tax_rates", lambda: tax_rates), "items")):
  _l_(692453)

  _c_(692451, _n_(692448, "print", lambda: print), _n_(692449, "key", lambda: key),_n_(692450, "value", lambda: value))
  _l_(692452)

tax = _c_(692456, _a_(692455, _n_(692454, "tax_rates", lambda: tax_rates), "keys"))
_l_(692457)
_c_(692460, _n_(692458, "print", lambda: print), _n_(692459, "tax", lambda: tax))
_l_(692461)