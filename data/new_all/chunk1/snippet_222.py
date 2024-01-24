# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53686612/rpi3b-bme280-attributeerror-module-object-has-no-attribute-load-calibration
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import smbus2
    _l_(410763)

except ImportError:
    pass
try:
    import bme280
    _l_(410765)

except ImportError:
    pass

port = 1
_l_(410766)
address = 0x76
_l_(410767)
bus = _c_(410771, _a_(410769, _n_(410768, "smbus2", lambda: smbus2), "SMBus"), _n_(410770, "port", lambda: port))
_l_(410772)

calibration_params = _c_(410777, _a_(410774, _n_(410773, "bme280", lambda: bme280), "load_calibration_params"), _n_(410775, "bus", lambda: bus), _n_(410776, "address", lambda: address))
_l_(410778)

# the sample method will take a single reading and return a
# compensated_reading object
data = _c_(410784, _a_(410780, _n_(410779, "bme280", lambda: bme280), "sample"), _n_(410781, "bus", lambda: bus), _n_(410782, "address", lambda: address), _n_(410783, "calibration_params", lambda: calibration_params))
_l_(410785)

# the compensated_reading class has the following attributes
_c_(410789, _n_(410786, "print", lambda: print), _a_(410788, _n_(410787, "data", lambda: data), "id"))
_l_(410790)
_c_(410794, _n_(410791, "print", lambda: print), _a_(410793, _n_(410792, "data", lambda: data), "timestamp"))
_l_(410795)
_c_(410799, _n_(410796, "print", lambda: print), _a_(410798, _n_(410797, "data", lambda: data), "temperature"))
_l_(410800)
_c_(410804, _n_(410801, "print", lambda: print), _a_(410803, _n_(410802, "data", lambda: data), "pressure"))
_l_(410805)
_c_(410809, _n_(410806, "print", lambda: print), _a_(410808, _n_(410807, "data", lambda: data), "humidity"))
_l_(410810)

# there is a handy string representation too
_c_(410813, _n_(410811, "print", lambda: print), _n_(410812, "data", lambda: data))
_l_(410814)