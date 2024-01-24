# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68360067/how-wo-fix-typeerror-unsupported-operand-types-for-datetime-time-and-da
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import sys
  _l_(630434)

except ImportError:
  pass
try:
  import os
  _l_(630436)

except ImportError:
  pass
try:
  import datetime
  _l_(630438)

except ImportError:
  pass
try:
  import boto3
  _l_(630440)

except ImportError:
  pass
try:
  import pytz
  _l_(630442)

except ImportError:
  pass
try:
  import time
  _l_(630444)

except ImportError:
  pass


ST = "05:30"
_l_(630445)

def test():
  _l_(630500)

  WST1 = _c_(630452, _a_(630451, _c_(630450, _a_(630448, _a_(630447, _n_(630446, "datetime", lambda: datetime), "datetime"), "strptime"), _n_(630449, "ST", lambda: ST), '%H:%M'), "time"))
  _l_(630453)
  _c_(630456, _n_(630454, "print", lambda: print), _n_(630455, "WST1", lambda: WST1))
  _l_(630457)
  _c_(630461, _n_(630458, "print", lambda: print), _a_(630460, _n_(630459, "WST1", lambda: WST1), "tzinfo"))
  _l_(630462)
  ST1 = _c_(630467, _a_(630465, _a_(630464, _n_(630463, "pytz", lambda: pytz), "utc"), "localize"), _n_(630466, "WST1", lambda: WST1))
  _l_(630468)
  _c_(630472, _n_(630469, "print", lambda: print), _a_(630471, _n_(630470, "ST1", lambda: ST1), "tzinfo"))
  _l_(630473)
  # ST1 = timezone.localize(WST1)
  _c_(630476, _n_(630474, "print", lambda: print), _n_(630475, "ST1", lambda: ST1))
  _l_(630477)
  tz1 = _c_(630480, _a_(630479, _n_(630478, "pytz", lambda: pytz), "timezone"), 'Europe/London')
  _l_(630481)
  T1 = _c_(630485, _a_(630483, _n_(630482, "tz1", lambda: tz1), "localize"), _n_(630484, "WST1", lambda: WST1))
  _l_(630486)
  T1 = _c_(630494, _a_(630492, _c_(630491, _a_(630488, _n_(630487, "ST1", lambda: ST1), "replace"), tzinfo=_a_(630490, _n_(630489, "pytz", lambda: pytz), "utc")), "astimezone"), _n_(630493, "tz1", lambda: tz1))
  _l_(630495)
  _c_(630498, _n_(630496, "print", lambda: print), _n_(630497, "T1", lambda: T1))
  _l_(630499)



_c_(630502, _n_(630501, "test", lambda: test))
_l_(630503)