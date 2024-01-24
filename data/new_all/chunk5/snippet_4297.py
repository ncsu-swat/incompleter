# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60092328/conecting-to-rest-api-with-python-typeerror-dict-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def jprint(obj):
    _l_(706347)

    # create a formatted string of the Python JSON object
    text = _c_(706341, _a_(706339, _n_(706338, "json", lambda: json), "dumps"), _n_(706340, "obj", lambda: obj), sort_keys=True, indent=4)
    _l_(706342)
    _c_(706345, _n_(706343, "print", lambda: print), _n_(706344, "text", lambda: text))
    _l_(706346)

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
_l_(706348)

respuesta = _c_(706352, _a_(706350, _n_(706349, "request", lambda: request), "GET"), "http://www.iso4app.net/rest/1.3/isoline.geojson?licKey=4ECDEFB8-1F48-4A0B-A5CA-5B0420162922", _n_(706351, "parametros", lambda: parametros))
_l_(706353)