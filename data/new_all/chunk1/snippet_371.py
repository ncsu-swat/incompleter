# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50119668/attributeerror-generator-object-has-no-attribute-to-sql-while-creating-datf
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas.io.sql as psql
    _l_(381318)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(381320)

except ImportError:
    pass
try:
    from sqlalchemy import create_engine
    _l_(381322)

except ImportError:
    pass

def chunck_generator(filename, header=False,chunk_size = 10 ** 5):
    _l_(381331)

    for chunk in _c_(381327, _a_(381324, _n_(381323, "pd", lambda: pd), "read_fwf"), _n_(381325, "filename", lambda: filename), colspecs=[[0,12],[12,13]],index_col=False,header=None, iterator=True, chunksize=_n_(381326, "chunk_size", lambda: chunk_size)):
        _l_(381330)

        yield _n_(381328, "chunk", lambda: (chunk))
        _l_(381329)

def _generator( engine, filename, header=False,chunk_size = 10 ** 5):
    _l_(381343)

    chunk = _c_(381334, _n_(381332, "chunck_generator", lambda: chunck_generator), _n_(381333, "filename", lambda: filename), header=False,chunk_size = 10 ** 5)
    _l_(381335)
    _c_(381339, _a_(381337, _n_(381336, "chunk", lambda: chunk), "to_sql"), 'sample_table', _n_(381338, "engine", lambda: engine), if_exists='replace', schema='sample_schema', index=False)
    _l_(381340)
    yield _n_(381341, "row", lambda: row)
    _l_(381342)

if _n_(381344, "__name__", lambda: __name__) == "__main__":
    _l_(381372)

    filename = r'test_file.txt'
    _l_(381345)
    engine = _c_(381347, _n_(381346, "create_engine", lambda: create_engine), 'postgresql://ABCD:ABCD@ip:port/database')
    _l_(381348)
    c = _c_(381351, _a_(381350, _n_(381349, "engine", lambda: engine), "connect"))
    _l_(381352)
    conn = _a_(381354, _n_(381353, "c", lambda: c), "connection")
    _l_(381355)
    generator = _c_(381359, _n_(381356, "_generator", lambda: _generator), engine=_n_(381357, "engine", lambda: engine), filename=_n_(381358, "filename", lambda: filename))
    _l_(381360)
    while True:
        _l_(381367)

        _c_(381365, _n_(381361, "print", lambda: print), _c_(381364, _n_(381362, "next", lambda: next), _n_(381363, "generator", lambda: generator)))
        _l_(381366)
    _c_(381370, _a_(381369, _n_(381368, "conn", lambda: conn), "close"))
    _l_(381371)