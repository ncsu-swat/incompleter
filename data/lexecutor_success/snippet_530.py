# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/969285/how-do-i-translate-an-iso-8601-datetime-string-into-a-python-datetime-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime, time
    _l_(1538744)

except ImportError:
    pass
def convert_enddate_to_seconds(self, ts):
    _l_(1538774)

    """Takes ISO 8601 format(string) and converts into epoch time."""
    dt = _c_(1538749, _a_(1538747, _a_(1538746, _n_(1538745, "datetime", lambda: datetime), "datetime"), "strptime"), _n_(1538748, "ts", lambda: ts)[:-7],'%Y-%m-%dT%H:%M:%S.%f')+\
                _c_(1538758, _a_(1538751, _n_(1538750, "datetime", lambda: datetime), "timedelta"), hours=_c_(1538754, _n_(1538752, "int", lambda: int), _n_(1538753, "ts", lambda: ts)[-5:-3]),
                minutes=_c_(1538757, _n_(1538755, "int", lambda: int), _n_(1538756, "ts", lambda: ts)[-2:]))*_c_(1538761, _n_(1538759, "int", lambda: int), _n_(1538760, "ts", lambda: ts)[-6:-5]+'1')
    _l_(1538762)
    seconds = _c_(1538768, _a_(1538764, _n_(1538763, "time", lambda: time), "mktime"), _c_(1538767, _a_(1538766, _n_(1538765, "dt", lambda: dt), "timetuple"))) + _a_(1538770, _n_(1538769, "dt", lambda: dt), "microsecond")/1000000.0
    _l_(1538771)
    aux = _n_(1538772, "seconds", lambda: seconds)
    _l_(1538773)
    return aux
try:
    import datetime, time
    _l_(1538776)

except ImportError:
    pass
ts = '2012-09-30T15:31:50.262-08:00'
_l_(1538777)
dt = _c_(1538782, _a_(1538780, _a_(1538779, _n_(1538778, "datetime", lambda: datetime), "datetime"), "strptime"), _n_(1538781, "ts", lambda: ts)[:-7],'%Y-%m-%dT%H:%M:%S.%f')+ _c_(1538791, _a_(1538784, _n_(1538783, "datetime", lambda: datetime), "timedelta"), hours=_c_(1538787, _n_(1538785, "int", lambda: int), _n_(1538786, "ts", lambda: ts)[-5:-3]), minutes=_c_(1538790, _n_(1538788, "int", lambda: int), _n_(1538789, "ts", lambda: ts)[-2:]))*_c_(1538794, _n_(1538792, "int", lambda: int), _n_(1538793, "ts", lambda: ts)[-6:-5]+'1')
_l_(1538795)
seconds = _c_(1538801, _a_(1538797, _n_(1538796, "time", lambda: time), "mktime"), _c_(1538800, _a_(1538799, _n_(1538798, "dt", lambda: dt), "timetuple"))) + _a_(1538803, _n_(1538802, "dt", lambda: dt), "microsecond")/1000000.0
_l_(1538804)
_n_(1538805, "seconds", lambda: seconds)
_l_(1538806)
1348990310.26
_l_(1538807)

