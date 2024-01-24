# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/28926281/filenotfounderror-winerror-2-the-system-cannot-find-the-file-specified
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(689044)

except ImportError:
    pass
try:
    import os
    _l_(689046)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(689048)

except ImportError:
    pass
current_time = _c_(689053, _n_(689049, "str", lambda: str), _c_(689052, _a_(689051, _n_(689050, "datetime", lambda: datetime), "now")))
_l_(689054)
current_time = _c_(689057, _a_(689056, _n_(689055, "time", lambda: time), "strftime"), '%Y-%m-%d %H-%M')
_l_(689058)
_c_(689061, _n_(689059, "print", lambda: print), _n_(689060, "current_time", lambda: current_time))
_l_(689062)

OUTPUT_FILE = _c_(689065, _a_(689063, "{}.txt", "format"), _n_(689064, "current_time", lambda: current_time))
_l_(689066)

NEW_DIRS =[]
_l_(689067)

while 1:
    _l_(689153)

#Acquires list of dirs and the creation date attribute associated to them 
    for dir in _c_(689070, _a_(689069, _n_(689068, "os", lambda: os), "listdir"), "S:\\"):
        _l_(689152)

        dir = _c_(689075, _a_(689073, _a_(689072, _n_(689071, "os", lambda: os), "path"), "join"), "S:\\", _n_(689074, "dir", lambda: dir))
        _l_(689076)
        if _c_(689081, _a_(689079, _a_(689078, _n_(689077, "os", lambda: os), "path"), "isdir"), _n_(689080, "dir", lambda: dir)):
            _l_(689151)


            try:
                _l_(689106)

                seconds = _c_(689086, _a_(689084, _a_(689083, _n_(689082, "os", lambda: os), "path"), "getctime"), _n_(689085, "dir", lambda: dir))
                _l_(689087)
                datecreated = _c_(689094, _a_(689089, _n_(689088, "time", lambda: time), "strftime"), '%Y-%m-%d %H:%M', _c_(689093, _a_(689091, _n_(689090, "time", lambda: time), "localtime"), _n_(689092, "seconds", lambda: seconds)))
                _l_(689095)


            except (_n_(689096, "FileNotFoundError", lambda: FileNotFoundError), _n_(689097, "IOError", lambda: IOError),_n_(689098, "AttributeError", lambda: AttributeError)):
                _l_(689105)

                _c_(689103, _a_(689101, _c_(689100, _n_(689099, "print", lambda: print), "{} Missing!"), "format"), _n_(689102, "dir", lambda: dir))
                _l_(689104)


            close_time = "23-59"
            _l_(689107)

            DATE_TIME = _c_(689112, _n_(689108, "str", lambda: str), _c_(689111, _a_(689110, _n_(689109, "datetime", lambda: datetime), "now")))
            _l_(689113)
            DATE_TIME = _c_(689116, _a_(689115, _n_(689114, "time", lambda: time), "strftime"), '%H-%M')
            _l_(689117)

            if _n_(689118, "DATE_TIME", lambda: DATE_TIME) == _n_(689119, "close_time", lambda: close_time):
                _l_(689150)

                _c_(689121, _n_(689120, "quit", lambda: quit))
                _l_(689122)

            elif _n_(689123, "dir", lambda: dir) not in _n_(689124, "NEW_DIRS", lambda: NEW_DIRS) and _n_(689125, "datecreated", lambda: datecreated) > _n_(689126, "current_time", lambda: current_time):
                _l_(689149)

                with _c_(689129, _n_(689127, "open", lambda: open), _n_(689128, "OUTPUT_FILE", lambda: OUTPUT_FILE),"a") as c:
                    _l_(689148)

                    _c_(689135, _a_(689131, _n_(689130, "c", lambda: c), "write"), _c_(689134, _a_(689132, "{}\n", "format"), _n_(689133, "dir", lambda: dir)))
                    _l_(689136)
                    _c_(689140, _a_(689138, _n_(689137, "NEW_DIRS", lambda: NEW_DIRS), "append"), _n_(689139, "dir", lambda: dir))
                    _l_(689141)
                    _c_(689146, _n_(689142, "print", lambda: print), _c_(689145, _a_(689143, "{} added to array", "format"), _n_(689144, "dir", lambda: dir)))
                    _l_(689147)