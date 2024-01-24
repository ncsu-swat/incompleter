# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63913377/typeerror-object-of-type-asia-kolkata-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
   from django.db import models
   _l_(570137)

except ImportError:
   pass
try:
   from timezone_field import TimeZoneField
   _l_(570139)

except ImportError:
   pass
# Create your models here.
class Member(_a_(570141, _n_(570140, "models", lambda: models), "Model")):
   _l_(570149)

   tz = _c_(570143, _n_(570142, "TimeZoneField", lambda: TimeZoneField), default='Asia/Kolkata')
   _l_(570144)

   def __str__(self):
      _l_(570148)

      aux = _a_(570146, _n_(570145, "self", lambda: self), "tz")
      _l_(570147)
      return aux