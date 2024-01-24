# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72999836/micropython-application-throws-attributeerror-for-very-basic-use-of-re-split-wit
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from machine import Pin, SPI, UART
    _l_(538763)

except ImportError:
    pass
try:
    from array import array
    _l_(538765)

except ImportError:
    pass
try:
    import sys, re, time, math, framebuf
    _l_(538767)

except ImportError:
    pass

_c_(538771, _a_(538770, _a_(538769, _n_(538768, "sys", lambda: sys), "path"), "append"), "C:/Source/Pico/SSD1322_SPI_4W")
_l_(538772)
_c_(538776, _n_(538773, "print", lambda: print), _a_(538775, _n_(538774, "sys", lambda: sys), "path"))
_l_(538777)
try:
    import ssd1322
    _l_(538779)

except ImportError:
    pass

_c_(538781, _n_(538780, "print", lambda: print), "Test print")
_l_(538782)
s1="123\t123\t123"
_l_(538783)
s2 = _c_(538787, _a_(538785, _n_(538784, "re", lambda: re), "split"), r'\t', _n_(538786, "s1", lambda: s1))
_l_(538788)
_c_(538791, _n_(538789, "print", lambda: print), _n_(538790, "s2", lambda: s2))
_l_(538792)