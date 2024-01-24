# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58958394/typeerror-a-bytes-like-object-is-required-not-str-with-a-mouse-emulation
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
report = '\x00\x81\x81\x00'
_l_(446770)
with _c_(446772, _n_(446771, "open", lambda: open), '/dev/hidg1', 'rb+') as fd:
    _l_(446778)

    _c_(446776, _a_(446774, _n_(446773, "fd", lambda: fd), "write"), _n_(446775, "report", lambda: report))
    _l_(446777)