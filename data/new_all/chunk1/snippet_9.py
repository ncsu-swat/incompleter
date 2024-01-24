# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/31019854/typeerror-cant-use-a-string-pattern-on-a-bytes-like-object-in-re-findall
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
   import urllib.request
   _l_(409079)

except ImportError:
   pass
try:
   import re
   _l_(409081)

except ImportError:
   pass

url = "http://www.google.com"
_l_(409082)
regex = r'<title>(,+?)</title>'
_l_(409083)
pattern  = _c_(409087, _a_(409085, _n_(409084, "re", lambda: re), "compile"), _n_(409086, "regex", lambda: regex))
_l_(409088)

with _c_(409092, _a_(409090, _a_(409089, urllib, "request"), "urlopen"), _n_(409091, "url", lambda: url)) as response:
   _l_(409097)

   html = _c_(409095, _a_(409094, _n_(409093, "response", lambda: response), "read"))
   _l_(409096)

title = _c_(409102, _a_(409099, _n_(409098, "re", lambda: re), "findall"), _n_(409100, "pattern", lambda: pattern), _n_(409101, "html", lambda: html))
_l_(409103)
_c_(409106, _n_(409104, "print", lambda: print), _n_(409105, "title", lambda: title))
_l_(409107)