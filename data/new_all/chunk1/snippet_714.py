# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50183951/raspberry-pi-python-spi-open-error-filenotfounderror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import spidev
    _l_(406137)

except ImportError:
    pass
try:
    from time import sleep
    _l_(406139)

except ImportError:
    pass
spi = _c_(406142, _a_(406141, _n_(406140, "spidev", lambda: spidev), "SpiDev"))
_l_(406143)
_c_(406146, _a_(406145, _n_(406144, "spi", lambda: spi), "open"), 1,0)
_l_(406147)