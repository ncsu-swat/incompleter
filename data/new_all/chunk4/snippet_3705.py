# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69555882/type-error-init-requires-1-positional-argument-yet-2-are-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class change_about(_n_(595304, "UpdateView", lambda: UpdateView)):
 _l_(595334)

 def get_object(self, queryset=None):
  _l_(595313)

  aux = _c_(595311, _a_(595307, _a_(595306, _n_(595305, "User", lambda: User), "objects"), "get"), user=_a_(595310, _a_(595309, _n_(595308, "self", lambda: self), "request"), "user"))
  _l_(595312)

  return aux

 def form_valid(self, form):
  _l_(595333)


  instance = _a_(595315, _n_(595314, "form", lambda: form), "instance") # This is the new object being saved
  _l_(595316) # This is the new object being saved
  _n_(595317, "instance", lambda: instance).user = _a_(595320, _a_(595319, _n_(595318, "self", lambda: self), "request"), "user")
  _l_(595321)
  _c_(595324, _a_(595323, _n_(595322, "instance", lambda: instance), "save"))
  _l_(595325)
  aux = _c_(595331, _a_(595329, _n_(595326, "super", lambda: super)(_n_(595327, "change_about", lambda: change_about), _n_(595328, "self", lambda: self)), "form_valid"), _n_(595330, "form", lambda: form))
  _l_(595332)

  return aux