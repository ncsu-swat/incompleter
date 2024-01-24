# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68492959/attributeerror-nonetype-object-has-no-attribute-fetchall-in-prefect
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_n_(617465, "task", lambda: task)
def sql_run_procs():
    _l_(617514)

    """This is a delete and update..."""
    # Get our logger
    logger = _c_(617470, _a_(617469, _a_(617468, _a_(617467, _n_(617466, "prefect", lambda: prefect), "utilities"), "logging"), "get_logger"))  # type: ignore
    _l_(617471)  # type: ignore

    conn = _c_(617479, _n_(617472, "connect_db", lambda: connect_db), _a_(617477, _a_(617476, _a_(617475, _a_(617474, _n_(617473, "prefect", lambda: prefect), "config"), "kv"), "p"), "prod_db_constring"), _n_(617478, "logger", lambda: logger))  ## wrapper around create_engine()
    _l_(617480)  ## wrapper around create_engine()

    with _c_(617483, _a_(617482, _n_(617481, "conn", lambda: conn), "connect")) as con:
        _l_(617513)

        try:
            _l_(617512)

            r = _c_(617493, _a_(617492, _c_(617491, _a_(617485, _n_(617484, "con", lambda: con), "execute"), f"EXECUTE fs.spETL_MyProc '{_a_(617490, _a_(617489, _a_(617488, _a_(617487, _n_(617486, 'prefect', lambda: prefect), 'config'), 'kv'), 'p'), 'staging_db_name')}'"
            ), "fetchall"))
            _l_(617494)
            for q in _n_(617495, "r", lambda: r)[0]:
                _l_(617507)

                if _n_(617496, "q", lambda: q) == 1:
                    _l_(617506)

                    _c_(617500, _a_(617498, _n_(617497, "logger", lambda: logger), "info"), f"Query {_n_(617499, 'q', lambda: q)} has failed")
                    _l_(617501)
                    raise _c_(617504, _a_(617503, _n_(617502, "signals", lambda: signals), "FAIL"))
                    _l_(617505)
        except :
            _l_(617511)

            raise _c_(617509, _n_(617508, "SQLAlchemyError", lambda: SQLAlchemyError), "Error in SQL Script")
            _l_(617510)