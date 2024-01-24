# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72134050/python3-python-can-notifier-typeerror-nonetype-object-is-not-callables
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
        import os
        _l_(538691)

except ImportError:
        pass
try:
        import can
        _l_(538693)

except ImportError:
        pass

_c_(538696, _a_(538695, _n_(538694, "os", lambda: os), "system"), 'sudo ip link set can0 up type can bitrate 500000')
_l_(538697)

bus = _c_(538701, _a_(538700, _a_(538699, _n_(538698, "can", lambda: can), "interface"), "Bus"), channel = 'can0', bustype = 'socketcan')
_l_(538702)

def parseData(can):
        _l_(538706)

        SingleCanFrame = _a_(538704, _n_(538703, "can", lambda: can), "Message")
        _l_(538705)

notifier = _c_(538713, _a_(538708, _n_(538707, "can", lambda: can), "Notifier"), _n_(538709, "bus", lambda: bus),[_c_(538712, _n_(538710, "parseData", lambda: parseData), _n_(538711, "can", lambda: can))])
_l_(538714)

while(1):
        _l_(538716)

        continue
        _l_(538715)

_c_(538719, _a_(538718, _n_(538717, "os", lambda: os), "system"), 'sudo ifconfig can0 down')
_l_(538720)