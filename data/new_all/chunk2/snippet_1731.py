# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60078342/pandas-read-sql-query-throws-typeerror-nonetype-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_n_(429216, "contextmanager", lambda: contextmanager)
def open_db_connection(connection_string):
    _l_(429245)

    _n_(429217, "pyodbc", lambda: pyodbc).pooling = False
    _l_(429218)
    connection = _c_(429222, _a_(429220, _n_(429219, "pyodbc", lambda: pyodbc), "connect"), _n_(429221, "connection_string", lambda: connection_string))
    _l_(429223)

    try:
        _l_(429244)

        yield _n_(429224, "connection", lambda: connection)
        _l_(429225)
    except _a_(429227, _n_(429226, "pyodbc", lambda: pyodbc), "DatabaseError") as err:
        _l_(429238)

        error, = _a_(429229, _n_(429228, "err", lambda: err), "args")
        _l_(429230)
        _c_(429236, _a_(429233, _a_(429232, _n_(429231, "sys", lambda: sys), "stderr"), "write"), _a_(429235, _n_(429234, "error", lambda: error), "message"))
        _l_(429237)
    finally:
        _l_(429243)

        _c_(429241, _a_(429240, _n_(429239, "connection", lambda: connection), "close"))
        _l_(429242)

noCount = """ SET NOCOUNT ON; """
_l_(429246)
with _c_(429249, _n_(429247, "open_db_connection", lambda: open_db_connection), _n_(429248, "connection_string", lambda: connection_string)) as conn:
    _l_(429257)

    res = _c_(429255, _a_(429251, _n_(429250, "pd", lambda: pd), "read_sql_query"), _n_(429252, "noCount", lambda: noCount)+_n_(429253, "queryObj", lambda: queryObj), _n_(429254, "conn", lambda: conn))
    _l_(429256)