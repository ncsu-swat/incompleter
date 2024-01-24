# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56931505/python3-slicing-typeerror-list-indices-must-be-integers-or-slices-not-list
# Get the response from the API endpoint.
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
response = _c_(420238, _a_(420237, _n_(420236, "requests", lambda: requests), "get"), "http://api.open-notify.org/astros.json")
_l_(420239)
data = _c_(420242, _a_(420241, _n_(420240, "response", lambda: response), "json"))
_l_(420243)
_c_(420246, _n_(420244, "print", lambda: print), _n_(420245, "data", lambda: data)["people"][0:2]["name"])
_l_(420247)