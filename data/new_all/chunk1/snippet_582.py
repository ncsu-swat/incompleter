# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77361799/attributeerror-dataframe-object-has-no-attribute-group-by
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import polars as pl
    _l_(395564)

except ImportError:
    pass
df = _c_(395567, _a_(395566, _n_(395565, "pl", lambda: pl), "DataFrame"), {
        "a": ["a", "b", "a", "b", "c"],
        "b": [1, 2, 1, 3, 3],
        "c": [5, 4, 3, 2, 1],
    }
)
_l_(395568)
_c_(395578, _a_(395572, _c_(395571, _a_(395570, _n_(395569, "df", lambda: df), "group_by"), "a"), "agg"), _c_(395577, _a_(395576, _c_(395575, _a_(395574, _n_(395573, "pl", lambda: pl), "col"), "b"), "sum")))
_l_(395579)