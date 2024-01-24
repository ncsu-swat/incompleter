# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60092328/conecting-to-rest-api-with-python-typeerror-dict-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def jprint(obj):
    _l_(703105)

    # create a formatted string of the Python JSON object
    text = _c_(703099, _a_(703097, _n_(703096, "json", lambda: json), "dumps"), _n_(703098, "obj", lambda: obj), sort_keys=True, indent=4)
    _l_(703100)
    _c_(703103, _n_(703101, "print", lambda: print), _n_(703102, "text", lambda: text))
    _l_(703104)

parametros = {"type" : "isodistance",
              "value" : 10000,
              "lat" : 43.334098,
              "lng" : -1.7920697,
              "approx" : 1000,
              "mobility" : "motor_vehicle",
              "speedType" : "normal",
              "reduceQueue" : "false",
              "avoidTolls" : "true",
              "restrictedAreas" : "false",
              "fastestRouting" : "true",
              "concavity" : 6,
              "buffering" : 3,
              "reqId" : "A57X"}
_l_(703106)

respuesta = _c_(703110, _a_(703108, _n_(703107, "request", lambda: request), "GET"), "http://www.iso4app.net/rest/1.3/isoline.geojson?licKey=4ECDEFB8-1F48-4A0B-A5CA-5B0420162922", _n_(703109, "parametros", lambda: parametros))
_l_(703111)