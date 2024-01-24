# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59471398/typeerror-a-bytes-like-object-is-required-not-str-in-python3-6-8
#!/usr/bin/env python
from __future__ import print_function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(652270)
try:
  import json
  _l_(652272)

except ImportError:
  pass
try:
  import sys
  _l_(652274)

except ImportError:
  pass
try:
  import os
  _l_(652276)

except ImportError:
  pass
try:
  import re
  _l_(652278)

except ImportError:
  pass
try:
  import subprocess
  _l_(652280)

except ImportError:
  pass
try:
  import datetime
  _l_(652282)

except ImportError:
  pass
try:
  from glob import glob
  _l_(652284)

except ImportError:
  pass
try:
  import boto3
  _l_(652286)

except ImportError:
  pass

class VariableCollector:
  _l_(652326)

  def getall(self):
    _l_(652325)

    collected_vars = {}
    _l_(652287)
    for name in _c_(652290, _n_(652288, "dir", lambda: dir), _n_(652289, "self", lambda: self)):
      _l_(652322)

      #name = name.decode()
      if _c_(652293, _a_(652292, _n_(652291, "name", lambda: name), "startswith"), "get_"):
        _l_(652321)

        _c_(652296, _n_(652294, "debug", lambda: debug), "VariableCollector - Calling: %s" % _n_(652295, "name", lambda: (name)))
        _l_(652297)
        method = _c_(652301, _n_(652298, "getattr", lambda: getattr), _n_(652299, "self", lambda: self), _n_(652300, "name", lambda: name))
        _l_(652302)
        _n_(652303, "collected_vars", lambda: collected_vars)[_n_(652304, "name", lambda: name)] = _c_(652306, _n_(652305, "method", lambda: method))
        _l_(652307)
        _n_(652308, "collected_vars", lambda: collected_vars)[_n_(652309, "name", lambda: name) + ":no_quotes"] = _c_(652313, _a_(652312, _n_(652310, "collected_vars", lambda: collected_vars)[_n_(652311, "name", lambda: name)], "replace"), "'","")
        _l_(652314)

        _c_(652319, _n_(652315, "debug", lambda: debug), "Function: [%s] Value: [%s]" % ( _n_(652316, "name", lambda: name), _n_(652317, "collected_vars", lambda: collected_vars)[_n_(652318, "name", lambda: name)] ))
        _l_(652320)
    aux = _n_(652323, "collected_vars", lambda: collected_vars)
    _l_(652324)
    return aux