# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/17909954/python-ddl-program-if-statement-causing-name-error-when-using-y-n-instead-of-1
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sqlite3
    _l_(618682)

except ImportError:
    pass
#
def create_table(db_name,table_name,sql):
    _l_(618744)

    with _c_(618686, _a_(618684, _n_(618683, "sqlite3", lambda: sqlite3), "connect"), _n_(618685, "db_name", lambda: db_name)) as db:
        _l_(618743)

        cursor = _c_(618689, _a_(618688, _n_(618687, "db", lambda: db), "cursor"))
        _l_(618690)
        _c_(618694, _a_(618692, _n_(618691, "cursor", lambda: cursor), "execute"), 'select name from sqlite_master where name=?',(_n_(618693, "table_name", lambda: table_name),))
        _l_(618695)
        result = _c_(618698, _a_(618697, _n_(618696, "cursor", lambda: cursor), "fetchall"))
        _l_(618699)
        keep_table = True
        _l_(618700)
        if _c_(618703, _n_(618701, "len", lambda: len), _n_(618702, "result", lambda: result)) == 1:
            _l_(618731)

#Problem area
            response = _c_(618708, _n_(618704, "input", lambda: input), _c_(618707, _a_(618705, 'The table {0} already exists, do you wish to overide? (y/n): ', "format"), _n_(618706, "table_name", lambda: table_name)))
            _l_(618709)
            if _n_(618710, "response", lambda: response) == 'y':
                _l_(618729)

#Problem area end
                keep_table = False
                _l_(618711)
                _c_(618717, _a_(618713, _n_(618712, "cursor", lambda: cursor), "execute"), _c_(618716, _a_(618714, 'drop table if exists {0}', "format"), _n_(618715, "table_name", lambda: table_name)))
                _l_(618718)
                _c_(618720, _n_(618719, "print", lambda: print), 'Table overwritten')
                _l_(618721)
                _c_(618724, _a_(618723, _n_(618722, "db", lambda: db), "commit"))
                _l_(618725)
            else:
                _c_(618727, _n_(618726, "print", lambda: print), 'Table kept')
                _l_(618728)
        else:
            keep_table = False
            _l_(618730)
        if not _n_(618732, "keep_table", lambda: keep_table):
            _l_(618742)

            _c_(618736, _a_(618734, _n_(618733, "cursor", lambda: cursor), "execute"), _n_(618735, "sql", lambda: sql))
            _l_(618737)
            _c_(618740, _a_(618739, _n_(618738, "db", lambda: db), "commit"))
            _l_(618741)
#
if _n_(618745, "__name__", lambda: __name__) == '__main__':
    _l_(618753)

    db_name = 'coffee_shop.db'
    _l_(618746)
    sql = '''create table Product
             (ProductID integer,
             Name varchar(30),
             Price real,
             primary key(ProductID))'''
    _l_(618747)
    _c_(618751, _n_(618748, "create_table", lambda: create_table), _n_(618749, "db_name", lambda: db_name),'Product',_n_(618750, "sql", lambda: sql))
    _l_(618752)