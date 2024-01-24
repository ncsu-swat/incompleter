# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61973622/attributeerror-dict-object-has-no-attribute-split
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
columns = []
_l_(382525)
rows = []
_l_(382526)
chunks = _c_(382529, _a_(382528, _n_(382527, "body", lambda: body), "split"), '}')
_l_(382530)
for chunk in _n_(382531, "chunks", lambda: chunks):
    _l_(382577)

    row = []
    _l_(382532)
    if _c_(382535, _n_(382533, "len", lambda: len), _n_(382534, "chunk", lambda: chunk))>1:
        _l_(382576)

        entry = _c_(382542, _a_(382541, _c_(382540, _a_(382539, _c_(382538, _a_(382537, _n_(382536, "chunk", lambda: chunk), "replace"), '{',''), "strip")), "split"), ',')
        _l_(382543)
        for e in _n_(382544, "entry", lambda: entry):
            _l_(382570)

            item = _c_(382549, _a_(382548, _c_(382547, _a_(382546, _n_(382545, "e", lambda: e), "strip")), "split"), ':')
            _l_(382550)
            if _c_(382553, _n_(382551, "len", lambda: len), _n_(382552, "item", lambda: item))==2:
                _l_(382569)

                _c_(382557, _a_(382555, _n_(382554, "row", lambda: row), "append"), _n_(382556, "item", lambda: item)[1])
                _l_(382558)
                if _c_(382562, _a_(382560, _n_(382559, "chunks", lambda: chunks), "index"), _n_(382561, "chunk", lambda: chunk))==0:
                    _l_(382568)

                    _c_(382566, _a_(382564, _n_(382563, "columns", lambda: columns), "append"), _n_(382565, "item", lambda: item)[0])
                    _l_(382567)
        _c_(382574, _a_(382572, _n_(382571, "rows", lambda: rows), "append"), _n_(382573, "row", lambda: row))
        _l_(382575)
df = _c_(382582, _a_(382579, _n_(382578, "pd", lambda: pd), "DataFrame"), _n_(382580, "rows", lambda: rows), columns = _n_(382581, "columns", lambda: columns))
_l_(382583)
_c_(382586, _a_(382585, _n_(382584, "df", lambda: df), "head"))
_l_(382587)

_c_(382590, _a_(382589, _n_(382588, "df", lambda: df), "to_csv"), 'r3edata.csv', index = False, header = True)
_l_(382591)