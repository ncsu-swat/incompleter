# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72036511/attribute-error-module-uctypes-has-no-attribute-int32
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from machine import UART
    _l_(630855)

except ImportError:
    pass
try:
    import time
    _l_(630857)

except ImportError:
    pass
buffer=_c_(630859, _n_(630858, "bytearray", lambda: bytearray), 31) 
_l_(630860) 
uart = _c_(630862, _n_(630861, "UART", lambda: UART), 1, 115200) # uart1 tx-pin 4, rx-pin 5
_l_(630863) # uart1 tx-pin 4, rx-pin 5
while True:
    _l_(630912)

    c=_c_(630866, _a_(630865, _n_(630864, "uart", lambda: uart), "read"), 1)
    _l_(630867)
    if _n_(630868, "c", lambda: c)[0] == 0x20:
        _l_(630911)

        _c_(630872, _a_(630870, _n_(630869, "uart", lambda: uart), "readinto"), _n_(630871, "buffer", lambda: buffer))
        _l_(630873)
        checksum = 0xffff - 0x20
        _l_(630874)
        for i in _c_(630876, _n_(630875, "range", lambda: range), 29):
            _l_(630879)

checksum -= _n_(630877, "buffer", lambda: buffer)[_n_(630878, "i", lambda: i)]        if _n_(630880, "checksum", lambda: checksum) == (_n_(630881, "buffer", lambda: buffer)[30] << 8) | _n_(630882, "buffer", lambda: buffer)[29]:
            _l_(630910)

            # skip buffer[0] = 0x40
            ch1 = _n_(630883, "buffer", lambda: buffer)[2]*255+_n_(630884, "buffer", lambda: buffer)[1]
            _l_(630885)
            ch2 = _n_(630886, "buffer", lambda: buffer)[4]*255+_n_(630887, "buffer", lambda: buffer)[3]
            _l_(630888)
            ch3 = _n_(630889, "buffer", lambda: buffer)[6]*255+_n_(630890, "buffer", lambda: buffer)[5]
            _l_(630891)
            ch4 = _n_(630892, "buffer", lambda: buffer)[8]*255+_n_(630893, "buffer", lambda: buffer)[7]
            _l_(630894)
            ch5 = _n_(630895, "buffer", lambda: buffer)[10]*255+_n_(630896, "buffer", lambda: buffer)[9]
            _l_(630897)
            ch6 = _n_(630898, "buffer", lambda: buffer)[12]*255+_n_(630899, "buffer", lambda: buffer)[11]
            _l_(630900)
            _c_(630908, _n_(630901, "print", lambda: print), 'ch  1-',_n_(630902, "ch1", lambda: ch1),'  2-',_n_(630903, "ch2", lambda: ch2),'  3-',_n_(630904, "ch3", lambda: ch3),'  4-',_n_(630905, "ch4", lambda: ch4),'  5-',_n_(630906, "ch5", lambda: ch5),'   6-',_n_(630907, "ch6", lambda: ch6))
            _l_(630909)