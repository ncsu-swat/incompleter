# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65948454/attributeerror-owm-object-has-no-attribute-weather-at-coords
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from python.owm import OWM
    _l_(639937)

except ImportError:
    pass
owm = _c_(639939, _n_(639938, "OWM", lambda: OWM), 'API KEY')
_l_(639940)
mgr = _c_(639943, _a_(639942, _n_(639941, "owm", lambda: owm), "weather_manager"))
_l_(639944)
lat = 0
_l_(639945)
lon = 0
_l_(639946)
current_weather = _a_(639952, _c_(639951, _a_(639948, _n_(639947, "owm", lambda: owm), "weather_at_coords"), _n_(639949, "lat", lambda: lat), _n_(639950, "lon", lambda: lon)), "weather")
_l_(639953)
_c_(639956, _n_(639954, "print", lambda: print), _n_(639955, "current_weather", lambda: current_weather))
_l_(639957)