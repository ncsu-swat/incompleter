# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65540523/python-installation-issue-with-adalm-pluto-typeerror
# Import library
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import adi
    _l_(424772)

except ImportError:
    pass
# Create radio object
sdr = _c_(424775, _a_(424774, _n_(424773, "adi", lambda: adi), "Pluto"), uri="ip:192.168.2.1")
_l_(424776)
# Configure properties
_n_(424777, "sdr", lambda: sdr).rx_rf_bandwidth = 4000000
_l_(424778)
# Get data
data = _c_(424781, _a_(424780, _n_(424779, "sdr", lambda: sdr), "rx"))
_l_(424782)