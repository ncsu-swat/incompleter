# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38643554/weird-typeerror-when-using-the-datetime-time-module
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(666389)

except ImportError:
    pass
try:
    import datetime as dt
    _l_(666391)

except ImportError:
    pass
try:
    from time import sleep
    _l_(666393)

except ImportError:
    pass


def  connect():
    _l_(666401)

    _c_(666395, _n_(666394, "print", lambda: print), "Connecting...")
    _l_(666396)
    _c_(666399, _a_(666398, _n_(666397, "os", lambda: os), "system"), "netsh wlan connect Sushi")
    _l_(666400)

def disconnect():
    _l_(666409)

    _c_(666403, _n_(666402, "print", lambda: print), "Disconnecting...")
    _l_(666404)
    _c_(666407, _a_(666406, _n_(666405, "os", lambda: os), "system"), "netsh wlan disconnect")
    _l_(666408)

def checkcon():
    _l_(666438)

    attempt= 0
    _l_(666410)
    while _c_(666413, _a_(666412, _n_(666411, "os", lambda: os), "system"), "ping google.com") != 0:
        _l_(666434)

        _c_(666415, _n_(666414, "print", lambda: print), "Unable to connect. Trying again.")
        _l_(666416)
        _c_(666418, _n_(666417, "connect", lambda: connect))
        _l_(666419)
        _c_(666422, _n_(666420, "sleep", lambda: sleep), _n_(666421, "attempt", lambda: attempt))
        _l_(666423)
        attempt = _n_(666424, "attempt", lambda: attempt) + 1
        _l_(666425)
        if _n_(666426, "attempt", lambda: attempt) != 0:
            _l_(666433)

            _c_(666431, _n_(666427, "print", lambda: print), "Attempt ", _c_(666430, _n_(666428, "str", lambda: str), _n_(666429, "attempt", lambda: attempt)), " ...")
            _l_(666432)
    _c_(666436, _n_(666435, "print", lambda: print), "Connected successfully")
    _l_(666437)


def timeformat (hr, min, sec) :
    _l_(666449)

    aux = (_c_(666441, _n_(666439, "str", lambda: str), _n_(666440, "hr", lambda: hr)) + ":" + _c_(666444, _n_(666442, "str", lambda: str), _n_(666443, "min", lambda: min)) + ":" + _c_(666447, _n_(666445, "str", lambda: str), _n_(666446, "sec", lambda: sec)))
    _l_(666448)
    return aux

FMT = '%H:%M:%S'
_l_(666450)
now = _c_(666473, _n_(666451, "timeformat", lambda: timeformat), _a_(666458, _c_(666457, _a_(666456, _c_(666455, _a_(666454, _a_(666453, _n_(666452, "dt", lambda: dt), "datetime"), "now")), "time")), "hour"), _a_(666465, _c_(666464, _a_(666463, _c_(666462, _a_(666461, _a_(666460, _n_(666459, "dt", lambda: dt), "datetime"), "now")), "time")), "minute"), _a_(666472, _c_(666471, _a_(666470, _c_(666469, _a_(666468, _a_(666467, _n_(666466, "dt", lambda: dt), "datetime"), "now")), "time")), "second"))
_l_(666474)
twoam = '02:00:00'
_l_(666475)
eightam = '08:00:00'
_l_(666476)

def tdelta(a, b = _n_(666477, "now", lambda: now)):
    _l_(666494)

    tdel = _c_(666483, _a_(666480, _a_(666479, _n_(666478, "dt", lambda: dt), "datetime"), "strptime"), _n_(666481, "a", lambda: a), _n_(666482, "FMT", lambda: FMT)) - _c_(666489, _a_(666486, _a_(666485, _n_(666484, "dt", lambda: dt), "datetime"), "strptime"), _n_(666487, "b", lambda: b), _n_(666488, "FMT", lambda: FMT))
    _l_(666490)
    aux = _a_(666492, _n_(666491, "tdel", lambda: tdel), "seconds")
    _l_(666493)
    return aux

twoto8 = _c_(666498, _n_(666495, "tdelta", lambda: tdelta), _n_(666496, "eightam", lambda: eightam), _n_(666497, "twoam", lambda: twoam))
_l_(666499)
nowto8 = _c_(666502, _n_(666500, "tdelta", lambda: tdelta), _n_(666501, "eightam", lambda: eightam))
_l_(666503)

def main():
    _l_(666552)

    if  _n_(666504, "twoto8", lambda: twoto8) >= _n_(666505, "nowto8", lambda: nowto8):
        _l_(666551)

        _c_(666507, _n_(666506, "connect", lambda: connect))
        _l_(666508)
        _c_(666510, _n_(666509, "checkcon", lambda: checkcon))
        _l_(666511)
        _c_(666513, _n_(666512, "print", lambda: print), "Your internet has been successfully connected")
        _l_(666514)
        x = _c_(666517, _n_(666515, "tdelta", lambda: tdelta), _n_(666516, "nowto8", lambda: nowto8))
        _l_(666518)
        _c_(666521, _n_(666519, "sleep", lambda: sleep), _n_(666520, "x", lambda: x))
        _l_(666522)
        _c_(666524, _n_(666523, "print", lambda: print), "Time's up!")
        _l_(666525)
        _c_(666527, _n_(666526, "disconnect", lambda: disconnect))
        _l_(666528)
        aux = ""
        _l_(666531)
        exit(aux)
    else:
            _c_(666533, _n_(666532, "print", lambda: print), "Not yet!")
            _l_(666534)
            _c_(666536, _n_(666535, "disconnect", lambda: disconnect))
            _l_(666537)
            x = _c_(666540, _n_(666538, "tdelta", lambda: tdelta), _n_(666539, "nowto8", lambda: nowto8))
            _l_(666541)
            _c_(666546, _n_(666542, "sleep", lambda: sleep), _c_(666545, _n_(666543, "str", lambda: str), _n_(666544, "x", lambda: x)))
            _l_(666547)
            _c_(666549, _n_(666548, "main", lambda: main))
            _l_(666550)

_c_(666554, _n_(666553, "main", lambda: main))
_l_(666555)