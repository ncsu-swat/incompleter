# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/16353858/type-error-occurred-using-buffer-memoryview
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import serial
    _l_(609634)

except ImportError:
    pass

ser = _c_(609643, _a_(609636, _n_(609635, "serial", lambda: serial), "Serial"), port='COM5',\
    baudrate=9600,\
    parity=_a_(609638, _n_(609637, "serial", lambda: serial), "PARITY_NONE"),\
    stopbits=_a_(609640, _n_(609639, "serial", lambda: serial), "STOPBITS_ONE"),\
    bytesize=_a_(609642, _n_(609641, "serial", lambda: serial), "EIGHTBITS"),\
        timeout=0)
_l_(609644)

MAX_BUF_SIZE = 16
_l_(609645)
bits = 0
_l_(609646)

v = _n_(609647, "memoryview", lambda: memoryview)
_l_(609648)



_c_(609652, _n_(609649, "print", lambda: print), "connected to: " + _a_(609651, _n_(609650, "ser", lambda: ser), "portstr"))
_l_(609653)



while(1):
    _l_(609669)

    for memoryview in _c_(609656, _a_(609655, _n_(609654, "ser", lambda: ser), "read")):
        _l_(609668)

        if _n_(609657, "v", lambda: v)[0] == 42:
            _l_(609667)


            if _n_(609658, "v", lambda: v)[-1] == 35:
                _l_(609665)


                _c_(609663, _n_(609659, "print", lambda: print), _c_(609662, _a_(609661, _n_(609660, "v", lambda: v)[1:-1], "tobytes")))
                _l_(609664)

        else:
            memoryview = 0
            _l_(609666)
_c_(609672, _a_(609671, _n_(609670, "ser", lambda: ser), "close"))
_l_(609673)