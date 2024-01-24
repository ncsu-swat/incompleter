# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73825029/error-when-defining-a-dictionary-path-as-a-variable-typeerror-string-indices-m
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def updateJson(fileName, pathToValue, updatedValue):
    _l_(677407)

    # Opening JSON file
    f = _c_(677383, _n_(677381, "open", lambda: open), _n_(677382, "fileName", lambda: fileName))
    _l_(677384)
    # returns JSON object as a dictionary
    data = _c_(677388, _a_(677386, _n_(677385, "json", lambda: json), "load"), _n_(677387, "f", lambda: f))
    _l_(677389)
    # Changes the ID value in JSON
    _n_(677390, "data", lambda: data)[_n_(677391, "pathToValue", lambda: pathToValue)] = _n_(677392, "updatedValue", lambda: updatedValue)
    _l_(677393)

    _c_(677396, _a_(677395, _n_(677394, "f", lambda: f), "close"))
    _l_(677397)
    with _c_(677399, _n_(677398, "open", lambda: open), "template3.json", "w") as outfile:
        _l_(677406)

        _c_(677404, _a_(677401, _n_(677400, "json", lambda: json), "dump"), _n_(677402, "data", lambda: data), _n_(677403, "outfile", lambda: outfile))
        _l_(677405)
   
x = ['Something 1'][0]['ID']
_l_(677408)

_c_(677411, _n_(677409, "updateJson", lambda: updateJson), "Temp\\random.json", _n_(677410, "x", lambda: x), 9) 
_l_(677412) 