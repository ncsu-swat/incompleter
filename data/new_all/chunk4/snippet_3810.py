# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67410273/typeerror-unicode-strings-are-not-supported-please-encode-to-bytes-t-x10-x0
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import serial
    _l_(642801)

except ImportError:
    pass
try:
    import time
    _l_(642803)

except ImportError:
    pass
try:
    import binascii
    _l_(642805)

except ImportError:
    pass

ser = _c_(642814, _a_(642807, _n_(642806, "serial", lambda: serial), "Serial"), port='COM8',baudrate=9600,timeout=1,parity=_a_(642809, _n_(642808, "serial", lambda: serial), "PARITY_NONE"),stopbits=_a_(642811, _n_(642810, "serial", lambda: serial), "STOPBITS_ONE"),bytesize=_a_(642813, _n_(642812, "serial", lambda: serial), "EIGHTBITS"))
_l_(642815)

counter = 0
_l_(642816)

while _n_(642817, "counter", lambda: counter) < 1:
    _l_(642845)


    counter = _n_(642818, "counter", lambda: counter) + 1
    _l_(642819)

    _c_(642822, _a_(642821, _n_(642820, "ser", lambda: ser), "write"), "\x09\x10\x03\xE8\x00\x03\x06\x00\x00\x00\x00\x00\x00\x73\x30")
    _l_(642823)

    data_raw = _c_(642826, _a_(642825, _n_(642824, "ser", lambda: ser), "readline"))
    _l_(642827)

    _c_(642830, _n_(642828, "print", lambda: print), _n_(642829, "data_raw", lambda: data_raw))
    _l_(642831)

    data = _c_(642835, _a_(642833, _n_(642832, "binascii", lambda: binascii), "hexlify"), _n_(642834, "data_raw", lambda: data_raw))
    _l_(642836)

    _c_(642839, _n_(642837, "print", lambda: print), "Response 1 ", _n_(642838, "data", lambda: data))
    _l_(642840)

    _c_(642843, _a_(642842, _n_(642841, "time", lambda: time), "sleep"), 0.01)
    _l_(642844)

 

_c_(642848, _a_(642847, _n_(642846, "ser", lambda: ser), "write"), "\x09\x03\x07\xD0\x00\x01\x85\xCF")
_l_(642849)

data_raw = _c_(642852, _a_(642851, _n_(642850, "ser", lambda: ser), "readline"))
_l_(642853)

_c_(642856, _n_(642854, "print", lambda: print), _n_(642855, "data_raw", lambda: data_raw))
_l_(642857)

data = _c_(642861, _a_(642859, _n_(642858, "binascii", lambda: binascii), "hexlify"), _n_(642860, "data_raw", lambda: data_raw))
_l_(642862)

_c_(642865, _n_(642863, "print", lambda: print), "Response 2 ", _n_(642864, "data", lambda: data))
_l_(642866)

_c_(642869, _a_(642868, _n_(642867, "time", lambda: time), "sleep"), 1)
_l_(642870)

 

while(True):
    _l_(642899)


    _c_(642872, _n_(642871, "print", lambda: print), "Close gripper")
    _l_(642873)

    _c_(642876, _a_(642875, _n_(642874, "ser", lambda: ser), "write"), "\x09\x10\x03\xE8\x00\x03\x06\x09\x00\x00\xFF\xFF\xFF\x42\x29")
    _l_(642877)

    data_raw = _c_(642880, _a_(642879, _n_(642878, "ser", lambda: ser), "readline"))
    _l_(642881)

    _c_(642884, _n_(642882, "print", lambda: print), _n_(642883, "data_raw", lambda: data_raw))
    _l_(642885)

    data = _c_(642889, _a_(642887, _n_(642886, "binascii", lambda: binascii), "hexlify"), _n_(642888, "data_raw", lambda: data_raw))
    _l_(642890)

    _c_(642893, _n_(642891, "print", lambda: print), "Response 3 ", _n_(642892, "data", lambda: data))
    _l_(642894)

    _c_(642897, _a_(642896, _n_(642895, "time", lambda: time), "sleep"), 2)
    _l_(642898)

 

_c_(642901, _n_(642900, "print", lambda: print), "Open gripper")
_l_(642902)

_c_(642905, _a_(642904, _n_(642903, "ser", lambda: ser), "write"), "\x09\x10\x03\xE8\x00\x03\x06\x09\x00\x00\x00\xFF\xFF\x72\x19")
_l_(642906)

data_raw = _c_(642909, _a_(642908, _n_(642907, "ser", lambda: ser), "readline"))
_l_(642910)

_c_(642913, _n_(642911, "print", lambda: print), _n_(642912, "data_raw", lambda: data_raw))
_l_(642914)

data = _c_(642918, _a_(642916, _n_(642915, "binascii", lambda: binascii), "hexlify"), _n_(642917, "data_raw", lambda: data_raw))
_l_(642919)

_c_(642922, _n_(642920, "print", lambda: print), "Response 4 ", _n_(642921, "data", lambda: data))
_l_(642923)

_c_(642926, _a_(642925, _n_(642924, "time", lambda: time), "sleep"), 2)
_l_(642927)