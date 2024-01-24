# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61161498/why-binary-usage-in-sqlalchemy-with-python3-cause-a-typeerror-string-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sqlalchemy import MetaData, Integer, Column, Table, Binary, create_engine
    _l_(456063)

except ImportError:
    pass
try:
    from sqlalchemy.ext.declarative import declarative_base
    _l_(456065)

except ImportError:
    pass
try:
    from sqlalchemy.orm import sessionmaker, scoped_session
    _l_(456067)

except ImportError:
    pass

DB_CONFIG = {
        'user': 'user_test',
        'password': 'PSW_test',
        'host': '127.0.0.1',
        'database': 'db_test',
        }
_l_(456068)

if _n_(456069, "__name__", lambda: __name__) == '__main__':
    _l_(456156)

    Base = _c_(456071, _n_(456070, "declarative_base", lambda: declarative_base))
    _l_(456072)
    engine = _c_(456075, _n_(456073, "create_engine", lambda: create_engine), "mysql+mysqlconnector://%(user)s:%(password)s@%(host)s/%(database)s" % _n_(456074, "DB_CONFIG", lambda: DB_CONFIG),
                           echo=False)
    _l_(456076)
    _a_(456078, _n_(456077, "Base", lambda: Base), "metadata").bind = _n_(456079, "engine", lambda: engine)
    _l_(456080)
    db_sessionmaker = _c_(456083, _n_(456081, "sessionmaker", lambda: sessionmaker), bind=_n_(456082, "engine", lambda: engine))
    _l_(456084)
    Session = _c_(456087, _n_(456085, "scoped_session", lambda: scoped_session), _n_(456086, "db_sessionmaker", lambda: db_sessionmaker))
    _l_(456088)

    # create the table
    meta = _c_(456090, _n_(456089, "MetaData", lambda: MetaData))
    _l_(456091)
    tests = _c_(456100, _n_(456092, "Table", lambda: Table), 'test', _n_(456093, "meta", lambda: meta),
        _c_(456096, _n_(456094, "Column", lambda: Column), 'id', _n_(456095, "Integer", lambda: Integer), primary_key=True),
        _c_(456099, _n_(456097, "Column", lambda: Column), 'attr', _n_(456098, "Binary", lambda: Binary))
    )
    _l_(456101)
    _c_(456105, _a_(456103, _n_(456102, "meta", lambda: meta), "create_all"), _n_(456104, "engine", lambda: engine))
    _l_(456106)


    class Test(_n_(456107, "Base", lambda: Base)):
        _l_(456117)

        __tablename__ = 'test'
        _l_(456108)
        id = _c_(456111, _n_(456109, "Column", lambda: Column), _n_(456110, "Integer", lambda: Integer), primary_key=True)
        _l_(456112)
        attr = _c_(456115, _n_(456113, "Column", lambda: Column), _n_(456114, "Binary", lambda: Binary))
        _l_(456116)

    new_test = _c_(456121, _n_(456118, "Test", lambda: Test), attr=_c_(456120, _a_(456119, 'try', "encode"), 'utf-8'))
    _l_(456122)
    session = _c_(456124, _n_(456123, "Session", lambda: Session))
    _l_(456125)
    _c_(456129, _a_(456127, _n_(456126, "session", lambda: session), "add"), _n_(456128, "new_test", lambda: new_test))
    _l_(456130)
    _c_(456133, _a_(456132, _n_(456131, "session", lambda: session), "commit"))
    _l_(456134)
    result = _c_(456140, _a_(456139, _c_(456138, _a_(456136, _n_(456135, "session", lambda: session), "query"), _n_(456137, "Test", lambda: Test)), "all"))
    _l_(456141)
    for a in _n_(456142, "result", lambda: result):
        _l_(456151)

        _c_(456149, _n_(456143, "print", lambda: print), _n_(456144, "a", lambda: a), _a_(456146, _n_(456145, "a", lambda: a), "id"), _a_(456148, _n_(456147, "a", lambda: a), "attr"))
        _l_(456150)
    _c_(456154, _a_(456153, _n_(456152, "Session", lambda: Session), "remove"))
    _l_(456155)