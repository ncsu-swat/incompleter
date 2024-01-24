# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64012754/geopandas-attributeerror-transaction-object-has-no-attribute-run-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sqlalchemy import create_engine
    _l_(636214)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(636216)

except ImportError:
    pass


def insert(df):
    _l_(636246)

    calidades_df = _c_(636219, _a_(636218, _n_(636217, "df", lambda: df), "copy"))
    _l_(636220)
    _c_(636224, _a_(636222, _n_(636221, "calidades_df", lambda: calidades_df), "insert"), loc=0, column='proceso', value=_n_(636223, "p", lambda: p)['proceso'])
    _l_(636225)
    _c_(636232, _a_(636227, _n_(636226, "calidades_df", lambda: calidades_df), "insert"), loc=_c_(636231, _n_(636228, "len", lambda: len), _a_(636230, _n_(636229, "calidades_df", lambda: calidades_df), "columns")),
        column='baja',
        value=False)
    _l_(636233)

    engine = _c_(636235, _n_(636234, "create_engine", lambda: create_engine), "postgres://usr:pass#@localhost:5432/database"
    )
    _l_(636236)
    with _c_(636239, _a_(636238, _n_(636237, "engine", lambda: engine), "begin")) as conn:
        _l_(636245)

        _c_(636243, _a_(636241, _n_(636240, "calidades_df", lambda: calidades_df), "to_postgis"), 'calidades',
            _n_(636242, "conn", lambda: conn),
            schema='ndvi',
            if_exists='append',
            index=False
            )
        _l_(636244)