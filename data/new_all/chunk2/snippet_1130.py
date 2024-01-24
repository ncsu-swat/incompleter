# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/36865799/alembic-sqlalchemy-postgres-nameerror-name-string-is-not-defined-trying-to
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sqlalchemy import Column, String, Integer, DateTime
    _l_(437857)

except ImportError:
    pass
try:
    from serve_spec.db_global import db
    _l_(437859)

except ImportError:
    pass
try:
    import datetime
    _l_(437861)

except ImportError:
    pass
try:
    from time import time
    _l_(437863)

except ImportError:
    pass
try:
    from sqlalchemy.dialects.postgresql import JSON
    _l_(437865)

except ImportError:
    pass
try:
    from sqlalchemy.dialects.postgresql import ARRAY
    _l_(437867)

except ImportError:
    pass

class Issues(_a_(437869, _n_(437868, "db", lambda: db), "Base")):
    _l_(437945)


    __tablename__ = 'issues'
    _l_(437870)

    id = _c_(437873, _n_(437871, "Column", lambda: Column), _n_(437872, "String", lambda: String), primary_key=True)
    _l_(437874)
    thread_id                   = _c_(437877, _n_(437875, "Column", lambda: Column), _n_(437876, "String", lambda: String), nullable=False)
    _l_(437878)
    created                     = _c_(437885, _n_(437879, "Column", lambda: Column), _c_(437881, _n_(437880, "DateTime", lambda: DateTime), timezone=False), nullable=False, default=_a_(437884, _a_(437883, _n_(437882, "datetime", lambda: datetime), "datetime"), "utcnow"))
    _l_(437886)
    created_timestamp           = _c_(437890, _n_(437887, "Column", lambda: Column), _n_(437888, "Integer", lambda: Integer), nullable=False, default=_n_(437889, "time", lambda: time))
    _l_(437891)
    created_by_user_name        = _c_(437894, _n_(437892, "Column", lambda: Column), _n_(437893, "String", lambda: String), nullable=False)
    _l_(437895)
    is_parent                   = _c_(437898, _n_(437896, "Column", lambda: Column), _n_(437897, "Integer", lambda: Integer), nullable=False)
    _l_(437899)
    parent_title                = _c_(437902, _n_(437900, "Column", lambda: Column), _n_(437901, "String", lambda: String))
    _l_(437903)
    subscribed                  = _c_(437908, _n_(437904, "Column", lambda: Column), _c_(437907, _n_(437905, "ARRAY", lambda: ARRAY), _n_(437906, "String", lambda: String)))
    _l_(437909)
    unsubscribed                = _c_(437914, _n_(437910, "Column", lambda: Column), _c_(437913, _n_(437911, "ARRAY", lambda: ARRAY), _n_(437912, "String", lambda: String)))
    _l_(437915)
    pending_notifications_web   = _c_(437920, _n_(437916, "Column", lambda: Column), _c_(437919, _n_(437917, "ARRAY", lambda: ARRAY), _n_(437918, "String", lambda: String)))
    _l_(437921)
    pending_notifications_email = _c_(437926, _n_(437922, "Column", lambda: Column), _c_(437925, _n_(437923, "ARRAY", lambda: ARRAY), _n_(437924, "String", lambda: String)))
    _l_(437927)
    markdown_text               = _c_(437930, _n_(437928, "Column", lambda: Column), _n_(437929, "String", lambda: String), nullable=False, )
    _l_(437931)
    kernel_id                   = _c_(437934, _n_(437932, "Column", lambda: Column), _n_(437933, "String", lambda: String), nullable=False)
    _l_(437935)
    state                       = _c_(437938, _n_(437936, "Column", lambda: Column), _n_(437937, "String", lambda: String), nullable=False, default='open')
    _l_(437939)
    labels                      = _c_(437943, _n_(437940, "Column", lambda: Column), _c_(437942, _n_(437941, "JSON", lambda: JSON)))
    _l_(437944)