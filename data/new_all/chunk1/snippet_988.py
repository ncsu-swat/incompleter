# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59066080/attributeerror-module-django-contrib-auth-has-no-attribute-models-what-am
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  from django.db import models
  _l_(382299)

except ImportError:
  pass
try:
  from django.contrib import auth
  _l_(382301)

except ImportError:
  pass

class User(_a_(382304, _a_(382303, _n_(382302, "auth", lambda: auth), "models"), "User"),_a_(382307, _a_(382306, _n_(382305, "auth", lambda: auth), "models"), "PermissionsMixin")):
  _l_(382314)


  def __str__(self):
    _l_(382313)

    aux = _c_(382311, _a_(382308, "@{}", "format"), _a_(382310, _n_(382309, "self", lambda: self), "username"))
    _l_(382312)
    return aux