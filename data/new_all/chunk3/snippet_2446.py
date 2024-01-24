# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/33251130/python-3-import-typeerror-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from myproject.app import app
    _l_(534783)

except ImportError:
    pass
try:
    from myproject.app import db
    _l_(534785)

except ImportError:
    pass

def create_tables():
    _l_(534794)

    try:
        from myproject.models.util import Weekday, weekday_type
        _l_(534787)

    except ImportError:
        pass
    try:
        from myproject.models.activity import Activity, activities_tags, Occurrence, Tag
        _l_(534789)

    except ImportError:
        pass

    _c_(534792, _a_(534791, _n_(534790, "db", lambda: db), "create_all"))
    _l_(534793)