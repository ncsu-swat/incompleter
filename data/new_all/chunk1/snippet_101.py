# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/30032078/typeerror-init-takes-1-positional-argument-but-3-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from app import db
    _l_(411096)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(411098)

except ImportError:
    pass


class Post(_a_(411100, _n_(411099, "db", lambda: db), "Model")):
    _l_(411145)

    post_id = _c_(411105, _a_(411102, _n_(411101, "db", lambda: db), "Column"), _a_(411104, _n_(411103, "db", lambda: db), "Integer"), primary_key=True)
    _l_(411106)
    title = _c_(411112, _a_(411108, _n_(411107, "db", lambda: db), "Column"), _c_(411111, _a_(411110, _n_(411109, "db", lambda: db), "String"), 100))
    _l_(411113)
    text = _c_(411119, _a_(411115, _n_(411114, "db", lambda: db), "Column"), _c_(411118, _a_(411117, _n_(411116, "db", lambda: db), "Text")))
    _l_(411120)
    created_time = _c_(411126, _a_(411122, _n_(411121, "db", lambda: db), "Column"), _c_(411125, _a_(411124, _n_(411123, "db", lambda: db), "DateTime")))
    _l_(411127)

    def __init__(self, title, text, created_time=None):
        _l_(411144)

        _n_(411128, "self", lambda: self).title = _n_(411129, "title", lambda: title)
        _l_(411130)
        _n_(411131, "self", lambda: self).text = _n_(411132, "text", lambda: text)
        _l_(411133)
        if _n_(411134, "created_time", lambda: created_time) is None:
            _l_(411143)

            _n_(411135, "self", lambda: self).created_time = _c_(411138, _a_(411137, _n_(411136, "datetime", lambda: datetime), "utcnow"))
            _l_(411139)
        else:
            _n_(411140, "self", lambda: self).created_time = _n_(411141, "created_time", lambda: created_time)
            _l_(411142)