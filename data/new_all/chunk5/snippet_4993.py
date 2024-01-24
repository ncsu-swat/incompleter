# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/28926281/filenotfounderror-winerror-2-the-system-cannot-find-the-file-specified
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(685205)

except ImportError:
    pass
try:
    import os
    _l_(685207)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(685209)

except ImportError:
    pass
current_time = _c_(685214, _n_(685210, "str", lambda: str), _c_(685213, _a_(685212, _n_(685211, "datetime", lambda: datetime), "now")))
_l_(685215)
current_time = _c_(685218, _a_(685217, _n_(685216, "time", lambda: time), "strftime"), '%Y-%m-%d %H-%M')
_l_(685219)
_c_(685222, _n_(685220, "print", lambda: print), _n_(685221, "current_time", lambda: current_time))
_l_(685223)

OUTPUT_FILE = _c_(685226, _a_(685224, "{}.txt", "format"), _n_(685225, "current_time", lambda: current_time))
_l_(685227)

NEW_DIRS =[]
_l_(685228)

while 1:
    _l_(685314)

#Acquires list of dirs and the creation date attribute associated to them 
    for dir in _c_(685231, _a_(685230, _n_(685229, "os", lambda: os), "listdir"), "S:\\"):
        _l_(685313)

        dir = _c_(685236, _a_(685234, _a_(685233, _n_(685232, "os", lambda: os), "path"), "join"), "S:\\", _n_(685235, "dir", lambda: dir))
        _l_(685237)
        if _c_(685242, _a_(685240, _a_(685239, _n_(685238, "os", lambda: os), "path"), "isdir"), _n_(685241, "dir", lambda: dir)):
            _l_(685312)


            try:
                _l_(685267)

                seconds = _c_(685247, _a_(685245, _a_(685244, _n_(685243, "os", lambda: os), "path"), "getctime"), _n_(685246, "dir", lambda: dir))
                _l_(685248)
                datecreated = _c_(685255, _a_(685250, _n_(685249, "time", lambda: time), "strftime"), '%Y-%m-%d %H:%M', _c_(685254, _a_(685252, _n_(685251, "time", lambda: time), "localtime"), _n_(685253, "seconds", lambda: seconds)))
                _l_(685256)


            except (_n_(685257, "FileNotFoundError", lambda: FileNotFoundError), _n_(685258, "IOError", lambda: IOError),_n_(685259, "AttributeError", lambda: AttributeError)):
                _l_(685266)

                _c_(685264, _a_(685262, _c_(685261, _n_(685260, "print", lambda: print), "{} Missing!"), "format"), _n_(685263, "dir", lambda: dir))
                _l_(685265)


            close_time = "23-59"
            _l_(685268)

            DATE_TIME = _c_(685273, _n_(685269, "str", lambda: str), _c_(685272, _a_(685271, _n_(685270, "datetime", lambda: datetime), "now")))
            _l_(685274)
            DATE_TIME = _c_(685277, _a_(685276, _n_(685275, "time", lambda: time), "strftime"), '%H-%M')
            _l_(685278)

            if _n_(685279, "DATE_TIME", lambda: DATE_TIME) == _n_(685280, "close_time", lambda: close_time):
                _l_(685311)

                _c_(685282, _n_(685281, "quit", lambda: quit))
                _l_(685283)

            elif _n_(685284, "dir", lambda: dir) not in _n_(685285, "NEW_DIRS", lambda: NEW_DIRS) and _n_(685286, "datecreated", lambda: datecreated) > _n_(685287, "current_time", lambda: current_time):
                _l_(685310)

                with _c_(685290, _n_(685288, "open", lambda: open), _n_(685289, "OUTPUT_FILE", lambda: OUTPUT_FILE),"a") as c:
                    _l_(685309)

                    _c_(685296, _a_(685292, _n_(685291, "c", lambda: c), "write"), _c_(685295, _a_(685293, "{}\n", "format"), _n_(685294, "dir", lambda: dir)))
                    _l_(685297)
                    _c_(685301, _a_(685299, _n_(685298, "NEW_DIRS", lambda: NEW_DIRS), "append"), _n_(685300, "dir", lambda: dir))
                    _l_(685302)
                    _c_(685307, _n_(685303, "print", lambda: print), _c_(685306, _a_(685304, "{} added to array", "format"), _n_(685305, "dir", lambda: dir)))
                    _l_(685308)