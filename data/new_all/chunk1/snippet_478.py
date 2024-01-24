# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64241141/how-to-solve-typeerror-sequence-item-0-expected-str-instance-float-found
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
docs_df = _c_(415014, _a_(415012, _n_(415011, "pd", lambda: pd), "DataFrame"), _n_(415013, "data", lambda: data), columns=["Doc"])
_l_(415015)
_n_(415016, "docs_df", lambda: docs_df)['Topic'] = _a_(415018, _n_(415017, "cluster", lambda: cluster), "labels_")
_l_(415019)
_n_(415020, "docs_df", lambda: docs_df)['Doc_ID'] = _c_(415025, _n_(415021, "range", lambda: range), _c_(415024, _n_(415022, "len", lambda: len), _n_(415023, "docs_df", lambda: docs_df)))
_l_(415026)
docs_per_topic = _c_(415032, _a_(415030, _c_(415029, _a_(415028, _n_(415027, "docs_df", lambda: docs_df), "groupby"), ['Topic'], as_index = False), "agg"), {'Doc': _a_(415031, ' ', "join")})
_l_(415033)