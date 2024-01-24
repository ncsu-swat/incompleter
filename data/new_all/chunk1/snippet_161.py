# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48997007/check-for-string-in-response-content-raising-typeerror-a-bytes-like-object-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
   import requests
   _l_(416111)

except ImportError:
   pass

r = _c_(416114, _a_(416113, _n_(416112, "requests", lambda: requests), "get"), 'https://www.eventbrite.co.uk/o/piers-test-16613670281')
_l_(416115)
text = 'Sorry, there are no upcoming events'
_l_(416116)

if _n_(416117, "text", lambda: text) in _a_(416119, _n_(416118, "r", lambda: r), "content"):
   _l_(416123)

   _c_(416121, _n_(416120, "print", lambda: print), 'No Upcoming Events')
   _l_(416122)