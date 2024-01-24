# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48939168/python-error-typeerror-expected-string-or-buffer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
half_hour_date = '23/02/2018 23:00PM'
_l_(524461)
epg_time_1 = _c_(524465, _a_(524463, _n_(524462, "time", lambda: time), "strptime"), _n_(524464, "half_hour_date", lambda: half_hour_date), '%d/%m/%Y %I:%M%p')
_l_(524466)

#convert from time_struct_time object to datetime
date_format = _c_(524474, _a_(524469, _a_(524468, _n_(524467, "datetime", lambda: datetime), "datetime"), "fromtimestamp"), _c_(524473, _a_(524471, _n_(524470, "time", lambda: time), "mktime"), _n_(524472, "epg_time_1", lambda: epg_time_1)))
_l_(524475)
half_hour = _n_(524476, "date_format", lambda: date_format) + _c_(524481, _a_(524478, _n_(524477, "datetime", lambda: datetime), "timedelta"), days = _a_(524480, _n_(524479, "self", lambda: self), "program_day"))
_l_(524482)

#convert from datetime to time_struct_time object
epg_time_1 = _c_(524486, _a_(524484, _n_(524483, "time", lambda: time), "strptime"), _n_(524485, "half_hour", lambda: half_hour), '%d/%m/%Y %I:%M%p')
_l_(524487)