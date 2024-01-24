# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72036511/attribute-error-module-uctypes-has-no-attribute-int32
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from machine import UART
    _l_(639565)

except ImportError:
    pass
try:
    import time
    _l_(639567)

except ImportError:
    pass
buffer=_c_(639569, _n_(639568, "bytearray", lambda: bytearray), 31) 
_l_(639570) 
uart = _c_(639572, _n_(639571, "UART", lambda: UART), 1, 115200) # uart1 tx-pin 4, rx-pin 5
_l_(639573) # uart1 tx-pin 4, rx-pin 5
while True:
    _l_(639622)

    c=_c_(639576, _a_(639575, _n_(639574, "uart", lambda: uart), "read"), 1)
    _l_(639577)
    if _n_(639578, "c", lambda: c)[0] == 0x20:
        _l_(639621)

        _c_(639582, _a_(639580, _n_(639579, "uart", lambda: uart), "readinto"), _n_(639581, "buffer", lambda: buffer))
        _l_(639583)
        checksum = 0xffff - 0x20
        _l_(639584)
        for i in _c_(639586, _n_(639585, "range", lambda: range), 29):
            _l_(639589)

checksum -= _n_(639587, "buffer", lambda: buffer)[_n_(639588, "i", lambda: i)]        if _n_(639590, "checksum", lambda: checksum) == (_n_(639591, "buffer", lambda: buffer)[30] << 8) | _n_(639592, "buffer", lambda: buffer)[29]:
            _l_(639620)

            # skip buffer[0] = 0x40
            ch1 = _n_(639593, "buffer", lambda: buffer)[2]*255+_n_(639594, "buffer", lambda: buffer)[1]
            _l_(639595)
            ch2 = _n_(639596, "buffer", lambda: buffer)[4]*255+_n_(639597, "buffer", lambda: buffer)[3]
            _l_(639598)
            ch3 = _n_(639599, "buffer", lambda: buffer)[6]*255+_n_(639600, "buffer", lambda: buffer)[5]
            _l_(639601)
            ch4 = _n_(639602, "buffer", lambda: buffer)[8]*255+_n_(639603, "buffer", lambda: buffer)[7]
            _l_(639604)
            ch5 = _n_(639605, "buffer", lambda: buffer)[10]*255+_n_(639606, "buffer", lambda: buffer)[9]
            _l_(639607)
            ch6 = _n_(639608, "buffer", lambda: buffer)[12]*255+_n_(639609, "buffer", lambda: buffer)[11]
            _l_(639610)
            _c_(639618, _n_(639611, "print", lambda: print), 'ch  1-',_n_(639612, "ch1", lambda: ch1),'  2-',_n_(639613, "ch2", lambda: ch2),'  3-',_n_(639614, "ch3", lambda: ch3),'  4-',_n_(639615, "ch4", lambda: ch4),'  5-',_n_(639616, "ch5", lambda: ch5),'   6-',_n_(639617, "ch6", lambda: ch6))
            _l_(639619)