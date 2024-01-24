# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69555882/type-error-init-requires-1-positional-argument-yet-2-are-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class change_about(_n_(640798, "UpdateView", lambda: UpdateView)):
 _l_(640828)

 def get_object(self, queryset=None):
  _l_(640807)

  aux = _c_(640805, _a_(640801, _a_(640800, _n_(640799, "User", lambda: User), "objects"), "get"), user=_a_(640804, _a_(640803, _n_(640802, "self", lambda: self), "request"), "user"))
  _l_(640806)

  return aux

 def form_valid(self, form):
  _l_(640827)


  instance = _a_(640809, _n_(640808, "form", lambda: form), "instance") # This is the new object being saved
  _l_(640810) # This is the new object being saved
  _n_(640811, "instance", lambda: instance).user = _a_(640814, _a_(640813, _n_(640812, "self", lambda: self), "request"), "user")
  _l_(640815)
  _c_(640818, _a_(640817, _n_(640816, "instance", lambda: instance), "save"))
  _l_(640819)
  aux = _c_(640825, _a_(640823, _n_(640820, "super", lambda: super)(_n_(640821, "change_about", lambda: change_about), _n_(640822, "self", lambda: self)), "form_valid"), _n_(640824, "form", lambda: form))
  _l_(640826)

  return aux