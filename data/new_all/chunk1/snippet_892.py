# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51804916/struct-unpack-type-error-a-byte-like-object-is-required-not-str-unpack-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
list1 = [b'\x03\x00\x00\x00\xff\xff\xff\xff',
b'\x07\x00\x00\x00\x06\x00\x00\x00\xff\xff\xff\xff']
_l_(388647)

_c_(388655, _n_(388648, "print", lambda: print), _c_(388654, _a_(388650, _n_(388649, "struct", lambda: struct), "unpack"), '<s', _c_(388653, _n_(388651, "bytes", lambda: bytes), _n_(388652, "i", lambda: i))))
_l_(388656)