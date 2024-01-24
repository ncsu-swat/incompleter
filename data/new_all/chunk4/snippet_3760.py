# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68492959/attributeerror-nonetype-object-has-no-attribute-fetchall-in-prefect
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_n_(596321, "task", lambda: task)
def sql_run_procs():
    _l_(596370)

    """This is a clean, truncate and insert"""
    # Get our logger
    logger = _c_(596326, _a_(596325, _a_(596324, _a_(596323, _n_(596322, "prefect", lambda: prefect), "utilities"), "logging"), "get_logger"))  # type: ignore
    _l_(596327)  # type: ignore

    conn = _c_(596335, _n_(596328, "connect_db", lambda: connect_db), _a_(596333, _a_(596332, _a_(596331, _a_(596330, _n_(596329, "prefect", lambda: prefect), "config"), "kv"), "p"), "prod_db_constring"), _n_(596334, "logger", lambda: logger))
    _l_(596336)

    with _c_(596339, _a_(596338, _n_(596337, "conn", lambda: conn), "connect")) as con:
        _l_(596369)

        try:
            _l_(596368)

            r = _c_(596349, _a_(596348, _c_(596347, _a_(596341, _n_(596340, "con", lambda: con), "execute"), f"EXECUTE forms.spETL_MyOtherProc '{_a_(596346, _a_(596345, _a_(596344, _a_(596343, _n_(596342, 'prefect', lambda: prefect), 'config'), 'kv'), 'p'), 'staging_db_name')}'"
            ), "fetchall"))
            _l_(596350)
            for q in _n_(596351, "r", lambda: r)[0]:
                _l_(596363)

                if _n_(596352, "q", lambda: q) == 1:
                    _l_(596362)

                    _c_(596356, _a_(596354, _n_(596353, "logger", lambda: logger), "info"), f"Query {_n_(596355, 'q', lambda: q)} has failed")
                    _l_(596357)
                    raise _c_(596360, _a_(596359, _n_(596358, "signals", lambda: signals), "FAIL"))
                    _l_(596361)
        except :
            _l_(596367)

            raise _c_(596365, _n_(596364, "SQLAlchemyError", lambda: SQLAlchemyError), "Error in SQL Script")
            _l_(596366)