# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57395187/python-string-concatenation-typeerror-bad-operand-type-for-unary-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
weather = _c_(436927, _n_(436924, "forecast", lambda: forecast), 'api_key',_n_(436925, "lat", lambda: lat), -_n_(436926, "long", lambda: long))
_l_(436928)
windbearing = _a_(436930, _n_(436929, "weather", lambda: weather), "windBearing")
_l_(436931)
windspeed = _c_(436935, _n_(436932, "float", lambda: float), _a_(436934, _n_(436933, "weather", lambda: weather), "windSpeed"))
_l_(436936)

def windcompass(windbearing):
    _l_(436945)

    val = _c_(436939, _n_(436937, "int", lambda: int), (_n_(436938, "windbearing", lambda: windbearing)/22.5)+.5)
    _l_(436940)
    argument = ["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    _l_(436941)
    aux = _n_(436942, "argument", lambda: argument)[(_n_(436943, "val", lambda: val) % 16)]
    _l_(436944)
    return aux

direction = _c_(436948, _n_(436946, "windcompass", lambda: windcompass), _n_(436947, "windbearing", lambda: windbearing))
_l_(436949)

_c_(436953, _n_(436950, "print", lambda: print), 'The wind is blowing ', + _n_(436951, "windspeed", lambda: windspeed), + 'at ', + _n_(436952, "direction", lambda: direction), + 'MPH')
_l_(436954)