# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71704716/typeerror-list-indices-must-be-integers-or-slices-not-str-error-appears-while
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import requests
  _l_(626066)

except ImportError:
  pass
try:
  import xmltodict
  _l_(626068)

except ImportError:
  pass

url = 'http://192.168.1.8:8060/query/apps'
_l_(626069)
text = _a_(626074, _c_(626073, _a_(626071, _n_(626070, "requests", lambda: requests), "get"), _n_(626072, "url", lambda: url)), "text")
_l_(626075)
#content = """
#<?xml version="1.0" encoding="UTF-8"?>
#<apps>
#<app id="31012" type="menu" #version="2.0.53">Vudu Movie &amp; #TV Store</app>
#</apps>
#"""
text = _c_(626078, _a_(626077, _n_(626076, "text", lambda: text), "split"), '\n')
_l_(626079)
text = _n_(626080, "text", lambda: text)[1:]
_l_(626081)
text = _c_(626084, _a_(626082, '', "join"), _n_(626083, "text", lambda: text))
_l_(626085)
data = _c_(626089, _a_(626087, _n_(626086, "xmltodict", lambda: xmltodict), "parse"), _n_(626088, "text", lambda: text))
_l_(626090)
data = _c_(626093, _n_(626091, "dict", lambda: dict), _n_(626092, "data", lambda: data))
_l_(626094)

for key1, value1 in _c_(626097, _a_(626096, _n_(626095, "data", lambda: data), "items")):
  _l_(626114)

  for key2, value2 in _c_(626100, _a_(626099, _n_(626098, "value1", lambda: value1), "items")):
    _l_(626113)

    _c_(626103, _n_(626101, "print", lambda: print), _n_(626102, "value2", lambda: value2)['@id'])
    _l_(626104)
    _c_(626107, _n_(626105, "print", lambda: print), _n_(626106, "value2", lambda: value2)['@type'])
    _l_(626108)
    _c_(626111, _n_(626109, "print", lambda: print), _n_(626110, "value2", lambda: value2)['#text'])
    _l_(626112)