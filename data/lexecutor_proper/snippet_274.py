# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6392739/what-does-the-at-symbol-do-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df = _c_(62191, _a_(62190, _n_(62189, "pandas", lambda: pandas), "DataFrame"), {'foo': [1,2,15,17]})
_l_(62192)
y = 10
_l_(62193)
_n_(62194, "df", lambda: df) >> _c_(62196, _n_(62195, "query", lambda: query), 'foo > @y') # plydata
_l_(62197) # plydata
_c_(62200, _a_(62199, _n_(62198, "df", lambda: df), "query"), 'foo > @y') # pandas
_l_(62201) # pandas

