# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38643554/weird-typeerror-when-using-the-datetime-time-module
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(660615)

except ImportError:
    pass
try:
    import datetime as dt
    _l_(660617)

except ImportError:
    pass
try:
    from time import sleep
    _l_(660619)

except ImportError:
    pass


def  connect():
    _l_(660627)

    _c_(660621, _n_(660620, "print", lambda: print), "Connecting...")
    _l_(660622)
    _c_(660625, _a_(660624, _n_(660623, "os", lambda: os), "system"), "netsh wlan connect Sushi")
    _l_(660626)

def disconnect():
    _l_(660635)

    _c_(660629, _n_(660628, "print", lambda: print), "Disconnecting...")
    _l_(660630)
    _c_(660633, _a_(660632, _n_(660631, "os", lambda: os), "system"), "netsh wlan disconnect")
    _l_(660634)

def checkcon():
    _l_(660664)

    attempt= 0
    _l_(660636)
    while _c_(660639, _a_(660638, _n_(660637, "os", lambda: os), "system"), "ping google.com") != 0:
        _l_(660660)

        _c_(660641, _n_(660640, "print", lambda: print), "Unable to connect. Trying again.")
        _l_(660642)
        _c_(660644, _n_(660643, "connect", lambda: connect))
        _l_(660645)
        _c_(660648, _n_(660646, "sleep", lambda: sleep), _n_(660647, "attempt", lambda: attempt))
        _l_(660649)
        attempt = _n_(660650, "attempt", lambda: attempt) + 1
        _l_(660651)
        if _n_(660652, "attempt", lambda: attempt) != 0:
            _l_(660659)

            _c_(660657, _n_(660653, "print", lambda: print), "Attempt ", _c_(660656, _n_(660654, "str", lambda: str), _n_(660655, "attempt", lambda: attempt)), " ...")
            _l_(660658)
    _c_(660662, _n_(660661, "print", lambda: print), "Connected successfully")
    _l_(660663)


def timeformat (hr, min, sec) :
    _l_(660675)

    aux = (_c_(660667, _n_(660665, "str", lambda: str), _n_(660666, "hr", lambda: hr)) + ":" + _c_(660670, _n_(660668, "str", lambda: str), _n_(660669, "min", lambda: min)) + ":" + _c_(660673, _n_(660671, "str", lambda: str), _n_(660672, "sec", lambda: sec)))
    _l_(660674)
    return aux

FMT = '%H:%M:%S'
_l_(660676)
now = _c_(660699, _n_(660677, "timeformat", lambda: timeformat), _a_(660684, _c_(660683, _a_(660682, _c_(660681, _a_(660680, _a_(660679, _n_(660678, "dt", lambda: dt), "datetime"), "now")), "time")), "hour"), _a_(660691, _c_(660690, _a_(660689, _c_(660688, _a_(660687, _a_(660686, _n_(660685, "dt", lambda: dt), "datetime"), "now")), "time")), "minute"), _a_(660698, _c_(660697, _a_(660696, _c_(660695, _a_(660694, _a_(660693, _n_(660692, "dt", lambda: dt), "datetime"), "now")), "time")), "second"))
_l_(660700)
twoam = '02:00:00'
_l_(660701)
eightam = '08:00:00'
_l_(660702)

def tdelta(a, b = _n_(660703, "now", lambda: now)):
    _l_(660720)

    tdel = _c_(660709, _a_(660706, _a_(660705, _n_(660704, "dt", lambda: dt), "datetime"), "strptime"), _n_(660707, "a", lambda: a), _n_(660708, "FMT", lambda: FMT)) - _c_(660715, _a_(660712, _a_(660711, _n_(660710, "dt", lambda: dt), "datetime"), "strptime"), _n_(660713, "b", lambda: b), _n_(660714, "FMT", lambda: FMT))
    _l_(660716)
    aux = _a_(660718, _n_(660717, "tdel", lambda: tdel), "seconds")
    _l_(660719)
    return aux

twoto8 = _c_(660724, _n_(660721, "tdelta", lambda: tdelta), _n_(660722, "eightam", lambda: eightam), _n_(660723, "twoam", lambda: twoam))
_l_(660725)
nowto8 = _c_(660728, _n_(660726, "tdelta", lambda: tdelta), _n_(660727, "eightam", lambda: eightam))
_l_(660729)

def main():
    _l_(660778)

    if  _n_(660730, "twoto8", lambda: twoto8) >= _n_(660731, "nowto8", lambda: nowto8):
        _l_(660777)

        _c_(660733, _n_(660732, "connect", lambda: connect))
        _l_(660734)
        _c_(660736, _n_(660735, "checkcon", lambda: checkcon))
        _l_(660737)
        _c_(660739, _n_(660738, "print", lambda: print), "Your internet has been successfully connected")
        _l_(660740)
        x = _c_(660743, _n_(660741, "tdelta", lambda: tdelta), _n_(660742, "nowto8", lambda: nowto8))
        _l_(660744)
        _c_(660747, _n_(660745, "sleep", lambda: sleep), _n_(660746, "x", lambda: x))
        _l_(660748)
        _c_(660750, _n_(660749, "print", lambda: print), "Time's up!")
        _l_(660751)
        _c_(660753, _n_(660752, "disconnect", lambda: disconnect))
        _l_(660754)
        aux = ""
        _l_(660757)
        exit(aux)
    else:
            _c_(660759, _n_(660758, "print", lambda: print), "Not yet!")
            _l_(660760)
            _c_(660762, _n_(660761, "disconnect", lambda: disconnect))
            _l_(660763)
            x = _c_(660766, _n_(660764, "tdelta", lambda: tdelta), _n_(660765, "nowto8", lambda: nowto8))
            _l_(660767)
            _c_(660772, _n_(660768, "sleep", lambda: sleep), _c_(660771, _n_(660769, "str", lambda: str), _n_(660770, "x", lambda: x)))
            _l_(660773)
            _c_(660775, _n_(660774, "main", lambda: main))
            _l_(660776)

_c_(660780, _n_(660779, "main", lambda: main))
_l_(660781)