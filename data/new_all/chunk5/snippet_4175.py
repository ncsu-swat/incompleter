# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62016881/python-flask-sqlalchemy-attributeerror-table-object-has-no-attribute-added
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from TasMar import db,create_app
    _l_(656740)

except ImportError:
    pass
try:
    from TasMar.models import User,Tasks,tm_status, tm_urgency,tm_type
    _l_(656742)

except ImportError:
    pass
app=_c_(656744, _n_(656743, "create_app", lambda: create_app))
_l_(656745)
_c_(656750, _a_(656749, _c_(656748, _a_(656747, _n_(656746, "app", lambda: app), "app_context")), "push"))
_l_(656751)
#db.create_all()   #<<works perfectly but not below !
user = _c_(656757, _a_(656756, _c_(656755, _a_(656754, _a_(656753, _n_(656752, "User", lambda: User), "query"), "filter_by"), email='dummy@email.com'), "first"))
_l_(656758)
_c_(656761, _n_(656759, "print", lambda: print), _n_(656760, "user", lambda: user))
_l_(656762)