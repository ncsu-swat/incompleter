# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59185633/typeerror-object-of-type-map-has-no-len-when-trying-to-insert-a-csv-into-an
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(470966)

except ImportError:
    pass
try:
    import pyodbc
    _l_(470968)

except ImportError:
    pass

thecsv = 'iamacsvfile.csv'
_l_(470969)

_c_(470971, _n_(470970, "print", lambda: print), 'connecting')
_l_(470972)
drivr = "SQL Server"
_l_(470973)
servr = "1.2.3.4"
_l_(470974)
db = "testdata"
_l_(470975)
username = "user"
_l_(470976)
password = "thepassword"
_l_(470977)
my_cnxn = _c_(470987, _a_(470979, _n_(470978, "pyodbc", lambda: pyodbc), "connect"), _c_(470986, _a_(470980, 'DRIVER={};SERVER={};DATABASE={};UID={};PWD={}', "format"), _n_(470981, "drivr", lambda: drivr),_n_(470982, "servr", lambda: servr),_n_(470983, "db", lambda: db),_n_(470984, "username", lambda: username),_n_(470985, "password", lambda: password)))
_l_(470988)

my_cursor = _c_(470991, _a_(470990, _n_(470989, "my_cnxn", lambda: my_cnxn), "cursor"))
_l_(470992)

def insert_records(table, thecsv, my_cursor, my_cnxn):
    _l_(471046)


    with _c_(470995, _n_(470993, "open", lambda: open), _n_(470994, "thecsv", lambda: thecsv)) as csvfile:
        _l_(471045)

        csvFile = _c_(470999, _a_(470997, _n_(470996, "csv", lambda: csv), "reader"), _n_(470998, "csvfile", lambda: csvfile), delimiter=',')
        _l_(471000)
        header = _c_(471003, _n_(471001, "next", lambda: next), _n_(471002, "csvFile", lambda: csvFile))
        _l_(471004)
        headers = _c_(471010, _n_(471005, "map", lambda: map), (lambda x: _c_(471008, _a_(471007, _n_(471006, "x", lambda: x), "strip"))), _n_(471009, "header", lambda: header))
        _l_(471011)
        insert = _c_(471014, _a_(471012, 'INSERT INTO {} (', "format"), _n_(471013, "table", lambda: table)) + _c_(471017, _a_(471015, ', ', "join"), _n_(471016, "headers", lambda: headers)) + _c_(471024, _a_(471018, ') VALUES ({})', "format"), _c_(471023, _a_(471019, ', ', "join"), _c_(471022, _n_(471020, "len", lambda: len), _n_(471021, "headers", lambda: headers)) * '?'))
        _l_(471025)
        for row in _n_(471026, "csvFile", lambda: csvFile):
            _l_(471044)

            values = _c_(471032, _n_(471027, "map", lambda: map), (lambda x: _c_(471030, _a_(471029, _n_(471028, "x", lambda: x), "strip"))), _n_(471031, "row", lambda: row))  
            _l_(471033)  
            _c_(471038, _a_(471035, _n_(471034, "my_cursor", lambda: my_cursor), "execute"), _n_(471036, "insert", lambda: insert), _n_(471037, "values", lambda: values)) 
            _l_(471039) 
            _c_(471042, _a_(471041, _n_(471040, "my_cnxn", lambda: my_cnxn), "commit"))
            _l_(471043)


table = 'dbo.iamthetable'
_l_(471047)
mycsv = _n_(471048, "thecsv", lambda: thecsv) 
_l_(471049) 
_c_(471055, _n_(471050, "insert_records", lambda: insert_records), _n_(471051, "table", lambda: table), _n_(471052, "mycsv", lambda: mycsv), _n_(471053, "my_cursor", lambda: my_cursor), _n_(471054, "my_cnxn", lambda: my_cnxn))
_l_(471056)
_c_(471059, _a_(471058, _n_(471057, "my_cursor", lambda: my_cursor), "close"))
_l_(471060)