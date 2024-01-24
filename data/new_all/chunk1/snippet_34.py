# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/35642855/python3-pyserial-typeerror-unicode-strings-are-not-supported-please-encode-to
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import serial, time
    _l_(378025)

except ImportError:
    pass
try:
    import tkinter
    _l_(378027)

except ImportError:
    pass
try:
    import os
    _l_(378029)

except ImportError:
    pass

def serialcmdw():
    _l_(378042)

    _c_(378032, _a_(378031, _n_(378030, "os", lambda: os), "system"), 'clear')
    _l_(378033)
    serialcmd = _c_(378035, _n_(378034, "input", lambda: input), "serial command: ")
    _l_(378036)
    _c_(378040, _a_(378038, _n_(378037, "ser", lambda: ser), "write"), _n_(378039, "serialcmd", lambda: serialcmd))
    _l_(378041)

_c_(378044, _n_(378043, "serialcmdw", lambda: serialcmdw))
_l_(378045)

ser = _c_(378048, _a_(378047, _n_(378046, "serial", lambda: serial), "Serial"))
_l_(378049)
_c_(378052, _a_(378051, _n_(378050, "os", lambda: os), "system"), 'clear')
_l_(378053)
_n_(378054, "ser", lambda: ser).port = "/dev/cu.usbmodem4321"
_l_(378055)
_n_(378056, "ser", lambda: ser).baudrate = 9600
_l_(378057)
_c_(378060, _a_(378059, _n_(378058, "ser", lambda: ser), "open"))
_l_(378061)
_c_(378064, _a_(378063, _n_(378062, "time", lambda: time), "sleep"), 1)
_l_(378065)
_c_(378067, _n_(378066, "serialcmdw", lambda: serialcmdw))
_l_(378068)