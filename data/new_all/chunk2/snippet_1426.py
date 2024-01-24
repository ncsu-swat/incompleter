# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60108174/typeerror-only-takes-2-positional-arguments-but-3-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import *
    _l_(431960)

except ImportError:
    pass
try:
    from flask_cqlalchemy import CQLAlchemy
    _l_(431962)

except ImportError:
    pass

app = _c_(431965, _n_(431963, "Flask", lambda: Flask), _n_(431964, "__name__", lambda: __name__))
_l_(431966)
_a_(431968, _n_(431967, "app", lambda: app), "config")['CASSANDRA_HOSTS'] = ['127.0.0.1']
_l_(431969)
_a_(431971, _n_(431970, "app", lambda: app), "config")['CASSANDRA_KEYSPACE'] = "emp"
_l_(431972)

db = _c_(431975, _n_(431973, "CQLAlchemy", lambda: CQLAlchemy), _n_(431974, "app", lambda: app))
_l_(431976)

class Student(_a_(431978, _n_(431977, "db", lambda: db), "Model")):
    _l_(432027)

    uid = _c_(431982, _a_(431981, _a_(431980, _n_(431979, "db", lambda: db), "columns"), "Integer"), primary_key=True)
    _l_(431983)
    marks = _c_(431987, _a_(431986, _a_(431985, _n_(431984, "db", lambda: db), "columns"), "Integer"), primary_key=True)
    _l_(431988)
    username = _c_(431992, _a_(431991, _a_(431990, _n_(431989, "db", lambda: db), "columns"), "Text"), required=True)
    _l_(431993)
    password = _c_(431997, _a_(431996, _a_(431995, _n_(431994, "db", lambda: db), "columns"), "Text"))
    _l_(431998)

    @_c_(432001, _a_(432000, _n_(431999, "app", lambda: app), "route"), '/meriting')
    def show_meritlist():
        _l_(432026)

        ob = _c_(432012, _a_(432007, _c_(432006, _a_(432005, _c_(432004, _a_(432003, _n_(432002, "Student", lambda: Student), "objects")), "filter")), "only"), _a_(432009, _n_(432008, "Student", lambda: Student), "marks"), _a_(432011, _n_(432010, "Student", lambda: Student), "username"))
        _l_(432013)
        ob = _c_(432020, _a_(432019, _c_(432018, _a_(432015, _n_(432014, "ob", lambda: ob), "filter"), _a_(432017, _n_(432016, "Student", lambda: Student), "marks") >= 65), "allow_filtering"))
        _l_(432021)
        aux = _c_(432024, _n_(432022, "render_template", lambda: render_template), 'merit.html', ml = _n_(432023, "ob", lambda: ob))
        _l_(432025)
        return aux

_c_(432030, _a_(432029, _n_(432028, "db", lambda: db), "sync_db"))
_l_(432031)
if _n_(432032, "__name__", lambda: __name__) == '__main__':
    _l_(432037)

    _c_(432035, _a_(432034, _n_(432033, "app", lambda: app), "run"), debug = True)
    _l_(432036)