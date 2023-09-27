# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1345827/how-do-i-find-the-time-difference-between-two-datetime-objects-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import datetime
    _l_(1541795)

except ImportError:
    pass

datetimeFormat = '%Y/%m/%d %H:%M:%S.%f'    
_l_(1541796)    
time1 = '2016/03/16 10:01:28.585'
_l_(1541797)
time2 = '2016/03/16 09:56:28.067'  
_l_(1541798)  
time_dif = _c_(1541803, _a_(1541800, _n_(1541799, "datetime", lambda: datetime), "strptime"), _n_(1541801, "time1", lambda: time1), _n_(1541802, "datetimeFormat", lambda: datetimeFormat)) - _c_(1541808, _a_(1541805, _n_(1541804, "datetime", lambda: datetime), "strptime"), _n_(1541806, "time2", lambda: time2),_n_(1541807, "datetimeFormat", lambda: datetimeFormat))
_l_(1541809)
_c_(1541812, _n_(1541810, "print", lambda: print), _n_(1541811, "time_dif", lambda: time_dif))
_l_(1541813)

