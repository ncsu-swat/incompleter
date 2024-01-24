# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49222033/raise-typeerrorrepro-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  from marshmallow import Schema, fields
  _l_(624709)

except ImportError:
  pass

class Product():
  _l_(624728)

  def __init__(self, ident, name, description, category):
    _l_(624722)

    _n_(624710, "self", lambda: self).ident = _n_(624711, "ident", lambda: ident)
    _l_(624712)
    _n_(624713, "self", lambda: self).name = _n_(624714, "name", lambda: name)
    _l_(624715)
    _n_(624716, "self", lambda: self).description = _n_(624717, "description", lambda: description)
    _l_(624718)
    _n_(624719, "self", lambda: self).category = _n_(624720, "category", lambda: category)
    _l_(624721)

  def __repr__(self):
    _l_(624727)

    aux = _c_(624725, _a_(624723, '<Expense(name={self.description!r})>', "format"), self=_n_(624724, "self", lambda: self))
    _l_(624726)
    return aux

class ProductSchema(_n_(624729, "Schema", lambda: Schema)):
  _l_(624746)

  ident = _c_(624732, _a_(624731, _n_(624730, "fields", lambda: fields), "Str"))
  _l_(624733)
  name = _c_(624736, _a_(624735, _n_(624734, "fields", lambda: fields), "Str"))
  _l_(624737)
  category = _c_(624740, _a_(624739, _n_(624738, "fields", lambda: fields), "Str"))
  _l_(624741)
  description = _c_(624744, _a_(624743, _n_(624742, "fields", lambda: fields), "Str"))
  _l_(624745)